"""ESCENA BASE (Blender/bpy): trader humano tras el escritorio + Clawd pequeño + PC con pantalla interactiva.
Se importa desde render_bases.py y render_conversacion.py. No se ejecuta sola."""
"""Escena v3: trader humano sentado tras el escritorio (cintura arriba), Clawd pequeño sobre el escritorio,
PC con pantalla interactiva (texturas), props. Uso: python3 -I scene2.py <tex_dir> <out_dir> [ids...]"""
import bpy, math, sys, os, random
from mathutils import Vector

TEX = os.environ.get('VC_TEX') or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tex')
R = math.radians

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'; sc.cycles.samples = int(os.environ.get('VC_SAMPLES', '32')); sc.cycles.use_denoising = True; sc.cycles.device = 'CPU'
sc.view_settings.view_transform = 'Standard'; sc.view_settings.exposure = -0.25
sc.render.resolution_x, sc.render.resolution_y = 540, 960
sc.render.image_settings.file_format = 'PNG'

# ------------------------------------------------------------------ utilidades
def lin(c): return tuple((x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4) for x in c)
def rgb(r, g, b): return lin((r / 255, g / 255, b / 255))

def mat(name, color, rough=0.6, emit=None, strength=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*color, 1); b.inputs['Roughness'].default_value = rough
    if emit:
        b.inputs['Emission Color'].default_value = (*emit, 1); b.inputs['Emission Strength'].default_value = strength
    return m

def tex_mat(name, path, strength=1.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; b = nt.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (0, 0, 0, 1); b.inputs['Roughness'].default_value = 0.4
    t = nt.nodes.new('ShaderNodeTexImage'); t.image = bpy.data.images.load(path); t.interpolation = 'Linear'
    nt.links.new(t.outputs['Color'], b.inputs['Emission Color']); b.inputs['Emission Strength'].default_value = strength
    return m

def flat(o, m):
    o.data.materials.append(m)
    for p in o.data.polygons: p.use_smooth = False
    return o

def empty(name, loc=(0, 0, 0), parent=None, rot=(0, 0, 0)):
    e = bpy.data.objects.new(name, None); sc.collection.objects.link(e)
    e.location = loc; e.parent = parent; e.rotation_euler = rot; return e

def cube(name, loc, scale, m, parent=None, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(); o = bpy.context.object
    o.name = name; o.scale = scale; o.parent = parent; o.location = loc; o.rotation_euler = rot
    return flat(o, m)

def ico(name, loc, scale, m, parent=None, sub=1, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=sub); o = bpy.context.object
    o.name = name; o.scale = scale; o.parent = parent; o.location = loc; o.rotation_euler = rot
    return flat(o, m)

def cyl(name, loc, r, h, m, parent=None, v=8, rot=(0, 0, 0), r2=None):
    if r2 is None: bpy.ops.mesh.primitive_cylinder_add(vertices=v, radius=r, depth=h)
    else: bpy.ops.mesh.primitive_cone_add(vertices=v, radius1=r, radius2=r2, depth=h)
    o = bpy.context.object; o.name = name; o.parent = parent; o.location = loc; o.rotation_euler = rot
    return flat(o, m)

def plane_tex(name, loc, w, h, m, rot=(R(90), 0, 0), parent=None):
    bpy.ops.mesh.primitive_plane_add(size=1); o = bpy.context.object
    o.name = name; o.scale = (w, h, 1); o.parent = parent; o.location = loc; o.rotation_euler = rot
    o.data.materials.append(m); return o

# ------------------------------------------------------------------ materiales
M_skin = mat('skin', rgb(238, 176, 136)); M_skin2 = mat('skin2', rgb(190, 120, 90))
M_dark = mat('dark', rgb(12, 12, 18), 0.5); M_white = mat('white', rgb(235, 235, 240), 0.5)
M_hood = mat('hood', rgb(30, 130, 125)); M_hood2 = mat('hood2', rgb(22, 98, 96)); M_cord = mat('cord', rgb(230, 230, 230))
M_beanie = mat('beanie', rgb(215, 45, 60)); M_beanie2 = mat('beanie2', rgb(160, 30, 45))
M_phone = mat('phone', rgb(225, 225, 235), 0.35); M_acc = mat('acc', rgb(255, 150, 60), 0.4, emit=rgb(255, 120, 40), strength=0.6)
M_hair = mat('hair', rgb(40, 28, 30)); M_blush = mat('blush', rgb(235, 120, 120))
M_chair = mat('chair', rgb(38, 40, 66), 0.7); M_chair2 = mat('chair2', rgb(54, 58, 92), 0.6)
M_claw = mat('claw', rgb(222, 112, 80), 0.55, emit=rgb(230, 90, 40), strength=0.18)
M_claw2 = mat('claw2', rgb(185, 85, 58), 0.6)
M_desk = mat('desk', rgb(110, 70, 55), 0.7); M_desk2 = mat('desk2', rgb(70, 44, 40), 0.8)
M_pad = mat('pad', rgb(40, 42, 90), 0.9); M_key = mat('key', rgb(60, 64, 96), 0.45); M_kbase = mat('kbase', rgb(26, 28, 46), 0.5)
M_keyhi = mat('keyhi', rgb(255, 140, 90), 0.45, emit=rgb(255, 120, 60), strength=0.5)
M_mug = mat('mug', rgb(240, 240, 235), 0.4); M_coffee = mat('coffee', rgb(60, 30, 18), 0.3)
M_steam = mat('steam', rgb(200, 205, 225), 0.9, emit=rgb(200, 205, 230), strength=0.25)
M_lampa = mat('lampa', rgb(40, 40, 60), 0.4); M_lampe = mat('lampe', rgb(255, 210, 140), 0.5, emit=rgb(255, 190, 110), strength=14)
M_pot = mat('pot', rgb(200, 120, 90), 0.7); M_leaf = mat('leaf', rgb(60, 170, 100), 0.6); M_leaf2 = mat('leaf2', rgb(40, 130, 85), 0.6)
M_b1 = mat('b1', rgb(230, 80, 90)); M_b2 = mat('b2', rgb(80, 150, 230)); M_b3 = mat('b3', rgb(240, 200, 80)); M_b4 = mat('b4', rgb(90, 200, 150))
M_note1 = mat('note1', rgb(255, 225, 90), 0.8, emit=rgb(255, 225, 90), strength=0.25); M_note2 = mat('note2', rgb(255, 130, 190), 0.8)
M_note3 = mat('note3', rgb(130, 220, 255), 0.8)
M_wall = mat('wall', rgb(52, 38, 96), 0.9); M_wall2 = mat('wall2', rgb(40, 28, 78), 0.9); M_floor = mat('floor', rgb(26, 20, 50), 0.8)
M_rug = mat('rug', rgb(120, 50, 110), 0.95); M_frame = mat('frame', rgb(18, 18, 26), 0.5)
M_led = mat('led', rgb(255, 80, 200), 0.4, emit=rgb(255, 60, 200), strength=9); M_led2 = mat('led2', rgb(60, 220, 255), 0.4, emit=rgb(60, 200, 255), strength=9)
M_shelf = mat('shelf', rgb(90, 58, 50), 0.7)
SCREENS = {n: tex_mat('scr_' + n, f'{TEX}/screen_{n}.png', 1.15) for n in ('vacia', 'chart', 'chat', 'order')}
M_window = tex_mat('window', f'{TEX}/window.png', 1.0); M_neon = tex_mat('neon', f'{TEX}/neon.png', 1.6); M_poster = tex_mat('poster', f'{TEX}/poster.png', 0.35)

# ------------------------------------------------------------------ decorado
cube('floor', (0, 0, -1.9), (9, 7, 0.05), M_floor)
cube('rug', (0.5, -0.8, -1.84), (3.6, 2.6, 0.02), M_rug)
cube('wall', (0.5, 3.3, 1.6), (9, 0.1, 5), M_wall)
cube('wall_low', (0.5, 3.18, -0.9), (9, 0.05, 1.0), M_wall2)       # zocalo
plane_tex('window', (-2.55, 3.2, 2.1), 2.7, 3.0, M_window)
for (x, z, w, h) in ((-2.55, 3.64, 2.9, 0.1), (-2.55, 0.58, 2.9, 0.1)): cube('wf', (x, 3.18, z), (w / 2, 0.06, h / 2), M_frame)
for x in (-3.95, -1.15): cube('wf', (x, 3.18, 2.1), (0.05, 0.06, 1.55), M_frame)
cube('wf', (-2.55, 3.18, 2.1), (0.03, 0.06, 1.5), M_frame)
plane_tex('neon', (3.3, 3.2, 3.1), 2.2, 0.76, M_neon)
plane_tex('poster', (0.1, 3.2, 3.15), 1.2, 1.6, M_poster)
# estante con cosas
cube('shelf', (3.3, 3.0, 1.9), (1.3, 0.16, 0.04), M_shelf)
for i, (c, h) in enumerate(((M_b1, 0.55), (M_b2, 0.48), (M_b3, 0.6), (M_b4, 0.42))):
    cube('sb', (2.5 + i * 0.17, 3.0, 1.94 + h / 2), (0.07, 0.11, h / 2), c)
ico('trophy_ball', (3.5, 3.0, 2.12), (0.14, 0.14, 0.14), M_acc, sub=1)
cyl('trophy_base', (3.5, 3.0, 1.97), 0.1, 0.1, M_phone)
# mini-planta colgante
cyl('hang_pot', (3.95, 3.0, 2.08), 0.14, 0.2, M_pot, r2=0.1)
for k in range(4): cube('hang_leaf', (3.95 + 0.14 * math.cos(k * 1.57), 3.0 + 0.1 * math.sin(k * 1.57), 2.28), (0.05, 0.05, 0.14), M_leaf, rot=(R(20 * math.sin(k * 1.57)), R(20 * math.cos(k * 1.57)), 0))

# escritorio
cube('desk_top', (1.0, 0.1, -0.06), (3.0, 1.05, 0.06), M_desk)
cube('desk_edge', (1.0, -0.96, -0.2), (3.0, 0.05, 0.2), M_desk2)
for x in (-1.9, 3.9): cube('desk_leg', (x, 0.1, -1.0), (0.12, 1.0, 0.9), M_desk2)
cube('drawer', (3.3, -0.9, -0.95), (0.62, 0.06, 0.55), M_desk2); cube('drawer_h', (3.3, -0.98, -0.8), (0.2, 0.02, 0.03), M_acc)
# silla (respaldo detras del humano)
cube('chair_back', (-0.6, 2.15, 0.45), (0.78, 0.14, 1.05), M_chair); cube('chair_back2', (-0.6, 2.02, 0.5), (0.62, 0.05, 0.85), M_chair2)
cyl('chair_post', (-0.6, 1.7, -1.1), 0.08, 1.6, M_dark);

# monitor (girado hacia el humano)
MON = empty('monitor', (2.05, 0.8, 0), rot=(0, 0, R(-24)))
cyl('mon_base', (0, 0, 0.03), 0.5, 0.06, M_dark, MON, v=8)
cube('mon_neck', (0, 0.1, 0.38), (0.1, 0.06, 0.38), M_dark, MON)
cube('mon_panel', (0, 0, 1.4), (1.62, 0.06, 0.95), M_frame, MON)
SCR = plane_tex('screen', (0, -0.065, 1.4), 3.0, 1.69, SCREENS['chart'], parent=MON)
cube('mon_chin', (0, -0.02, 0.5), (0.3, 0.04, 0.03), M_dark, MON)
for i, (c, dx, dz, rz) in enumerate(((M_note1, -1.35, 2.38, 6), (M_note2, -1.05, 2.4, -8), (M_note3, 1.45, 2.4, 4))):
    cube('note', (dx, -0.05, dz), (0.13, 0.01, 0.13), c, MON, (0, 0, R(rz)))
# LEDs traseros
for i in range(7): cube('led', (-1.6 + i * 0.53, 0.2, 0.55 + 1.45 * (i % 2)), (0.2, 0.02, 0.025), M_led if i % 2 else M_led2, MON)
cube('led_v', (-1.62, 0.2, 1.4), (0.025, 0.02, 0.95), M_led, MON); cube('led_v', (1.62, 0.2, 1.4), (0.025, 0.02, 0.95), M_led2, MON)

# teclado (con teclas)
KB = empty('kb', (-0.15, 0.35, 0), rot=(0, 0, R(6)))
cube('kb_base', (0, 0, 0.04), (0.82, 0.27, 0.04), M_kbase, KB)
for r in range(5):
    for c in range(14):
        if r == 4 and 2 < c < 11: continue
        cube('key', (-0.72 + c * 0.111, 0.2 - r * 0.1, 0.1), (0.04, 0.04, 0.02), M_keyhi if (r == 0 and c == 0) else M_key, KB)
cube('spacebar', (0, -0.2, 0.1), (0.4, 0.04, 0.02), M_key, KB)
# raton + alfombrilla
cube('mousepad', (1.0, 0.35, 0.015), (0.5, 0.42, 0.015), M_pad)
ico('mouse', (1.05, 0.35, 0.07), (0.1, 0.16, 0.06), M_white, sub=1)
cube('mouse_btn', (1.05, 0.44, 0.115), (0.08, 0.004, 0.006), M_dark)
# taza de cafe + vapor
MUG = empty('mug', (1.85, -0.05, 0))
cyl('mug_body', (0, 0, 0.17), 0.17, 0.34, M_mug, MUG)
cyl('mug_coffee', (0, 0, 0.325), 0.145, 0.02, M_coffee, MUG)
cube('mug_handle', (0.2, 0, 0.17), (0.04, 0.03, 0.1), M_mug, MUG); cube('mug_h2', (0.24, 0, 0.17), (0.02, 0.03, 0.07), M_mug, MUG)
cyl('saucer', (0, 0, 0.01), 0.27, 0.02, M_white, MUG)
# libros apilados
for i, (c, w, h, rz) in enumerate(((M_b2, 0.42, 0.07, 3), (M_b1, 0.38, 0.06, -5), (M_b3, 0.4, 0.07, 6), (M_b4, 0.34, 0.05, -2))):
    z = 0.07 + sum(0.14 if k < 2 else 0.12 for k in range(i)) * 0.5 + (0.0)
cube('book1', (3.05, 0.1, 0.07), (0.44, 0.32, 0.07), M_b2, rot=(0, 0, R(3)))
cube('book2', (3.05, 0.1, 0.205), (0.4, 0.3, 0.065), M_b1, rot=(0, 0, R(-6)))
cube('book3', (3.05, 0.1, 0.335), (0.42, 0.31, 0.065), M_b3, rot=(0, 0, R(5)))
for z in (0.07, 0.205, 0.335): cube('pages', (3.05, 0.1 - 0.0, z), (0.43, 0.30, 0.045), M_white, rot=(0, 0, R(0)))  # paginas sobresalen un poco
# lampara
LAMP = empty('lamp', (-1.3, 0.55, 0))
cyl('lamp_base', (0, 0, 0.03), 0.22, 0.06, M_lampa, LAMP)
cube('lamp_arm1', (0, 0, 0.45), (0.03, 0.03, 0.42), M_lampa, LAMP, (R(8), 0, 0))
cube('lamp_arm2', (0.0, -0.24, 0.84), (0.03, 0.3, 0.03), M_lampa, LAMP, (R(-12), 0, 0))
cyl('lamp_head', (0.0, -0.5, 0.82), 0.07, 0.22, M_lampa, LAMP, r2=0.21, rot=(R(140), 0, 0))
cyl('lamp_bulb', (0.0, -0.585, 0.725), 0.15, 0.02, M_lampe, LAMP, rot=(R(140), 0, 0))
# planta
cyl('pot', (3.6, 0.55, 0.15), 0.22, 0.3, M_pot, r2=0.16)
for k in range(7):
    a = k * 0.9; h = 0.28 + 0.14 * (k % 3)
    cube('leaf', (3.6 + 0.1 * math.cos(a), 0.55 + 0.1 * math.sin(a), 0.4 + h / 2), (0.045, 0.02, h / 2), M_leaf if k % 2 else M_leaf2, rot=(R(18 * math.sin(a)), R(-18 * math.cos(a)), R(a * 40)))
# cuaderno, boli, movil
cube('notebook', (-0.95, -0.4, 0.025), (0.28, 0.38, 0.025), M_b4, rot=(0, 0, R(-12)))
cube('notebook_p', (-0.95, -0.4, 0.052), (0.26, 0.36, 0.006), M_white, rot=(0, 0, R(-12)))
cube('pen', (-0.7, -0.5, 0.07), (0.015, 0.2, 0.015), M_acc, rot=(0, 0, R(30)))
cube('phone', (0.4, -0.55, 0.02), (0.1, 0.19, 0.02), M_dark, rot=(0, 0, R(18)))
cube('phone_s', (0.4, -0.55, 0.043), (0.085, 0.17, 0.003), mat('phs', rgb(60, 130, 255), 0.3, emit=rgb(60, 130, 255), strength=1.4), rot=(0, 0, R(18)))

# ------------------------------------------------------------------ humano (cintura arriba)
HU = empty('hum', (-0.6, 1.45, -0.28), rot=(0, 0, R(14)))
TORSO = empty('torso', (0, 0, 0), HU)
cube('torso_m', (0, 0, 0.4), (0.5, 0.29, 0.46), M_hood, TORSO)
cube('pocket', (0, -0.3, 0.12), (0.3, 0.02, 0.1), M_hood2, TORSO)
cube('hood_back', (0, 0.18, 0.86), (0.34, 0.14, 0.12), M_hood2, TORSO)
for sx in (-1, 1): cube('shoulder', (sx * 0.54, 0, 0.74), (0.14, 0.15, 0.14), M_hood, TORSO)
for sx in (-1, 1): cube('cord', (sx * 0.08, -0.3, 0.62), (0.012, 0.012, 0.13), M_cord, TORSO)
cube('neck', (0, 0, 0.93), (0.13, 0.12, 0.1), M_skin2, TORSO)
HEAD = empty('head', (0, 0, 1.4), TORSO)
ico('skull', (0, 0, 0), (0.37, 0.34, 0.39), M_skin, HEAD, 2)
ico('beanie', (0, 0.015, 0.28), (0.41, 0.37, 0.25), M_beanie, HEAD, 1)
ico('cuff', (0, 0.0, 0.2), (0.425, 0.385, 0.085), M_beanie2, HEAD, 1)
cube('pompom', (0, 0.1, 0.56), (0.075, 0.075, 0.075), M_beanie, HEAD, (R(15), R(20), 0))
for sx in (-1, 1):
    cube('sideburn', (sx * 0.33, -0.1, 0.02), (0.03, 0.05, 0.1), M_hair, HEAD)
    cube('ear', (sx * 0.37, 0.02, -0.04), (0.035, 0.06, 0.08), M_skin2, HEAD)
    cube('cup', (sx * 0.43, 0.02, 0.0), (0.075, 0.15, 0.16), M_phone, HEAD)
    cube('cup_acc', (sx * 0.5, 0.02, 0.0), (0.012, 0.09, 0.09), M_acc, HEAD)
    for a in (22, 42, 62):
        ar = R(a)
        cube('band', (sx * 0.47 * math.cos(ar), 0.02, 0.1 + 0.47 * math.sin(ar) + 0.0), (0.028, 0.04, 0.085), M_phone, HEAD, (0, R(-a * sx), 0))
cube('band_top', (0, 0.02, 0.575), (0.12, 0.04, 0.028), M_phone, HEAD)
M_eye = mat('eye', rgb(22, 14, 18), 0.25)
EYES = []
for sx in (-1, 1):
    ex = sx * 0.135
    pu = ico('eye', (ex, -0.345, 0.0), (0.042, 0.02, 0.062), M_eye, HEAD, 1)
    hl = cube('hl', (ex + 0.011, -0.362, 0.03), (0.011, 0.004, 0.011), M_white, HEAD)
    hl2 = cube('hl2', (ex + 0.011, -0.362, 0.03), (0.0, 0.0, 0.0), M_white, HEAD)
    EYES.append((pu, hl, hl2))
BROWS = [cube('brow', (sx * 0.135, -0.335, 0.115), (0.07, 0.012, 0.012), M_hair, HEAD) for sx in (-1, 1)]
MOUTH = cube('mouth', (0, -0.33, -0.11), (0.065, 0.012, 0.014), M_dark, HEAD)
for sx in (-1, 1): cube('blush', (sx * 0.2, -0.31, -0.07), (0.05, 0.008, 0.026), M_blush, HEAD)

ARM = {}
for name, sx in (('L', -1), ('R', 1)):
    sh = empty('sh' + name, (sx * 0.58, 0, 0.74), TORSO)
    cube('upper', (0, 0, -0.27), (0.1, 0.1, 0.27), M_hood, sh)
    el = empty('el' + name, (0, 0, -0.54), sh)
    cube('fore', (0, 0, -0.23), (0.085, 0.085, 0.23), M_hood, el)
    cube('cuff', (0, 0, -0.44), (0.095, 0.095, 0.03), M_hood2, el)
    cube('hand', (0, -0.01, -0.52), (0.09, 0.075, 0.085), M_skin, el)
    cube('thumb', (sx * -0.07, -0.04, -0.5), (0.025, 0.03, 0.045), M_skin, el)
    ARM[name] = (sh, el)

# poses: (hombro_x, hombro_y, codo_x, codo_y) para L y R, inclinacion cabeza (x,y,z), torso x
HPOSE = {   # solo queda la pose que funciona: manos en el teclado. (pensar/facepalm/encoger/inclinar/señalar se BORRARON: los brazos no articulaban bien)
    'type': dict(L=(-38, 6, -58, 0), R=(-38, -6, -58, 0), head=(0, 0, 0), lean=0),
}
# expresiones: boca(w,h), cejas(y, rot), ojos(escala z), pupila escala
EXPR = {
    'neutral':   dict(mouth=(0.08, 0.018), brow=(0.115, 0), eye=1.0),
    'talk':      dict(mouth=(0.06, 0.028), brow=(0.125, 0), eye=1.0),
    'worried':   dict(mouth=(0.06, 0.012), brow=(0.135, 14), eye=1.0),
    'smug':      dict(mouth=(0.09, 0.012), brow=(0.13, -10), eye=0.6),
    'happy':     dict(mouth=(0.09, 0.03), brow=(0.13, 0), eye=0.55),
}
def set_human(pose, expr):
    P = HPOSE[pose]
    for n in ('L', 'R'):
        a, b, c, d = P[n]; sh, el = ARM[n]
        sh.rotation_euler = (R(a), R(b), 0); el.rotation_euler = (R(c), R(d), 0)
    TORSO.rotation_euler = (R(P['lean']), 0, 0)
    HEAD.rotation_euler = (R(P['head'][0]), R(P['head'][1]), R(P['head'][2]))
    HEAD.location[2] = 1.4 + P.get('raise_', 0)
    E = EXPR[expr]
    MOUTH.scale = (E['mouth'][0], 0.015, E['mouth'][1])
    for i, br in enumerate(BROWS):
        br.location[2] = E['brow'][0]; br.rotation_euler = (0, R((1 if i == 0 else -1) * E['brow'][1]), 0)
    for pu, hl, hl2 in EYES:
        pu.scale[2] = 0.062 * E['eye']; hl.scale[2] = 0.011 if E['eye'] > 0.45 else 0.002; hl.location[2] = 0.03 * E['eye']

# ------------------------------------------------------------------ Clawd (pequeno)
CL = empty('claw', (0, 0, 0)); CL.scale = (0.36, 0.36, 0.36)
LEGS = [cube(f'leg{i}', (x, 0, 0.17), (0.1, 0.12, 0.17), M_claw2, CL) for i, x in enumerate((-0.52, -0.18, 0.18, 0.52))]
CB = empty('cbody', (0, 0, 0.3), CL)
cube('torso', (0, 0, 0.42), (0.62, 0.42, 0.42), M_claw, CB)
CARM = {}
for n, sx in (('L', -1), ('R', 1)):
    p = empty('carm' + n, (sx * 0.62, 0, 0.5), CB)
    cube('carm_m', (sx * 0.2, 0, 0), (0.22, 0.2, 0.15), M_claw, p); CARM[n] = p
CEYES = [cube('ceye', (sx * 0.26, -0.435, 0.6), (0.075, 0.02, 0.1), M_dark, CB) for sx in (-1, 1)]
CHL = [cube('chl', (sx * 0.26 + 0.02, -0.452, 0.65), (0.022, 0.006, 0.03), M_white, CB) for sx in (-1, 1)]
CPOSE = {   # Clawd: solo 'stand' (de pie) y 'look' (de espaldas mirando el monitor). Poses raras BORRADAS.
    'stand': dict(arms=(-18, 18), eye=1.0, squash=1.0, rz=-10, ry=0, hop=0),
    'look':  dict(arms=(-18, 18), eye=1.0, squash=1.0, rz=140, ry=0, hop=0),
}
def set_clawd(pos, pose, face=0):
    P = CPOSE[pose]
    CL.location = pos
    CL.rotation_euler = (0, R(P['ry']), R(P['rz'] + face))
    CB.scale = (1 / math.sqrt(P['squash']), 1 / math.sqrt(P['squash']), P['squash'])
    CARM['L'].rotation_euler = (0, R(P['arms'][0]), 0); CARM['R'].rotation_euler = (0, R(P['arms'][1]), 0)
    for e, h in zip(CEYES, CHL):
        e.scale[2] = 0.1 * P['eye']; h.scale[2] = 0.03 * (1 if P['eye'] > 0.5 else 0.1)
        if P['eye'] < 0.5: e.scale[0] = 0.11
        else: e.scale[0] = 0.075
    CB.location[2] = 0.3 + P['hop'] / 0.36 * 0.36 * 1.0 if not P.get('sit') else 0.14
    for i, l in enumerate(LEGS):
        if P.get('sit'):
            l.scale = (0.1, 0.12, 0.07); l.location = ((-0.62, -0.2, 0.62, 0.2)[i] if False else (-0.55, -0.3, 0.3, 0.55)[i] * 1.0, -0.25 if i in (1, 2) else -0.05, 0.07)
        else:
            l.scale = (0.1, 0.12, 0.17); l.location = ((-0.52, -0.18, 0.18, 0.52)[i], 0, 0.17)

# ------------------------------------------------------------------ luces y camara
def look(obj, target, up='Y'):
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat('-Z', up).to_euler()
def light(kind, loc, energy, color, tgt, size=2.0, spot=60):
    bpy.ops.object.light_add(type=kind, location=loc); l = bpy.context.object
    l.data.energy = energy; l.data.color = color
    if kind == 'AREA': l.data.size = size
    if kind == 'SPOT': l.data.spot_size = R(spot); l.data.spot_blend = 0.5
    look(l, tgt); return l
light('AREA', (1.3, -1.6, 1.6), 55, (0.45, 0.7, 1.0), (0.3, 0.9, 0.9), 2.4)                # reflejo pantalla
light('SPOT', (3.8, 3.0, 3.6), 5200, (1.0, 0.5, 0.15), (0.0, 1.0, 1.0), spot=75)           # contorno naranja
light('SPOT', (-3.8, 2.4, 3.4), 4200, (0.75, 0.35, 0.95), (-0.6, 1.4, 1.2), spot=70)       # contorno morado
light('AREA', (0.0, -5.0, 1.2), 40, (0.6, 0.55, 0.95), (0.3, 0.8, 0.6), 5.0)
light('AREA', (-1.6, -2.6, 2.4), 110, (1.0, 0.85, 0.75), (-0.6, 1.4, 1.2), 2.5)  # luz suave sobre la cara               # relleno suave
light('SPOT', (-1.3, 0.0, 1.3), 900, (1.0, 0.75, 0.45), (-0.9, 1.0, 0.3), spot=80)         # lampara calida
world = bpy.data.worlds.new('w'); sc.world = world; world.use_nodes = True
bg = world.node_tree.nodes['Background']; bg.inputs['Color'].default_value = (0.05, 0.03, 0.12, 1); bg.inputs['Strength'].default_value = 1.0

bpy.ops.object.camera_add(); cam = bpy.context.object; sc.camera = cam
cam.data.sensor_fit = 'HORIZONTAL'; cam.data.sensor_width = 36
cam.data.dof.use_dof = True; cam.data.dof.aperture_fstop = 2.8
def set_cam(pos, tgt, lens, focus=None):
    cam.location = pos; cam.data.lens = lens; look(cam, tgt)
    cam.data.dof.focus_distance = focus or (Vector(tgt) - Vector(pos)).length


# ====================================================================== API REUTILIZABLE
POS = {'kb': (0.55, 0.0, 0.1), 'pad': (1.0, 0.1, 0.03), 'books': (3.05, 0.1, 0.47), 'mug': (2.2, -0.35, 0.0),
       'front': (-0.2, -0.55, 0.0), 'lamp': (-1.1, 0.0, 0.0), 'edge': (0.9, -0.62, 0.0), 'screen': (1.55, 0.2, 0.0), 'plant': (3.2, 0.5, 0.0)}
# Los 4 PLANOS BASE (siempre neutros: humano tecleando, Clawd de pie)
BASES = {
    'humano':   dict(cam=((-0.3, -2.0, 1.45), (-0.5, 1.4, 1.2), 50), clawd='pad',    clawd_pose='stand', desc='Primer plano del humano'),
    'claude':   dict(cam=((2.4, -2.0, 0.8), (3.0, 0.1, 0.55), 50),   clawd='books',  clawd_pose='stand', desc='Clawd sobre los libros, la pantalla detras'),
    'pantalla': dict(cam=((1.2, -2.8, 0.9), (1.5, 0.6, 0.9), 45),    clawd='screen', clawd_pose='look',  desc='Clawd de espaldas mirando el monitor'),
    'dos':      dict(cam=((-0.4, -2.6, 0.9), (-0.7, 0.6, 0.7), 40),  clawd='lamp',   clawd_pose='stand', desc='Plano de los dos: humano y Clawd en el escritorio'),
}
PANTALLAS = tuple(SCREENS)   # chart, chat, order  (para anadir una nueva: motor/texturas.py + SCREENS)

def aplicar(base, pantalla='chart', h_habla=False, c_habla=False, frame=0, h_pose='type'):
    """Pone TODA la escena en el estado de un frame. Solo movimientos basicos:
    - humano habla: boca abre/cierra (alterna por frame) + cabeceo minimo
    - Clawd habla: botecitos (sube y baja) con un poco de squash, sin boca
    - parpadeo ocasional"""
    B = BASES[base]; par = frame % 2 == 0
    set_human(h_pose, 'talk' if (h_habla and par) else 'neutral')
    if h_habla and par: HEAD.rotation_euler[0] = R(3)
    if frame % 14 == 6:
        for pu, hl, hl2 in EYES: pu.scale[2] = 0.004; hl.scale[2] = 0.002
    set_clawd(POS[B['clawd']], B['clawd_pose'])
    if c_habla and par:
        CL.location[2] += 0.05; CB.scale[2] *= 1.06
    if frame % 14 == 6 and B['clawd_pose'] != 'look':
        for e, h in zip(CEYES, CHL): e.scale[2] = 0.012; h.scale[2] = 0.003
    SCR.data.materials.clear(); SCR.data.materials.append(SCREENS[pantalla])
    set_cam(*B['cam'])

def render(path):
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)
