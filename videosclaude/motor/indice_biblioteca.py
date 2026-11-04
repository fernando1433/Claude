"""Genera biblioteca/INDICE.md y una hoja de contacto por plano (biblioteca/<plano>/_contacto.png) para reconocer rapido cada capa.
Uso: python3 -I motor/indice_biblioteca.py"""
import os, json
from PIL import Image, ImageDraw, ImageFont
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); BIB = os.path.join(RAIZ, 'biblioteca')
MF = json.load(open(os.path.join(BIB, 'manifest.json'))); W, H = MF['tamano']
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
md = ['# Indice de la biblioteca de capas\n', f'Tamano de cada capa: {W}x{H} (vertical). Todas las capas de un plano comparten camara: se apilan en este orden: '
      '**fondo -> pantalla del monitor (opcional) -> humano -> claude**.\n']
for plano, info in MF['planos'].items():
    md.append(f"\n## Plano `{plano}` - {info['descripcion']}\n")
    md.append(f"- Fondo: `{plano}/{info['fondo']}` (habitacion sin personajes, monitor con pantalla `vacia`).")
    md.append(f"- Cuadrilatero del monitor (px, TL,TR,BR,BL): `{info['pantalla_quad']}`")
    if info['humano']:
        md.append('- Capas del humano (RGBA, fondo transparente + sombra): ' + ', '.join(f'`{v}`' for v in info['humano'].values()))
    if info['claude']:
        md.append('- Capas de Clawd (RGBA): ' + ', '.join(f'`{v}`' for v in info['claude'].values()))
    # hoja de contacto
    capas = [('fondo', info['fondo'])] + [(f'h:{k}', v) for k, v in info['humano'].items()] + [(f'c:{k}', v) for k, v in info['claude'].items()]
    fondo = Image.open(os.path.join(BIB, plano, info['fondo'])).convert('RGBA'); tw, th = W // 3, H // 3
    cols = min(6, len(capas)); filas = -(-len(capas) // cols); hoja = Image.new('RGB', (cols * tw, filas * th))
    for i, (nombre, f) in enumerate(capas):
        p = os.path.join(BIB, plano, f)
        if not os.path.exists(p): continue
        im = Image.open(p).convert('RGBA'); im = im if nombre == 'fondo' else Image.alpha_composite(fondo, im)
        im = im.convert('RGB').resize((tw, th)); ImageDraw.Draw(im).text((4, 4), nombre, font=F, fill=(255, 255, 0), stroke_width=2, stroke_fill=(0, 0, 0))
        hoja.paste(im, ((i % cols) * tw, (i // cols) * th))
    hoja.save(os.path.join(BIB, plano, '_contacto.png'))
    md.append(f'- Vista rapida de todas las capas: `{plano}/_contacto.png`')
md.append('\n## Pantallas del monitor (`biblioteca/pantallas/`, 1280x720)\n- `vacia` (por defecto, neutra) y ejemplos de trading: `chart`, `chat`, `order`. Se pueden anadir mas: cualquier PNG 1280x720.')
open(os.path.join(BIB, 'INDICE.md'), 'w').write('\n'.join(md) + '\n'); print('INDICE ok')
