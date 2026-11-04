"""Renderiza LA BIBLIOTECA de capas reutilizables (se hace UNA vez; los videos se montan despues con montar_video.py).

Por cada PLANO (camara) genera:
  fondo.png                       -> habitacion sin personajes, con la pantalla del monitor VACIA (neutra)
  humano_<emocion>_<boca>.png     -> solo el humano, fondo transparente (RGBA) + sombra sobre el escritorio
  claude_<estado>.png             -> solo Clawd, fondo transparente (RGBA)
y un manifest.json con el cuadrilatero de la pantalla (para pegar cualquier imagen en el monitor con perspectiva).

Uso:  python3 -I render_biblioteca.py <carpeta_salida> [plano ...]      (planos: humano dos claude espalda)
"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('VC_SAMPLES', '24')
os.environ.setdefault('VC_TEX', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tex'))
import escena as E
import bpy
from bpy_extras.object_utils import world_to_camera_view

OUT = sys.argv[1]; ONLY = sys.argv[2:]
W, H = 720, 1280
sc = E.sc; sc.render.resolution_x, sc.render.resolution_y = W, H
sc.render.image_settings.color_mode = 'RGBA'

def tree(r):
    o = [r]
    for c in r.children: o += tree(c)
    return o
HUM = set(tree(E.HU)); CLA = set(tree(E.CL))
MESHES = [o for o in bpy.data.objects if o.type == 'MESH']
DESK = bpy.data.objects['desk_top']

def reset():
    sc.render.film_transparent = False
    for o in MESHES: o.is_holdout = False; o.is_shadow_catcher = False; o.hide_render = False

def capa_fondo():
    reset()
    for o in HUM | CLA: o.hide_render = True

def capa_personaje(quien):   # 'h' o 'c'
    reset(); sc.render.film_transparent = True
    mios, otros = (HUM, CLA) if quien == 'h' else (CLA, HUM)
    for o in otros: o.hide_render = True
    for o in MESHES:
        if o in HUM or o in CLA: continue
        o.is_holdout = True            # el resto de la sala recorta (oclusion correcta) pero no se ve
    DESK.is_holdout = False; DESK.is_shadow_catcher = True   # solo su sombra

# --- estados del humano: emocion x boca
EMO = {'neutral': 'neutral', 'feliz': 'happy', 'preocupado': 'worried', 'burlon': 'smug'}
BOCA = {'cerrada': None, 'media': (0.058, 0.02), 'abierta': (0.052, 0.04)}
def humano(emo, boca, parpadeo=False):
    E.set_human('type', EMO[emo])
    if BOCA[boca]: E.MOUTH.scale = (BOCA[boca][0], 0.015, BOCA[boca][1])
    if parpadeo:
        for pu, hl, hl2 in E.EYES: pu.scale[2] = 0.004; hl.scale[2] = 0.002

# --- estados de Clawd (siempre neutros)
def claude(pos, estado, pose='stand'):
    E.set_clawd(E.POS[pos], pose)
    if estado == 'parpadeo':
        for e, h in zip(E.CEYES, E.CHL): e.scale[2] = 0.012; h.scale[2] = 0.003
    elif estado == 'feliz':   # ojos ^ ^ (sin brazos raros)
        for e, h in zip(E.CEYES, E.CHL): e.scale[2] = 0.035; e.scale[0] = 0.11; h.scale[2] = 0.003

PLANOS = {
    'humano':  dict(base='humano',   humano=True,  clawd=None),
    'dos':     dict(base='dos',      humano=True,  clawd=('lamp', 'stand')),
    'claude':  dict(base='claude',   humano=False, clawd=('books', 'stand')),
    'espalda': dict(base='pantalla', humano=False, clawd=('screen', 'look')),
}

def quad_pantalla():
    bpy.context.view_layer.update()
    pts = []
    for sx, sy in ((-0.5, 0.5), (0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)):   # sup-izq, sup-der, inf-der, inf-izq
        co = E.SCR.matrix_world @ E.Vector((sx, sy, 0))
        p = world_to_camera_view(sc, E.cam, co)
        pts.append([round(p.x * W, 1), round((1 - p.y) * H, 1)])
    return pts

os.makedirs(OUT, exist_ok=True)
mf_path = os.path.join(OUT, 'manifest.json')
manifest = json.load(open(mf_path)) if os.path.exists(mf_path) else {'tamano': [W, H], 'planos': {}}

for nombre, P in PLANOS.items():
    if ONLY and nombre not in ONLY: continue
    d = os.path.join(OUT, nombre); os.makedirs(d, exist_ok=True)
    B = E.BASES[P['base']]
    E.SCR.data.materials.clear(); E.SCR.data.materials.append(E.SCREENS['vacia'])
    E.set_cam(*B['cam'])
    info = {'camara': [list(B['cam'][0]), list(B['cam'][1]), B['cam'][2]], 'descripcion': B['desc'],
            'pantalla_quad': quad_pantalla(), 'fondo': 'fondo.png', 'humano': {}, 'claude': {}}
    # fondo
    E.set_human('type', 'neutral'); E.set_clawd(E.POS['lamp'], 'stand')
    capa_fondo(); E.render(f'{d}/fondo.png'); print('OK', nombre, 'fondo', flush=True)
    # humano
    if P['humano']:
        for emo in EMO:
            for boca in BOCA:
                humano(emo, boca); capa_personaje('h')
                f = f'humano_{emo}_{boca}.png'; E.render(f'{d}/{f}'); info['humano'][f'{emo}_{boca}'] = f
                print('OK', nombre, f, flush=True)
        humano('neutral', 'cerrada', parpadeo=True); capa_personaje('h')
        E.render(f'{d}/humano_neutral_parpadeo.png'); info['humano']['neutral_parpadeo'] = 'humano_neutral_parpadeo.png'
    # clawd
    if P['clawd']:
        pos, pose = P['clawd']
        estados = ['idle'] if pose == 'look' else ['idle', 'parpadeo', 'feliz']
        for est in estados:
            claude(pos, est, pose); capa_personaje('c')
            f = f'claude_{est}.png'; E.render(f'{d}/{f}'); info['claude'][est] = f
            print('OK', nombre, f, flush=True)
    manifest['planos'][nombre] = info
    json.dump(manifest, open(mf_path, 'w'), indent=1, ensure_ascii=False)
reset(); print('BIBLIOTECA LISTA')
