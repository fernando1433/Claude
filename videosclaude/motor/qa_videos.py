"""Control de calidad de los videos montados + tiras de vista previa para la documentacion.
Comprueba: existe el mp4, duracion = la del guion (+-0.2 s), tiene audio, los fotogramas no estan vacios/negros.
Genera docs/videos/img/<id>.jpg (tira de 6 fotogramas), salidas/portadas/<id>.jpg (portada 1080x1920 con el titulo) y docs/QA.md. Uso: python3 -I motor/qa_videos.py"""
import os, sys, json, glob, subprocess
import numpy as np
from PIL import Image
from PIL import ImageDraw, ImageFont
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
IMG = f'{RAIZ}/docs/videos/img'; os.makedirs(IMG, exist_ok=True); tmp = '/tmp/_qa_frames'; os.makedirs(tmp, exist_ok=True)

def portada(vid, titulo, mp4):
    """portada 1080x1920: un fotograma del gancho (t=0.7 s) con el titulo en grande arriba"""
    os.makedirs(f'{RAIZ}/salidas/portadas', exist_ok=True); p = f'{tmp}/{vid}_cover.png'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '0.7', '-i', mp4, '-frames:v', '1', p], check=True)
    im = Image.open(p).convert('RGB'); d = ImageDraw.Draw(im, 'RGBA'); f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 78)
    lin, ln = [], ''
    for w_ in titulo.split(' '):
        if d.textlength((ln + ' ' + w_).strip(), font=f) > 940 and ln: lin.append(ln); ln = w_
        else: ln = (ln + ' ' + w_).strip()
    lin.append(ln); alto = len(lin) * 96 + 60; d.rectangle((0, 110, 1080, 110 + alto), fill=(10, 8, 24, 190)); y = 140
    for l in lin: d.text((540, y), l, font=f, fill=(255, 235, 200), anchor='ma', stroke_width=6, stroke_fill=(10, 8, 20)); y += 96
    im.save(f'{RAIZ}/salidas/portadas/{vid}.jpg', quality=88)
filas = []; malos = 0
for f in sorted(glob.glob(f'{RAIZ}/guiones/*.json')):
    vid = os.path.basename(f)[:-5]
    if vid.startswith('ejemplo_'): continue
    G = json.load(open(f)); mp4 = f'{RAIZ}/salidas/{vid}.mp4'; prob = []
    if not os.path.exists(mp4): filas.append((vid, G['duracion'], '-', 'FALTA'));  malos += 1; continue
    try:
        info = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_type', '-of', 'json', mp4]))
        dur = float(info['format']['duration']); tipos = [s['codec_type'] for s in info['streams']]
        if abs(dur - G['duracion']) > 0.25: prob.append(f'duracion {dur:.1f} s (guion {G["duracion"]})')
        if 'audio' not in tipos: prob.append('sin audio')
        ims = []
        for i in range(6):
            t = dur * (i + 0.5) / 6; p = f'{tmp}/{vid}_{i}.png'
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{t:.2f}', '-i', mp4, '-frames:v', '1', '-vf', 'scale=270:480', p], check=True); ims.append(Image.open(p).convert('RGB'))
        if min(np.array(im).mean() for im in ims) < 12: prob.append('fotograma casi negro')
        tira = Image.new('RGB', (270 * 6, 480)); [tira.paste(im, (k * 270, 0)) for k, im in enumerate(ims)]; tira.save(f'{IMG}/{vid}.jpg', quality=82); portada(vid, G['titulo'], mp4)
    except Exception as e: prob.append(f'error: {e}')
    filas.append((vid, G['duracion'], f'{dur:.1f}' if not prob or 'error' not in prob[-1] else '-', 'OK' if not prob else '; '.join(prob))); malos += bool(prob)
md = ['# Control de calidad de los vídeos', '', f'{len(filas)} vídeos revisados · {malos} con problemas.', '', '| Vídeo | Guion (s) | Real (s) | Estado |', '|---|---|---|---|']
md += [f'| `{v}` | {d} | {r} | {e} |' for v, d, r, e in filas]
open(f'{RAIZ}/docs/QA.md', 'w').write('\n'.join(md) + '\n'); print(f'{len(filas)} revisados, {malos} con problemas')
for v, d, r, e in filas:
    if e != 'OK': print(' ', v, e)
