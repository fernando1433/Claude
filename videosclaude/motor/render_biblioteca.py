"""Renderiza LA BIBLIOTECA de capas reutilizables (se hace UNA vez; los videos se montan despues con montar_video.py).
REANUDABLE: no vuelve a renderizar capas que ya existen (usa --forzar para rehacerlas).

Por cada PLANO (camara) genera, en biblioteca/<plano>/:
  fondo.png                         habitacion sin personajes, monitor con pantalla `vacia`
  sombra_humano.png / sombra_claude.png   SOLO la sombra de cada personaje (capa FIJA: no se mueve con los botecitos)
  humano_<emocion>_<boca>.png       humano pose 'type' (manos en el teclado), RGBA sin sombra
  humano_<pose>_<emocion>_<boca>.png   poses extra (IK): pensar, senalar, hombros, mira
  claude_<estado>.png               Clawd (idle, parpadeo, feliz, mira_izq, mira_der, mira_arriba), RGBA sin sombra
y manifest.json con el cuadrilatero de la pantalla de cada plano (para pegar cualquier imagen en el monitor con perspectiva).

Uso:  python3 -I render_biblioteca.py <carpeta_salida> [plano ...] [--forzar] [--sin-fondo]
"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('VC_SAMPLES', '24')
os.environ.setdefault('VC_TEX', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tex'))
import escena as E
import bpy
import numpy as np
from PIL import Image
from bpy_extras.object_utils import world_to_camera_view

OUT = sys.argv[1]; ARGS = sys.argv[2:]
FORZAR = '--forzar' in ARGS
ONLY = [a for a in ARGS if not a.startswith('--')]
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

def capa_personaje(quien):   # SOLO el personaje, SIN sombra
    reset(); sc.render.film_transparent = True
    otros = CLA if quien == 'h' else HUM
    for o in otros: o.hide_render = True
    for o in MESHES:
        if o in HUM or o in CLA: continue
        o.is_holdout = True

def capa_sombra(visibles):
    reset(); sc.render.film_transparent = True
    for o in HUM | CLA: o.hide_render = o not in visibles
    for o in MESHES:
        if o in HUM or o in CLA: o.is_holdout = True
        elif o is DESK: o.is_shadow_catcher = True
        else: o.is_holdout = True

def hacer(ruta, fn):
    """renderiza solo si no existe (o --forzar)"""
    if os.path.exists(ruta) and not FORZAR: return False
    fn(); return True

def sombra_de(quien, ruta, tmp0):
    vis = HUM if quien == 'h' else CLA
    capa_sombra(vis); E.render(ruta + '.tmp.png')
    a1 = np.array(Image.open(ruta + '.tmp.png').convert('RGBA'))[..., 3].astype(int)
    a0 = np.array(Image.open(tmp0).convert('RGBA'))[..., 3].astype(int)
    d = np.clip(a1 - a0, 0, 255).astype(np.uint8)
    o = np.zeros(d.shape + (4,), np.uint8); o[..., 3] = d
    Image.fromarray(o, 'RGBA').save(ruta); os.remove(ruta + '.tmp.png')

EMO = {'neutral': 'neutral', 'feliz': 'happy', 'preocupado': 'worried', 'burlon': 'smug'}
BOCA = {'cerrada': None, 'media': (0.058, 0.02), 'abierta': (0.052, 0.04)}
def humano(pose, emo, boca, parpadeo=False):
    E.set_human(pose, EMO[emo])
    if BOCA[boca]: E.MOUTH.scale = (BOCA[boca][0], 0.015, BOCA[boca][1])
    if parpadeo:
        for pu, hl, hl2 in E.EYES: pu.scale[2] = 0.004; hl.scale[2] = 0.002

MIRADAS = {'mira_izq': (-0.06, 0), 'mira_der': (0.06, 0), 'mira_arriba': (0, 0.05)}
def claude(pos, estado, pose='stand', face=0):
    E.set_clawd(E.POS[pos], pose, face)
    if estado == 'parpadeo':
        for e, h in zip(E.CEYES, E.CHL): e.scale[2] = 0.012; h.scale[2] = 0.003
    elif estado == 'feliz':
        for e, h in zip(E.CEYES, E.CHL): e.scale[2] = 0.035; e.scale[0] = 0.11; h.scale[2] = 0.003
    elif estado in MIRADAS:
        dx, dz = MIRADAS[estado]
        for e, h in zip(E.CEYES, E.CHL): e.location[0] += dx; e.location[2] += dz; h.location[0] += dx; h.location[2] += dz

TODAS = list(EMO); BOCAS = list(BOCA)
POSES_NUEVAS = {'pensar': ['neutral', 'preocupado'], 'senalar': ['neutral', 'feliz'], 'hombros': ['neutral', 'preocupado'], 'mira': ['neutral', 'feliz']}
CL_BASE = ['idle', 'parpadeo', 'feliz']; CL_MIRA = CL_BASE + list(MIRADAS)
# humano: type_emos = emociones de la pose 'type'; poses = poses extra
PLANOS = {
    'humano':  dict(base='humano',  humano=dict(type_emos=TODAS, poses=POSES_NUEVAS), clawd=None),
    'dos':     dict(base='dos',     humano=dict(type_emos=TODAS, poses=POSES_NUEVAS), clawd=('lamp', 'stand', 0, CL_MIRA)),
    'claude':  dict(base='claude',  humano=None, clawd=('books', 'stand', 0, CL_MIRA)),
    'espalda': dict(base='pantalla', humano=None, clawd=('screen', 'look', 0, ['idle'])),
    'monitor':         dict(base='monitor',         humano=None, clawd=('monitor_frente', 'stand', -13, CL_MIRA), f=6.0),
    'monitor_espalda': dict(base='monitor_espalda', humano=None, clawd=('monitor_espalda', 'look', 16, ['idle']), f=6.0),
    # --- tomas extra
    'general':         dict(base='general', humano=dict(type_emos=['neutral', 'feliz'], poses={'senalar': ['neutral']}), clawd=('pad', 'stand', 0, CL_BASE), f=4.0),
    'cenital':         dict(base='cenital', humano=None, clawd=('kb', 'stand', 0, CL_MIRA), f=5.6),
    'claude_ojos':     dict(base='claude_ojos', humano=None, clawd=('books', 'stand', 0, CL_MIRA), f=5.6),
    'monitor_lateral': dict(base='monitor_lateral', humano=None, clawd=('monitor_frente', 'stand', 48, CL_BASE), f=6.0),
}

def quad_pantalla():
    bpy.context.view_layer.update(); pts = []
    for sx, sy in ((-0.5, 0.5), (0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)):
        co = E.SCR.matrix_world @ E.Vector((sx, sy, 0)); p = world_to_camera_view(sc, E.cam, co)
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
    E.set_cam(*B['cam']); E.cam.data.dof.aperture_fstop = P.get('f', 2.8)
    info = {'camara': [list(B['cam'][0]), list(B['cam'][1]), B['cam'][2]], 'descripcion': B['desc'],
            'pantalla_quad': quad_pantalla(), 'fondo': 'fondo.png', 'sombra': {}, 'humano': {}, 'claude': {}}
    E.set_human('type', 'neutral'); E.set_clawd(E.POS['lamp'], 'stand')
    if hacer(f'{d}/fondo.png', lambda: (capa_fondo(), E.render(f'{d}/fondo.png'))): print('OK', nombre, 'fondo', flush=True)
    tmp0 = f'{d}/_s0.png'; capa_sombra(set()); E.render(tmp0)
    Hs = P['humano']
    if Hs:
        E.set_human('type', 'neutral')
        if hacer(f'{d}/sombra_humano.png', lambda: sombra_de('h', f'{d}/sombra_humano.png', tmp0)): print('OK', nombre, 'sombra_humano', flush=True)
        info['sombra']['humano'] = 'sombra_humano.png'
        def capa_h(pose, emo, boca, parp=False):
            sufijo = 'parpadeo' if parp else boca
            f = f'humano_{emo}_{sufijo}.png' if pose == 'type' else f'humano_{pose}_{emo}_{sufijo}.png'
            clave = f'{emo}_{sufijo}' if pose == 'type' else f'{pose}:{emo}_{sufijo}'
            def r(): humano(pose, emo, boca, parp); capa_personaje('h'); E.render(f'{d}/{f}')
            if hacer(f'{d}/{f}', r): print('OK', nombre, f, flush=True)
            info['humano'][clave] = f
        for emo in Hs['type_emos']:
            for boca in BOCAS: capa_h('type', emo, boca)
        capa_h('type', 'neutral', 'cerrada', True)
        for pose, emos in Hs['poses'].items():
            for emo in emos:
                for boca in BOCAS: capa_h(pose, emo, boca)
    if P['clawd']:
        pos, pose, face, estados = P['clawd']
        claude(pos, 'idle', pose, face)
        if hacer(f'{d}/sombra_claude.png', lambda: sombra_de('c', f'{d}/sombra_claude.png', tmp0)): print('OK', nombre, 'sombra_claude', flush=True)
        info['sombra']['claude'] = 'sombra_claude.png'
        for est in estados:
            f = f'claude_{est}.png'
            def r(): claude(pos, est, pose, face); capa_personaje('c'); E.render(f'{d}/{f}')
            if hacer(f'{d}/{f}', r): print('OK', nombre, f, flush=True)
            info['claude'][est] = f
    os.remove(tmp0)
    manifest['planos'][nombre] = info
    json.dump(manifest, open(mf_path, 'w'), indent=1, ensure_ascii=False)
reset(); print('BIBLIOTECA LISTA')
