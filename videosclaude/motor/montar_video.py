"""MONTADOR: crea un video a partir de un GUION (json) usando SOLO la biblioteca de capas ya renderizada.
No usa Blender, no renderiza nada: son unos segundos de PIL + ffmpeg.

Uso:   python3 -I motor/montar_video.py guiones/ejemplo_dip.json salidas/ejemplo_dip.mp4
Opciones:  --solo-frames N   (monta solo los N primeros frames, para probar)

Guion (ver guiones/ejemplo_dip.json):
  ambiente: noche_trading (por defecto) | dia_trading | dia_tienda | atardecer_tienda   (carpeta de biblioteca/ con la sala de ese ambiente)
  (humano) pose: type (por defecto, manos en el teclado) | pensar | senalar | hombros | mira   (la que no exista en el plano se sustituye por type)
  (claude) claude_estado: idle | feliz | mira_izq | mira_der | mira_arriba   empuje: true (zoom lento durante la linea; opcional)
  tono (opcional): sarcastico (por defecto en claude: voz grave que arrastra hacia abajo) | dudoso (sube al final) | seguro (por defecto en humano)
  sfx (opcional, true por defecto): whoosh en los cortes de plano y pop al cambiar la pantalla
  fps_animacion  frames de animacion por segundo (6 recomendado: poco movimiento, se duplica a 24 al exportar)
  duracion       segundos totales
  lineas[]:  inicio, fin (s) | quien: "humano"|"claude" | texto | plano: humano|dos|claude|espalda (opcional)
             emocion: neutral|feliz|preocupado|burlon (humano, opcional) | claude_estado: idle|feliz (opcional)
             pantalla: nombre de la pantalla del monitor (opcional, se mantiene hasta que cambie)
  cambios_pantalla[]: {"t": seg, "pantalla": "nombre"}  (cambios extra en mitad de una linea o en silencio)
Pantallas del monitor (campo `pantalla`):
  - ANIMADAS (motor/pantallas.py): chat dashboard tienda calendario email analitica tareas hoja -> se animan solas (cifras que suben, texto que se teclea...)
    forma larga: {"tipo":"dashboard","datos":{"ingresos":9800},"duracion":4}   (duracion = segundos que tarda la animacion)
  - ESTATICAS: biblioteca/pantallas/<nombre>.png (1280x720: vacia, chart, chat, order) o una ruta a cualquier imagen.
Planos con monitor: monitor (centrado, Clawd al pie), monitor_espalda (Clawd de espaldas), dos, claude, espalda.
Plano especial `pantalla_completa`: la pantalla ocupa el video (fondo difuminado); campo `zoom`:[x0,y0,x1,y1] (coords 1280x720) recorta y amplia una zona; si no lo pones, usa un recorte automatico (pantallas.ZOOM_AUTO); `"zoom": false` = pantalla entera.
"""
import sys, os, json, math, subprocess, wave, random, glob
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pantallas import dibujar, PANTALLAS, ZOOM_AUTO
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
BIB_RAIZ = os.path.join(RAIZ, 'biblioteca'); PANT = os.path.join(BIB_RAIZ, 'pantallas'); BIB = None
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
COL = {'humano': (120, 220, 215), 'claude': (240, 125, 85)}
SOMBRA = 0.55   # intensidad de las sombras fijas (0-1)
CICLO_BOCA = ['media', 'abierta', 'media', 'cerrada', 'abierta', 'media']

def args():
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    n = None
    if '--solo-frames' in sys.argv: n = int(sys.argv[sys.argv.index('--solo-frames') + 1]); a = [x for x in a if x != str(n)]
    return a[0], a[1], n

# ---------------------------------------------------------------- biblioteca
_cache = {}
MF = None; W = H = None
def usar_ambiente(nombre):
    """selecciona la biblioteca de un ambiente (carpeta biblioteca/<nombre>): noche_trading, dia_trading, dia_tienda, atardecer_tienda..."""
    global BIB, MF, W, H
    BIB = os.path.join(BIB_RAIZ, nombre); MF = json.load(open(os.path.join(BIB, 'manifest.json'))); W, H = MF['tamano']; _cache.clear()
usar_ambiente('noche_trading')
def cargar(plano, fichero):
    k = (plano, fichero)
    if k not in _cache: _cache[k] = Image.open(os.path.join(BIB, plano, fichero)).convert('RGBA')
    return _cache[k]

def clave_pantalla(spec): return json.dumps(spec, sort_keys=True) if isinstance(spec, dict) else spec

def imagen_pantalla(spec, p=1.0):
    """spec: nombre (animada o estatica) o dict {tipo, datos, duracion}. p = progreso 0..1 de la animacion."""
    nombre, datos = (spec['tipo'], spec.get('datos')) if isinstance(spec, dict) else (spec, None)
    return dibujar(nombre, p, datos).convert('RGB') if nombre in PANTALLAS else cargar_pantalla(nombre)

def cargar_pantalla(nombre):
    ruta = nombre if os.path.exists(nombre) else os.path.join(PANT, nombre + '.png')
    return Image.open(ruta).convert('RGB')

def coef_perspectiva(quad, w, h):
    """coeficientes PIL (salida->entrada) para pegar una imagen w x h en el cuadrilatero quad (TL,TR,BR,BL)"""
    src = [(0, 0), (w, 0), (w, h), (0, h)]; A = []; B = []
    for (x, y), (u, v) in zip(quad, src):
        A.append([x, y, 1, 0, 0, 0, -x * u, -y * u]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -x * v, -y * v]); B.append(v)
    return np.linalg.solve(np.array(A, float), np.array(B, float))

def fondo_con_pantalla(plano, pantalla, p=1.0):
    nom = pantalla['tipo'] if isinstance(pantalla, dict) else pantalla
    q_ = round(p * 40) if nom in PANTALLAS else 0           # las animadas cambian cada frame; las estaticas se cachean
    k = ('fondo', plano, clave_pantalla(pantalla), q_)
    if k in _cache: return _cache[k]
    fondo = cargar(plano, 'fondo.png').copy()
    if pantalla != 'vacia':
        img = imagen_pantalla(pantalla, q_ / 40 if nom in PANTALLAS else 1.0); img = ImageEnhance.Brightness(img).enhance(0.9)
        q = MF['planos'][plano]['pantalla_quad']; c = coef_perspectiva(q, img.width, img.height)
        warp = img.convert('RGBA').transform((W, H), Image.PERSPECTIVE, tuple(c), Image.BICUBIC)
        mask = Image.new('L', img.size, 255).transform((W, H), Image.PERSPECTIVE, tuple(c), Image.BICUBIC)
        warp.putalpha(mask); fondo = Image.alpha_composite(fondo, warp)
    if len([1 for kk in _cache if kk[0] == 'fondo']) > 150: _cache.pop(next(kk for kk in _cache if kk[0] == 'fondo'))
    _cache[k] = fondo; return fondo

def pantalla_completa(spec, p, zoom=None):
    """plano especial: la pantalla del monitor ocupa el video (fondo = sala difuminada y oscurecida)"""
    bg = cargar('monitor', 'fondo.png').convert('RGB').filter(ImageFilter.GaussianBlur(16)); bg = ImageEnhance.Brightness(bg).enhance(0.32)
    img = imagen_pantalla(spec, p)
    if zoom: img = img.crop(tuple(zoom))
    ancho = int(W * 0.96); alto = int(img.height * ancho / img.width)
    if alto > H * 0.8: alto = int(H * 0.8); ancho = int(img.width * alto / img.height)
    img = img.resize((ancho, alto), Image.LANCZOS)
    x, y = (W - ancho) // 2, int(H * 0.46 - alto / 2)
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(glow).rounded_rectangle((x - 6, y - 6, x + ancho + 6, y + alto + 6), 26, fill=(240, 125, 85, 70))
    bg = Image.alpha_composite(bg.convert('RGBA'), glow.filter(ImageFilter.GaussianBlur(18)))
    mask = Image.new('L', (ancho, alto), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, ancho, alto), 20, fill=255)
    bg.paste(img, (x, y), mask); return bg

def sombra_capa(plano, f):
    k = ('sombra', plano, f)
    if k not in _cache:
        im = cargar(plano, f).copy(); a = im.getchannel('A').point(lambda v: int(v * SOMBRA)); im.putalpha(a); _cache[k] = im
    return _cache[k]

def desplazar(capa, dy):
    out = Image.new('RGBA', capa.size, (0, 0, 0, 0)); out.paste(capa, (0, dy), capa); return out

# ---------------------------------------------------------------- audio (voces "blip" + pad ambiente)
def generar_audio(G, ruta):
    SR = 44100; dur = G['duracion']; out = np.zeros(int(SR * dur)); rnd = random.Random(11)
    def blip(f, d, who):
        n = int(SR * d); t = np.arange(n) / SR
        if who == 'humano': w = 2 * np.abs(2 * ((t * f) % 1) - 1) - 1 + 0.25 * np.sign(np.sin(2 * np.pi * f * 2 * t))
        else: w = np.sign(np.sin(2 * np.pi * f * t)) * 0.6 + 0.4 * np.sin(2 * np.pi * f * 2 * t)
        return w * np.minimum(1, t / 0.006) * np.exp(-t / (d * 0.55))
    for L in G['lineas']:
        ch = [c for c in L['texto'] if c.isalpha()]
        if not ch: continue
        a, b, who = L['inicio'], L['fin'], L['quien']; base = 120 if who == 'humano' else 520
        paso = (b - a - 0.12) / len(ch)
        for i, c in enumerate(ch):
            f = base * (2 ** (((ord(c.lower()) * 7) % 9 - 4) / 12)); fr = i / max(1, len(ch)); tono = L.get('tono') or ('sarcastico' if who == 'claude' else 'seguro')
            if tono == 'sarcastico': f *= 0.9 * (1 - 0.16 * fr) * (1 + 0.025 * math.sin(i * 1.3))      # voz mas grave que arrastra hacia abajo, con retintin
            elif tono == 'dudoso': f *= 1 + 0.12 * fr
            if who == 'humano': f *= 1 + 0.04 * rnd.uniform(-1, 1)
            if L['texto'].rstrip().endswith('?') and i > len(ch) * 0.7: f *= 1 + 0.1 * (i - len(ch) * 0.7)
            larga = 1.7 if (tono == 'sarcastico' and i >= len(ch) - 2) else 1.0
            s = blip(f, min(0.09 * larga, paso * 1.05 * larga), who) * (0.34 if who == 'humano' else 0.2)
            k = int((a + 0.05 + i * paso) * SR); out[k:k + len(s)] += s[:len(out) - k]
    if G.get('sfx', True):      # efectos suaves: whoosh en cada cambio de plano, pop cuando cambia la pantalla del monitor
        rs = np.random.RandomState(3); prev = None
        def pon(s, t0):
            k = int(max(0, t0) * SR); out[k:k + len(s)] += s[:max(0, len(out) - k)]
        for L_ in G['lineas']:
            if prev is not None and L_['plano'] != prev:
                n_ = int(SR * 0.28); tt = np.linspace(0, 1, n_); ruido = rs.randn(n_); w_ = 14
                ruido = np.convolve(ruido, np.ones(w_) / w_, mode='same'); pon(ruido * np.sin(np.pi * tt) ** 2 * 0.22, L_['inicio'] - 0.06)
            if L_.get('pantalla'):
                n_ = int(SR * 0.09); tt = np.arange(n_) / SR; fr = 900 - 6000 * tt
                pon(np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-tt * 40) * 0.2, L_['inicio'] + 0.02)
            prev = L_['plano']
    t = np.arange(len(out)) / SR; pad = np.zeros_like(out)
    acordes = [(220.0, 261.6, 329.6), (174.6, 220.0, 261.6), (261.6, 329.6, 392.0), (196.0, 246.9, 293.7)]
    seg = dur / 4
    for ci, ch in enumerate(acordes):
        a, b = ci * seg, (ci + 1) * seg + 0.6; m = (t >= a) & (t < b); tt = t[m] - a
        env = np.minimum(1, tt / 0.8) * np.minimum(1, (b - a - tt) / 0.8)
        for f in ch: pad[m] += 0.018 * np.sin(2 * np.pi * f * tt) * env
        pad[m] += np.sin(2 * np.pi * ch[2] * 2 * tt) * np.exp(-tt * 2.2) * 0.02
    out += pad; fd = int(0.05 * SR); out[:fd] *= np.linspace(0, 1, fd); out[-fd:] *= np.linspace(1, 0, fd)
    out = np.tanh(out * 1.6) * 0.8
    with wave.open(ruta, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out * 32767).astype(np.int16).tobytes())

# ---------------------------------------------------------------- montaje
def montar(guion, salida, solo=None):
    G = json.load(open(guion)); fps = G.get('fps_animacion', 6); usar_ambiente(G.get('ambiente', 'noche_trading'))
    N = int(round(G['duracion'] * fps)) if solo is None else solo
    tmp = os.path.join(os.path.dirname(os.path.abspath(salida)), '_frames_' + os.path.basename(salida).rsplit('.', 1)[0])
    os.makedirs(tmp, exist_ok=True)
    fuente = ImageFont.truetype(FONT, 44)
    L = sorted(G['lineas'], key=lambda x: x['inicio'])
    cambios = sorted([(x['inicio'], x['pantalla']) for x in L if 'pantalla' in x] + [(c['t'], c['pantalla']) for c in G.get('cambios_pantalla', [])], key=lambda c: c[0])
    estado = dict(plano=None, emo='neutral', pantalla=G.get('pantalla_inicial', 'vacia'))
    for i in range(N):
        t = i / fps
        act = next((x for x in L if x['inicio'] <= t < x['fin']), None)
        t0, dur_p = 0.0, 4.0
        for j, (tc, p_) in enumerate(cambios):
            if tc <= t:
                estado['pantalla'] = p_; t0 = tc
                dur_p = (p_.get('duracion') if isinstance(p_, dict) and p_.get('duracion') else
                         ((cambios[j + 1][0] - tc) if j + 1 < len(cambios) else max(1.0, G['duracion'] - tc)))
        prog = max(0.0, min(1.0, (t - t0) / dur_p)) if cambios else 1.0
        if act:
            estado['plano'] = act.get('plano') or ('humano' if act['quien'] == 'humano' else 'claude')
            if act['quien'] == 'humano': estado['emo'] = act.get('emocion', estado['emo']); estado['pose'] = act.get('pose', estado.get('pose', 'type'))
        plano = estado['plano'] or ('humano' if not L else ('humano' if L[0]['quien'] == 'humano' else 'claude'))
        if plano == 'pantalla_completa':
            zoom = (act or {}).get('zoom'); nom_ = estado['pantalla']['tipo'] if isinstance(estado['pantalla'], dict) else estado['pantalla']
            if zoom is None: zoom = ZOOM_AUTO.get(nom_)          # zoom automatico (pon "zoom": false en la linea para ver la pantalla entera)
            if zoom is False: zoom = None
            lienzo = pantalla_completa(estado['pantalla'], prog, zoom); info = dict(humano={}, claude={}, sombra={})
        else:
            info = MF['planos'][plano]; lienzo = fondo_con_pantalla(plano, estado['pantalla'], prog).copy()
        habla_h = bool(act and act['quien'] == 'humano'); habla_c = bool(act and act['quien'] == 'claude')
        for _q, _f in info.get('sombra', {}).items():          # sombras FIJAS: el escenario no se mueve con los personajes
            lienzo = Image.alpha_composite(lienzo, sombra_capa(plano, _f))
        if info['humano']:
            boca = CICLO_BOCA[(i - int(act['inicio'] * fps)) % len(CICLO_BOCA)] if habla_h else 'cerrada'
            pose = estado.get('pose', 'type'); emo = estado['emo']
            cands = ([f'{pose}:{emo}_{boca}', f'{pose}:neutral_{boca}'] if pose != 'type' else []) + [f'{emo}_{boca}', f'neutral_{boca}', 'neutral_cerrada']
            clave = next(c for c in cands if c in info['humano'])
            if i % 14 == 6 and pose == 'type' and emo == 'neutral' and not habla_h and 'neutral_parpadeo' in info['humano']: clave = 'neutral_parpadeo'
            lienzo = Image.alpha_composite(lienzo, cargar(plano, info['humano'][clave]))
        if info['claude']:
            est = (act or {}).get('claude_estado', 'idle') if habla_c else estado.get('claude_estado', 'idle')
            if habla_c: estado['claude_estado'] = est
            if i % 14 == 9 and est == 'idle' and 'parpadeo' in info['claude']: est = 'parpadeo'
            capa = cargar(plano, info['claude'].get(est) or info['claude']['idle'])
            if habla_c and i % 2 == 0: capa = desplazar(capa, -14)       # botecitos al hablar (sin boca)
            lienzo = Image.alpha_composite(lienzo, capa)
        if act and act.get('empuje'):        # empuje de camara opcional (zoom lento hacia dentro durante la linea)
            k = (t - act['inicio']) / max(0.1, act['fin'] - act['inicio']); s = 1 + 0.08 * k
            cw, ch = int(W / s), int(H / s); x0, y0 = (W - cw) // 2, int((H - ch) * 0.4)
            lienzo = lienzo.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.LANCZOS)
        im = lienzo.convert('RGB').resize((1080, 1920), Image.LANCZOS)
        if act and act.get('texto') and G.get('subtitulos', True):
            d = ImageDraw.Draw(im); y = 1500
            for ln in act['texto'].split('\n'):
                w = d.textlength(ln, font=fuente)
                d.text(((1080 - w) / 2, y), ln, font=fuente, fill=COL[act['quien']], stroke_width=6, stroke_fill=(10, 8, 20)); y += 62
        im.save(f'{tmp}/f_{i:04d}.png')
    wav = os.path.join(tmp, 'voz.wav'); generar_audio(G, wav)
    dur = N / fps
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(fps), '-i', f'{tmp}/f_%04d.png', '-i', wav,
                    '-vf', 'fps=24,format=yuv420p', '-af', f'afade=t=out:st={max(0, dur - 0.4)}:d=0.4', '-c:v', 'libx264', '-crf', '18',
                    '-c:a', 'aac', '-b:a', '160k', '-t', str(dur), '-movflags', '+faststart', salida], check=True)
    for f in glob.glob(f'{tmp}/*'): os.remove(f)
    os.rmdir(tmp); print('VIDEO OK', salida, f'({N} frames de animacion, {dur:.1f}s)')

if __name__ == '__main__':
    g, s, n = args(); montar(g, s, n)
