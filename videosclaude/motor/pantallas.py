"""PANTALLAS ANIMADAS del monitor (1280x720). Se dibujan con PIL al montar el video: NO hace falta Blender ni renderizar nada.

    from pantallas import dibujar, PANTALLAS
    img = dibujar('dashboard', p=0.6, datos={...})   # p = progreso 0..1 de la animacion (numeros que suben, texto que se teclea...)

Pantallas (tema: Claude llevandote el negocio online / la vida entera). Genericas, sin marcas reales:
  chat       Claude en terminal: teclea lo que va haciendo
  dashboard  ingresos del dia que suben + grafica + KPIs
  tienda     pedidos que entran uno a uno + aviso de "nuevo pedido"
  calendario semana con reuniones/tareas que aparecen
  email      bandeja de entrada + Claude redacta y envia una respuesta
  analitica  visitas/seguidores creciendo + top contenidos
  tareas     lista de tareas que se van marcando + barra de progreso
  hoja       hoja de calculo que se rellena y suma el total
  trading    velas que se forman + P&L en vivo (datos: tendencia sube|cae)
  cartera    cartera destrozada con posiciones graciosas (humor)
  orden      ticket de orden: el stop loss vacio se rellena
  resultado  stop ejecutado: perdida con stop vs sin stop
Cada una admite `datos` para cambiar textos/cifras (ver DEFECTOS de cada funcion).
"""
from PIL import Image, ImageDraw, ImageFont
from functools import lru_cache
import math, random

W, H = 1280, 720
BG = (13, 15, 30); PANEL = (22, 25, 46); LINE = (45, 50, 85); TXT = (222, 226, 242); DIM = (120, 128, 162)
OR = (240, 125, 85); GR = (60, 230, 150); RD = (255, 85, 100); CY = (110, 215, 235); PU = (170, 125, 255); YE = (255, 200, 85)
_DIR = '/usr/share/fonts/truetype/dejavu/'

@lru_cache(None)
def F(size, bold=False, mono=False):
    return ImageFont.truetype(_DIR + ('DejaVuSansMono' if mono else 'DejaVuSans') + ('-Bold' if bold else '') + '.ttf', size)

def ease(x): x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)
def tramo(p, a, b): return ease((p - a) / (b - a)) if b > a else float(p >= a)   # progreso local entre a y b
def fmt(v, dec=0, pre='', suf=''):
    s = f'{v:,.{dec}f}'.replace(',', 'X').replace('.', ',').replace('X', '.'); return f'{pre}{s}{suf}'
def rr(d, box, fill, r=14, outline=None, w=2): d.rounded_rectangle(box, r, fill=fill, outline=outline, width=w)
def mezcla(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

@lru_cache(None)
def _fondo():
    im = Image.new('RGB', (W, H)); d = ImageDraw.Draw(im)
    for y in range(H):
        c = int(8 + 20 * y / H); d.line([(0, y), (W, y)], fill=(c, c + 2, c + 18))
    return im

def base(titulo, dock=True):
    im = _fondo().copy(); d = ImageDraw.Draw(im, 'RGBA')
    d.rectangle((0, 0, W, 38), fill=(10, 11, 22))
    for i, c in enumerate(((255, 95, 90), (255, 190, 60), (60, 210, 110))): d.ellipse((16 + i * 26, 12, 30 + i * 26, 26), fill=c)
    d.text((W // 2, 19), titulo, font=F(18, True), fill=DIM, anchor='mm')
    d.text((W - 24, 19), '09:41  ▮▮▮  WiFi', font=F(16), fill=DIM, anchor='rm')
    if dock:
        rr(d, (W // 2 - 270, H - 62, W // 2 + 270, H - 10), (25, 28, 52, 235), 20, LINE)
        for i, c in enumerate((OR, CY, GR, PU, YE, RD, (120, 160, 255))):
            rr(d, (W // 2 - 246 + i * 74, H - 54, W // 2 - 246 + i * 74 + 46, H - 18), c, 10)
    return im, d

def tarjeta(d, box, titulo=None):
    rr(d, box, PANEL, 16, LINE)
    if titulo: d.text((box[0] + 20, box[1] + 16), titulo, font=F(17, True), fill=DIM)

def grafica(im, box, serie, p, color=GR, relleno=True, grosor=4):
    """linea que se dibuja de izquierda a derecha segun p (0..1)"""
    x0, y0, x1, y1 = box; n = len(serie); mn, mx = min(serie), max(serie)
    d = ImageDraw.Draw(im, 'RGBA')
    for k in range(1, 4): d.line([(x0, y0 + (y1 - y0) * k / 4), (x1, y0 + (y1 - y0) * k / 4)], fill=(255, 255, 255, 18), width=1)
    hasta = max(2, int(p * (n - 1)) + 1)
    pts = [(x0 + (x1 - x0) * i / (n - 1), y1 - (serie[i] - mn) / (mx - mn + 1e-9) * (y1 - y0 - 10) - 5) for i in range(min(hasta, n))]
    if len(pts) < 2: return
    if relleno:
        ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
        od.polygon(pts + [(pts[-1][0], y1), (pts[0][0], y1)], fill=(*color, 50)); im.paste(ov, (0, 0), ov)
    d = ImageDraw.Draw(im); d.line(pts, fill=color, width=grosor, joint='curve')
    x, y = pts[-1]; d.ellipse((x - 7, y - 7, x + 7, y + 7), fill=color, outline=(255, 255, 255), width=2)

def serie_creciente(n, seed, ruido=0.08, caida=None):
    r = random.Random(seed); v = 0.15; out = []
    for i in range(n):
        v += 0.85 / n + r.uniform(-ruido, ruido) * 0.5
        if caida and i == caida: v -= 0.12
        out.append(max(0.02, v))
    return out

def chip(d, xy, texto, color, fs=15):
    x, y = xy; w = d.textlength(texto, font=F(fs, True)) + 22
    rr(d, (x, y, x + w, y + fs + 14), mezcla(PANEL, color, 0.28), 10, color, 1)
    d.text((x + 11, y + 7), texto, font=F(fs, True), fill=color); return w

# ====================================================================================================== pantallas
def p_chat(p, datos):
    lineas = datos.get('lineas') or [
        (TXT, '> Claude, llévame el negocio esta semana'), (DIM, ''), (CY, '● Revisando pedidos, correos y anuncios…'),
        (GR, '  ✔ 14 pedidos nuevos procesados'), (GR, '  ✔ 9 correos respondidos'), (GR, '  ✔ Campaña ajustada (ROAS 3,4)'),
        (GR, '  ✔ Facturas del mes enviadas'), (DIM, ''), (OR, '● Listo. ¿Algo más?')]
    im, d = base(datos.get('titulo', 'claude — ~/mi-negocio'))
    rr(d, (40, 60, W - 40, 650), (16, 18, 34), 16, LINE)
    total = sum(len(t) for _, t in lineas); n = int(ease(p / 0.9) * total); y = 84
    for col, t in lineas:
        vis = t[:max(0, n)]; n -= len(t)
        d.text((68, y), vis, font=F(27, True, True), fill=col)
        if 0 <= n + len(t) - len(vis) and len(vis) < len(t) or (n < 0 and vis):
            pass
        y += 50
        if n < 0: break
    if int(p * 14) % 2 == 0 or p > 0.97: d.rectangle((68 + d.textlength(vis, font=F(27, True, True)) + 4, y - 50 + 4, 68 + d.textlength(vis, font=F(27, True, True)) + 20, y - 50 + 36), fill=OR)
    return im

def p_dashboard(p, datos):
    v = datos.get('ingresos', 12480); ped = datos.get('pedidos', 87); vis = datos.get('visitas', 3420); conv = datos.get('conversion', 2.5)
    im, d = base(datos.get('titulo', 'Panel del negocio — hoy'))
    tarjeta(d, (40, 64, 830, 420), 'INGRESOS HOY')
    a = ease(p / 0.85)
    d.text((70, 100), fmt(v * a, 0, '', ' €'), font=F(78, True), fill=TXT)
    chip(d, (72, 205), f'▲ +{int(23 * a)}% vs ayer', GR)
    grafica(im, (70, 262, 800, 400), serie_creciente(40, 3, 0.1, 22), p / 0.9)
    d = ImageDraw.Draw(im)
    for i, (t, val, suf, col) in enumerate((('PEDIDOS', ped, '', CY), ('VISITAS', vis, '', PU), ('CONVERSIÓN', conv, ' %', YE))):
        y = 64 + i * 122; tarjeta(d, (860, y, W - 40, y + 108), t)
        txt = fmt(val * a, 1 if i == 2 else 0, '', suf); d.text((884, y + 44), txt, font=F(44, True), fill=col)
    tarjeta(d, (40, 440, 830, 650), 'ÚLTIMOS 7 DÍAS')
    vals = datos.get('semana', [0.45, 0.6, 0.5, 0.72, 0.65, 0.85, 1.0])
    for i, vv in enumerate(vals):
        h = 130 * vv * tramo(p, 0.05 + i * 0.07, 0.35 + i * 0.07); x = 80 + i * 105
        rr(d, (x, 630 - h, x + 62, 630), OR if i == 6 else (60, 66, 110), 8)
        d.text((x + 31, 636), 'LMXJVSD'[i], font=F(14, True), fill=DIM, anchor='ma')
    tarjeta(d, (860, 430, W - 40, 650), 'CLAUDE HA HECHO HOY')
    for i, t in enumerate(('Anuncios optimizados', 'Pedidos enviados', 'Clientes atendidos')):
        k = tramo(p, 0.3 + i * 0.18, 0.45 + i * 0.18)
        d.text((884, 478 + i * 50), ('✔ ' if k > 0.99 else '… ') + t, font=F(20, True), fill=GR if k > 0.99 else DIM)
    return im

def p_tienda(p, datos):
    filas = datos.get('pedidos') or [('#4821', 'María G.', 'Camiseta oversize', '39,90 €'), ('#4822', 'Carlos R.', 'Pack 3 sudaderas', '119,00 €'),
            ('#4823', 'Lucía M.', 'Gorra bordada', '24,50 €'), ('#4824', 'Pablo S.', 'Camiseta + gorra', '59,90 €'),
            ('#4825', 'Ana T.', 'Sudadera negra', '44,90 €'), ('#4826', 'Jorge L.', 'Camiseta oversize', '39,90 €')]
    im, d = base(datos.get('titulo', 'Tienda — pedidos'))
    tarjeta(d, (40, 64, 830, 650))
    d.text((70, 84), 'PEDIDOS DE HOY', font=F(20, True), fill=DIM)
    n = int(len(filas) * ease(p / 0.9) + 0.0001)
    d.text((780, 78), f'{n}', font=F(44, True), fill=OR, anchor='ra')
    for i, (num, cli, prod, imp) in enumerate(filas):
        y = 142 + i * 82; k = tramo(p, i * 0.14, i * 0.14 + 0.1)
        if k <= 0: continue
        off = int((1 - k) * 60)
        rr(d, (64 + off, y, 806 + off, y + 70), (28, 32, 58), 12, LINE)
        d.text((86 + off, y + 14), num, font=F(20, True, True), fill=CY); d.text((86 + off, y + 40), cli, font=F(16), fill=DIM)
        d.text((230 + off, y + 24), prod, font=F(21, True), fill=TXT); d.text((660 + off, y + 24), imp, font=F(22, True), fill=GR, anchor='ra')
        chip(d, (680 + off, y + 18), 'Enviado' if i < n - 1 else 'Nuevo', GR if i < n - 1 else OR, 14)
    tarjeta(d, (860, 64, W - 40, 330), 'VENTAS')
    tot = sum(float(f[3].replace(' €', '').replace('.', '').replace(',', '.')) for f in filas[:n])
    d.text((884, 120), fmt(tot, 2, '', ' €'), font=F(46, True), fill=TXT)
    grafica(im, (884, 200, W - 64, 310), serie_creciente(20, 8), p / 0.9, OR)
    d = ImageDraw.Draw(im)
    tarjeta(d, (860, 350, W - 40, 650), 'INVENTARIO')
    for i, (nom, st) in enumerate((('Camiseta oversize', 0.72), ('Sudadera negra', 0.4), ('Gorra bordada', 0.15))):
        y = 400 + i * 78; d.text((884, y), nom, font=F(18, True), fill=TXT)
        rr(d, (884, y + 32, W - 64, y + 46), (40, 44, 78), 7); rr(d, (884, y + 32, 884 + (W - 64 - 884) * st * ease(p / 0.8), y + 46), RD if st < 0.2 else CY, 7)
    # aviso de pedido nuevo
    if 0.1 < p < 0.95 and int(p * 20) % 6 < 3:
        rr(d, (880, 20 + 0, W - 60, 20 + 0), PANEL, 0)
    return im

def p_calendario(p, datos):
    ev = datos.get('eventos') or [(0, 9, 2, 'Llamada proveedor', CY), (1, 10, 1, 'Grabar vídeo', OR), (2, 9, 3, 'Reunión equipo', PU), (2, 14, 2, 'Entrega pedidos', GR),
                                   (3, 11, 2, 'Anuncios', YE), (4, 9, 2, 'Publicar newsletter', OR), (1, 15, 2, 'Facturación', CY), (3, 15, 1, 'Cliente VIP', RD)]
    im, d = base(datos.get('titulo', 'Agenda — esta semana'))
    tarjeta(d, (40, 64, W - 40, 650))
    dias = ['LUN', 'MAR', 'MIÉ', 'JUE', 'VIE']; x0, y0, cw, rh = 150, 150, 220, 52
    for i, dn in enumerate(dias): d.text((x0 + i * cw + cw // 2, 112), dn, font=F(20, True), fill=OR if i == 2 else DIM, anchor='mm')
    for r in range(9):
        y = y0 + r * rh; d.line([(x0, y), (W - 60, y)], fill=(255, 255, 255, 20) if False else (40, 44, 78))
        d.text((120, y + 6), f'{9 + r}:00', font=F(15), fill=DIM, anchor='ra')
    for i in range(1, 5): d.line([(x0 + i * cw, y0), (x0 + i * cw, y0 + 9 * rh)], fill=(40, 44, 78))
    for k, (dia, h, dur, t, col) in enumerate(ev):
        a = tramo(p, 0.05 + k * 0.1, 0.18 + k * 0.1)
        if a <= 0: continue
        x = x0 + dia * cw + 6; y = y0 + (h - 9) * rh + 4; hh = dur * rh - 8
        rr(d, (x, y + (1 - a) * 20, x + cw - 12, y + (1 - a) * 20 + hh * a), mezcla(PANEL, col, 0.55), 10, col, 2)
        if a > 0.8: d.text((x + 12, y + 10), t, font=F(16, True), fill=(255, 255, 255))
    if p > 0.85: rr(d, (W - 440, 70, W - 56, 118), (60, 35, 25), 12, OR); d.text((W - 248, 94), '✔ Claude lo ha organizado', font=F(18, True), fill=OR, anchor='mm')
    return im

def p_email(p, datos):
    mails = datos.get('correos') or [('Laura P.', 'Duda sobre mi pedido', 'Hola, ¿cuándo llegará…'), ('Proveedor', 'Nueva tarifa 2025', 'Adjunto las nuevas…'),
                                      ('Marcos D.', 'Colaboración', 'Me encanta tu marca…'), ('Banco', 'Resumen mensual', 'Tu extracto está…'), ('Elena V.', 'Devolución', 'Quería devolver…')]
    resp = datos.get('respuesta', 'Hola Laura, tu pedido sale hoy y llegará en 48 h. Te paso el seguimiento en cuanto lo tenga. ¡Gracias por tu paciencia!')
    im, d = base(datos.get('titulo', 'Correo — bandeja de entrada'))
    tarjeta(d, (40, 64, 470, 650), 'BANDEJA')
    for i, (de, asu, pre) in enumerate(mails):
        y = 108 + i * 108; sel = i == 0; hecho = p > 0.25 + i * 0.12 and i > 0
        rr(d, (56, y, 454, y + 96), (38, 42, 80) if sel else (26, 29, 52), 12, OR if sel else LINE)
        d.text((76, y + 12), de, font=F(18, True), fill=TXT); d.text((76, y + 40), asu, font=F(16, True), fill=CY if not hecho else DIM)
        d.text((76, y + 66), pre, font=F(14), fill=DIM)
        if hecho: d.text((440, y + 14), '✔ Respondido', font=F(13, True), fill=GR, anchor='ra')
    tarjeta(d, (490, 64, W - 40, 650))
    d.text((520, 90), mails[0][1], font=F(26, True), fill=TXT); d.text((520, 128), f'De: {mails[0][0]}  ·  hace 2 min', font=F(15), fill=DIM)
    d.text((520, 170), '“Hola, hice un pedido el lunes y todavía no ha llegado. ¿Podéis decirme algo?”', font=F(17), fill=(190, 196, 220))
    rr(d, (520, 240, W - 70, 600), (18, 20, 38), 14, OR); chip(d, (540, 256), 'Borrador de Claude', OR, 14)
    n = int(len(resp) * ease(p / 0.7)); linea = ''; y = 308; palabras = resp[:n].split(' ')
    for w_ in palabras:
        if d.textlength(linea + w_, font=F(21)) > W - 70 - 560: d.text((540, y), linea, font=F(21), fill=TXT); y += 34; linea = ''
        linea += w_ + ' '
    d.text((540, y), linea, font=F(21), fill=TXT)
    if p > 0.8: rr(d, (W - 270, 540, W - 90, 584), GR, 12); d.text((W - 180, 562), 'Enviado ✔', font=F(19, True), fill=(8, 20, 14), anchor='mm')
    return im

def p_analitica(p, datos):
    vistas = datos.get('vistas', 1840000); seg = datos.get('seguidores', 52300)
    im, d = base(datos.get('titulo', 'Analítica — últimos 28 días'))
    tarjeta(d, (40, 64, 830, 410), 'VISUALIZACIONES')
    a = ease(p / 0.85); d.text((70, 100), fmt(vistas * a), font=F(70, True), fill=TXT); chip(d, (72, 195), f'▲ +{int(312 * a)}%', GR)
    grafica(im, (70, 250, 800, 395), serie_creciente(40, 11, 0.12), p / 0.9, CY)
    d = ImageDraw.Draw(im)
    tarjeta(d, (860, 64, W - 40, 236), 'SEGUIDORES'); d.text((884, 112), fmt(seg * a), font=F(52, True), fill=OR)
    tarjeta(d, (860, 256, W - 40, 410), 'TIEMPO DE VISIONADO'); d.text((884, 304), fmt(4.8 * a, 1, '', ' h'), font=F(46, True), fill=PU)
    tarjeta(d, (40, 430, W - 40, 650), 'CONTENIDO QUE MÁS CRECE')
    top = datos.get('top') or [('Cómo Claude lleva mi tienda', 0.95, GR), ('3 tareas que ya no hago', 0.78, CY), ('Mi día con IA', 0.6, OR), ('Automatizar correos', 0.42, PU)]
    for i, (t, v, col) in enumerate(top):
        y = 480 + i * 42; d.text((70, y), t, font=F(18, True), fill=TXT)
        rr(d, (500, y + 4, 1220, y + 24), (40, 44, 78), 8); rr(d, (500, y + 4, 500 + 720 * v * tramo(p, 0.1 + i * 0.1, 0.5 + i * 0.1), y + 24), col, 8)
    return im

def p_tareas(p, datos):
    tareas = datos.get('tareas') or ['Responder 14 correos', 'Publicar 3 vídeos', 'Actualizar precios de la tienda', 'Enviar facturas del mes',
                                      'Revisar anuncios', 'Preparar pedidos de hoy', 'Contestar mensajes de clientes']
    im, d = base(datos.get('titulo', 'Tareas — hoy'))
    tarjeta(d, (40, 64, 830, 650)); d.text((70, 84), 'HOY', font=F(20, True), fill=DIM)
    n = len(tareas)
    for i, t in enumerate(tareas):
        y = 130 + i * 72; hecho = tramo(p, 0.05 + i * 0.12, 0.12 + i * 0.12)
        rr(d, (66, y, 804, y + 60), (28, 32, 58), 12, LINE)
        rr(d, (86, y + 16, 114, y + 44), GR if hecho > 0.5 else (20, 22, 40), 8, GR if hecho > 0.5 else DIM, 2)
        if hecho > 0.5: d.line([(92, y + 31), (99, y + 38), (110, y + 22)], fill=(8, 20, 14), width=4)
        d.text((136, y + 16), t, font=F(23, True), fill=DIM if hecho > 0.5 else TXT)
        if hecho > 0.5: d.line([(136, y + 30), (136 + d.textlength(t, font=F(23, True)), y + 30)], fill=DIM, width=2)
    hechas = sum(1 for i in range(n) if tramo(p, 0.05 + i * 0.12, 0.12 + i * 0.12) > 0.5)
    tarjeta(d, (860, 64, W - 40, 330), 'PROGRESO'); d.text((884, 118), f'{int(100 * hechas / n)} %', font=F(76, True), fill=GR if hechas == n else OR)
    rr(d, (884, 240, W - 64, 262), (40, 44, 78), 11); rr(d, (884, 240, 884 + (W - 64 - 884) * hechas / n, 262), GR if hechas == n else OR, 11)
    tarjeta(d, (860, 350, W - 40, 650), 'CLAUDE SE ENCARGA');
    for i, t in enumerate(('Tareas repetitivas', 'Correos y mensajes', 'Facturas y pedidos', 'Tu agenda')): d.text((884, 404 + i * 56), '● ' + t, font=F(20, True), fill=CY)
    return im

def p_hoja(p, datos):
    im, d = base(datos.get('titulo', 'Hoja — ventas por producto'))
    tarjeta(d, (40, 64, W - 40, 650))
    cab = ['Producto', 'Uds.', 'Precio', 'Ingresos', 'Margen']; xs = [70, 520, 650, 800, 1000]
    filas = datos.get('filas') or [('Camiseta oversize', 412, 39.9, 0.62), ('Sudadera negra', 238, 44.9, 0.55), ('Gorra bordada', 301, 24.5, 0.68), ('Pack 3 sudaderas', 96, 119.0, 0.5),
                                   ('Camiseta + gorra', 187, 59.9, 0.6)]
    rr(d, (60, 90, W - 60, 134), (38, 42, 80), 8)
    for x, c in zip(xs, cab): d.text((x + 10, 100), c, font=F(19, True), fill=OR)
    tot = 0
    for i, (n_, u, pr, m) in enumerate(filas):
        y = 140 + i * 66; k = tramo(p, 0.05 + i * 0.12, 0.18 + i * 0.12); ing = u * pr; tot += ing * (1 if k > 0.99 else 0)
        d.line([(60, y + 60), (W - 60, y + 60)], fill=(40, 44, 78))
        if k <= 0: continue
        d.text((xs[0] + 10, y + 14), n_, font=F(21, True), fill=TXT)
        d.text((xs[1] + 10, y + 14), fmt(u * k), font=F(21, mono=True), fill=TXT); d.text((xs[2] + 10, y + 14), fmt(pr, 2, '', ' €'), font=F(21, mono=True), fill=DIM)
        d.text((xs[3] + 10, y + 14), fmt(ing * k, 0, '', ' €'), font=F(21, True, True), fill=GR); d.text((xs[4] + 10, y + 14), f'{int(m * 100 * k)} %', font=F(21, True), fill=CY if m > 0.58 else YE)
    rr(d, (60, 500, W - 60, 570), (50, 38, 36) if p > 0.85 else (30, 33, 60), 12, OR, 2)
    d.text((80, 520), 'TOTAL', font=F(26, True), fill=OR); d.text((W - 90, 516), fmt(sum(u * pr for _, u, pr, _ in filas) * ease(p / 0.9), 0, '', ' €'), font=F(36, True), fill=TXT, anchor='ra')
    if p > 0.9: d.text((80, 596), '✔ Claude ha actualizado la hoja y calculado márgenes', font=F(20, True), fill=GR)
    return im


# ====================================================================================================== TRADING (humor)
def _velas(im, box, p, tendencia='sube', n=30, seed=4):
    d = ImageDraw.Draw(im); x0, y0, x1, y1 = box; rr(d, box, PANEL, 14, LINE)
    for k in range(1, 5): d.line([(x0 + 8, y0 + (y1 - y0) * k / 5), (x1 - 70, y0 + (y1 - y0) * k / 5)], fill=(35, 40, 70), width=1)
    r = random.Random(seed); pr = 0.35 if tendencia == 'sube' else 0.85; pts = []
    for i in range(n):
        dl = (0.032 if tendencia == 'sube' else -0.03) + r.uniform(-0.03, 0.03)
        if tendencia == 'sube' and i > n * 0.72: dl = -0.07 + r.uniform(-0.02, 0.02)      # el "dip" tras la subida
        o, c = pr, pr + dl; pr = c; pts.append((o, c, max(o, c) + r.uniform(0.005, 0.03), min(o, c) - r.uniform(0.005, 0.03)))
    ys = [v for q in pts for v in (q[2], q[3])]; mn, mx = min(ys), max(ys)
    Y = lambda v: y1 - 18 - (v - mn) / (mx - mn) * (y1 - y0 - 44)
    hasta = max(1, int(n * ease(p))); step = (x1 - x0 - 90) / n
    for i, (o, c, hi, lo) in enumerate(pts[:hasta]):
        x = x0 + 22 + i * step; col = GR if c >= o else RD
        d.line([(x, Y(hi)), (x, Y(lo))], fill=col, width=3); d.rectangle((x - step * 0.3, Y(max(o, c)), x + step * 0.3, Y(min(o, c)) + 2), fill=col)
    ult = pts[hasta - 1]; yy = Y(ult[1]); col = GR if ult[1] >= ult[0] else RD
    d.line([(x0 + 8, yy), (x1 - 70, yy)], fill=(255, 255, 255, 90), width=1); rr(d, (x1 - 66, yy - 13, x1 - 6, yy + 13), col, 6)
    d.text((x1 - 36, yy), 'BTC', font=F(13, True), fill=(10, 10, 20), anchor='mm')
    return ult[1] >= ult[0], hasta / n

def p_trading(p, datos):
    tend = datos.get('tendencia', 'sube'); im, d = base(datos.get('titulo', 'TradeDesk — BTC/USDT'))
    sube, prog = _velas(im, (40, 110, 900, 600), p, tend, 30, 4 if tend == 'sube' else 9)
    d = ImageDraw.Draw(im); pct = (0.06 * prog if prog < 0.72 else 0.0432 - 0.05 * (prog - 0.72) / 0.28) if tend == 'sube' else -0.09 * prog; precio = 61200 * (1 + pct)
    d.text((40, 62), 'BTC/USDT', font=F(30, True), fill=TXT); d.text((235, 64), fmt(precio, 2), font=F(32, True, True), fill=GR if sube else RD)
    chip(d, (520, 66), ('▲ ' if sube else '▼ ') + f'{abs((precio / 61200 - 1) * 100):.2f}%'.replace('.', ','), GR if sube else RD, 20)
    rr(d, (920, 110, W - 40, 600), PANEL, 14, LINE); d.text((944, 130), 'TU POSICIÓN', font=F(17, True), fill=DIM)
    d.text((944, 170), 'COMPRA 0,5 BTC', font=F(22, True), fill=TXT); d.text((944, 214), 'Entrada 61.200', font=F(18, mono=True), fill=DIM)
    pnl = (precio - 61200) * 0.5; d.text((944, 270), fmt(pnl, 0, '+' if pnl >= 0 else '', ' €'), font=F(44, True), fill=GR if pnl >= 0 else RD)
    d.text((944, 350), 'Stop loss', font=F(16), fill=DIM); chip(d, (944, 380), 'NINGUNO', RD, 16)
    d.text((944, 450), 'Convicción', font=F(16), fill=DIM); rr(d, (944, 480, W - 64, 500), (40, 44, 78), 10); rr(d, (944, 480, W - 64, 500), OR, 10)
    d.text((944, 515), '100 % (sin motivo)', font=F(15, True), fill=OR)
    return im

def p_cartera(p, datos):
    im, d = base(datos.get('titulo', 'Cartera — resumen')); tarjeta(d, (40, 64, 560, 330), 'RENDIMIENTO TOTAL')
    a = ease(p / 0.7); d.text((70, 110), f'-{43.2 * a:.1f} %'.replace('.', ','), font=F(86, True), fill=RD); d.text((72, 225), f'-{12840 * a:,.0f} €'.replace(',', '.'), font=F(34, True), fill=RD)
    chip(d, (72, 280), 'Stop loss: ninguno', RD, 17)
    grafica(im, (590, 80, W - 60, 320), [1 - 0.55 * (i / 40) ** 0.8 + 0.04 * math.sin(i * 1.7) for i in range(41)], p / 0.8, RD)
    d = ImageDraw.Draw(im); tarjeta(d, (40, 350, W - 40, 650), 'POSICIONES')
    pos = datos.get('posiciones') or [('Acción que me dijo mi primo', -62, RD), ('Memecoin con un perro', -81, RD), ('NFT de mono (2021)', -97, RD), ('Bitcoin', 4, GR), ('"Lo mantengo a largo plazo"', -38, RD)]
    pos = [(q[0], q[1], (RD if q[1] < 0 else GR)) for q in pos]
    for i, (n_, v, col) in enumerate(pos):
        k = tramo(p, 0.15 + i * 0.12, 0.3 + i * 0.12)
        if k <= 0: continue
        y = 396 + i * 48; d.text((70, y), n_, font=F(21, True), fill=TXT)
        d.text((W - 70, y), f'{int(v * k):+d} %', font=F(24, True, True), fill=col, anchor='ra')
        rr(d, (640, y + 8, 1000, y + 24), (40, 44, 78), 7); w_ = 360 * abs(v) / 100 * k
        rr(d, (640, y + 8, 640 + max(6, w_), y + 24), col, 7)
    return im

def p_orden(p, datos):
    im, d = base(datos.get('titulo', 'TradeDesk — Nueva orden')); tarjeta(d, (300, 64, 980, 650))
    rr(d, (330, 92, 640, 144), GR, 12); d.text((485, 118), 'COMPRAR', font=F(24, True), fill=(8, 20, 14), anchor='mm')
    rr(d, (650, 92, 950, 144), (40, 28, 40), 12, RD); d.text((800, 118), 'VENDER', font=F(24, True), fill=RD, anchor='mm')
    campos = [('Entrada', '61.200,00', TXT), ('Tamaño', '0,50 BTC', TXT), ('Take profit', '64.000,00', GR)]
    for i, (a, b, c) in enumerate(campos):
        y = 170 + i * 84; d.text((332, y), a, font=F(19), fill=DIM); rr(d, (332, y + 28, 948, y + 68), (14, 16, 32), 10, LINE); d.text((350, y + 48), b, font=F(25, True, True), fill=c, anchor='lm')
    y = 170 + 3 * 84; d.text((332, y), 'Stop loss', font=F(19), fill=DIM); lleno = p > 0.45
    pulso = 3 if (not lleno and int(p * 20) % 2 == 0) else 2
    rr(d, (332, y + 28, 948, y + 68), (14, 16, 32), 10, GR if lleno else RD, pulso)
    txt = '60.000,00  (-2 %)' if lleno else '— — —'; n = int(len(txt) * tramo(p, 0.45, 0.65)) if lleno else len(txt)
    d.text((350, y + 48), txt[:max(1, n)], font=F(25, True, True), fill=GR if lleno else RD, anchor='lm')
    if lleno and p > 0.7: d.text((930, y + 48), '✔', font=F(28, True), fill=GR, anchor='rm')
    btn = p > 0.85
    rr(d, (332, 540, 948, 620), GR if lleno else (60, 90, 70), 16); d.text((640, 580), 'CONFIRMAR COMPRA', font=F(30, True), fill=(8, 20, 14), anchor='mm')
    if not lleno: rr(d, (1000, 110, 1250, 220), (70, 25, 35), 14, RD); d.text((1125, 140), '⚠ Falta el stop', font=F(20, True), fill=(255, 255, 255), anchor='mm'); d.text((1125, 180), 'Riesgo sin límite', font=F(16), fill=(255, 190, 190), anchor='mm')
    return im

def p_resultado(p, datos):
    im, d = base(datos.get('titulo', 'Resultado — operación cerrada')); tarjeta(d, (40, 64, W - 40, 650))
    rr(d, (80, 96, W - 80, 160), (70, 25, 35) if p < 0.3 else (25, 60, 45), 14, RD if p < 0.3 else GR)
    d.text((W // 2, 128), '⚠ STOP LOSS EJECUTADO' if p < 0.3 else '✔ STOP LOSS EJECUTADO', font=F(30, True), fill=RD if p < 0.3 else GR, anchor='mm')
    a = ease((p - 0.15) / 0.5)
    d.text((100, 200), 'SIN STOP (tu plan)', font=F(22, True), fill=DIM); rr(d, (100, 238, 1180, 296), (40, 44, 78), 12); rr(d, (100, 238, 100 + 1080 * a, 296), RD, 12)
    d.text((1160, 267), f'-{4000 * a:,.0f} €'.replace(',', '.'), font=F(34, True, True), fill=(255, 255, 255), anchor='rm')
    b = ease((p - 0.35) / 0.4)
    d.text((100, 346), 'CON STOP (el de Claude)', font=F(22, True), fill=DIM); rr(d, (100, 384, 1180, 442), (40, 44, 78), 12); rr(d, (100, 384, 100 + max(8, 1080 * 0.01 * b), 442), GR, 12)
    d.text((1160, 413), f'-{40 * b:,.0f} €'.replace(',', '.'), font=F(34, True, True), fill=GR, anchor='rm')
    if p > 0.75: rr(d, (180, 500, W - 180, 600), (30, 33, 60), 16, OR, 2); d.text((W // 2, 550), 'Has perdido 3.960 € menos. Felicidades (?)', font=F(30, True), fill=OR, anchor='mm')
    return im


# ====================================================================================================== iconos de producto (dibujados, sin imagenes externas)
def icono(d, kind, x, y, s, fondo=None):
    """dibuja un producto sencillo (estilo plano) dentro del cuadrado (x, y, s, s)"""
    rr(d, (x, y, x + s, y + s), fondo or (40, 44, 80), int(s * 0.12))
    cx, cy, u = x + s / 2, y + s / 2, s / 100.0
    if kind == 'taza':
        rr(d, (cx - 26 * u, cy - 22 * u, cx + 20 * u, cy + 26 * u), (245, 245, 250), int(8 * u)); d.arc((cx + 8 * u, cy - 12 * u, cx + 40 * u, cy + 16 * u), 270, 90, fill=(245, 245, 250), width=int(7 * u))
        d.rectangle((cx - 26 * u, cy - 22 * u, cx + 20 * u, cy - 12 * u), fill=OR)
    elif kind == 'camiseta':
        d.polygon([(cx - 30 * u, cy - 28 * u), (cx - 12 * u, cy - 32 * u), (cx + 12 * u, cy - 32 * u), (cx + 30 * u, cy - 28 * u), (cx + 42 * u, cy - 6 * u), (cx + 28 * u, cy), (cx + 24 * u, cy - 8 * u), (cx + 24 * u, cy + 32 * u), (cx - 24 * u, cy + 32 * u), (cx - 24 * u, cy - 8 * u), (cx - 28 * u, cy), (cx - 42 * u, cy - 6 * u)], fill=(90, 190, 170))
        d.ellipse((cx - 11 * u, cy - 38 * u, cx + 11 * u, cy - 18 * u), fill=fondo or (40, 44, 80))
    elif kind == 'cactus':
        d.ellipse((cx - 40 * u, cy - 40 * u, cx + 40 * u, cy + 40 * u), fill=(70, 80, 40, 90) if False else (255, 230, 150))
        rr(d, (cx - 14 * u, cy - 26 * u, cx + 14 * u, cy + 18 * u), (60, 170, 100), int(12 * u)); rr(d, (cx - 32 * u, cy - 10 * u, cx - 14 * u, cy + 2 * u), (60, 170, 100), int(6 * u)); rr(d, (cx - 32 * u, cy - 24 * u, cx - 22 * u, cy), (60, 170, 100), int(5 * u))
        rr(d, (cx + 14 * u, cy - 14 * u, cx + 32 * u, cy - 2 * u), (60, 170, 100), int(6 * u)); rr(d, (cx + 22 * u, cy - 30 * u, cx + 32 * u, cy - 6 * u), (60, 170, 100), int(5 * u))
        d.polygon([(cx - 18 * u, cy + 18 * u), (cx + 18 * u, cy + 18 * u), (cx + 13 * u, cy + 40 * u), (cx - 13 * u, cy + 40 * u)], fill=(200, 120, 90))
    elif kind == 'soporte':
        d.polygon([(cx - 28 * u, cy + 30 * u), (cx + 28 * u, cy + 30 * u), (cx + 10 * u, cy - 6 * u), (cx - 10 * u, cy - 6 * u)], fill=(170, 125, 255)); rr(d, (cx - 14 * u, cy - 36 * u, cx + 14 * u, cy + 8 * u), (30, 32, 50), int(5 * u))
    elif kind == 'botella':
        rr(d, (cx - 14 * u, cy - 12 * u, cx + 14 * u, cy + 36 * u), CY, int(8 * u)); rr(d, (cx - 7 * u, cy - 34 * u, cx + 7 * u, cy - 10 * u), CY, int(4 * u)); rr(d, (cx - 9 * u, cy - 40 * u, cx + 9 * u, cy - 32 * u), (240, 240, 250), int(3 * u))
    elif kind == 'zapatilla':
        d.polygon([(cx - 40 * u, cy + 14 * u), (cx - 36 * u, cy - 14 * u), (cx - 10 * u, cy - 18 * u), (cx + 4 * u, cy - 4 * u), (cx + 38 * u, cy + 4 * u), (cx + 40 * u, cy + 18 * u)], fill=(255, 120, 130)); d.rectangle((cx - 42 * u, cy + 14 * u, cx + 42 * u, cy + 24 * u), fill=(240, 240, 245))
    elif kind == 'auriculares':
        d.arc((cx - 30 * u, cy - 34 * u, cx + 30 * u, cy + 26 * u), 180, 360, fill=(230, 230, 240), width=int(7 * u)); rr(d, (cx - 38 * u, cy - 6 * u, cx - 18 * u, cy + 26 * u), YE, int(6 * u)); rr(d, (cx + 18 * u, cy - 6 * u, cx + 38 * u, cy + 26 * u), YE, int(6 * u))
    elif kind == 'reloj':
        d.ellipse((cx - 28 * u, cy - 28 * u, cx + 28 * u, cy + 28 * u), fill=(235, 235, 245), outline=(120, 130, 170), width=int(5 * u)); d.line([(cx, cy), (cx, cy - 18 * u)], fill=(30, 30, 40), width=int(4 * u)); d.line([(cx, cy), (cx + 13 * u, cy + 6 * u)], fill=RD, width=int(3 * u))
    return (x, y, s, s)

PRODUCTOS = [('taza', 'Taza térmica', '24,90 €', (60, 66, 120)), ('camiseta', 'Camiseta oversize', '29,90 €', (70, 60, 110)), ('cactus', 'Lámpara cactus', '27,90 €', (50, 70, 90)),
             ('soporte', 'Soporte móvil', '14,90 €', (70, 60, 90)), ('botella', 'Botella inox', '19,90 €', (50, 74, 100)), ('zapatilla', 'Zapatillas', '49,90 €', (84, 56, 84))]

# ====================================================================================================== TRADING: curso milagro, pago, señales, apalancamiento, datos reales
def p_curso(p, datos):
    im, d = base(datos.get('titulo', 'hazte-rico-ya.com — Chrome')); rr(d, (40, 56, W - 40, 650), (24, 22, 40), 14, LINE)
    rr(d, (60, 70, W - 60, 106), (14, 15, 28), 18); d.text((86, 88), '🔒 hazte-rico-ya.com/oferta-secreta'.replace('🔒', '▪'), font=F(16, mono=True), fill=DIM, anchor='lm')
    rr(d, (60, 120, W - 60, 330), (70, 50, 12), 16); d.text((W // 2, 168), datos.get('curso', 'HAZTE MILLONARIO EN 7 DÍAS'), font=F(46, True), fill=(255, 214, 80), anchor='mm')
    d.text((W // 2, 218), 'El método secreto de un gurú de 23 años (no te lo cuentan los bancos)', font=F(21), fill=(255, 235, 190), anchor='mm')
    seg = max(0, 599 - int(ease(p) * 40)); mm, ss = divmod(seg, 60)      # contador "falso": parece avanzar
    rr(d, (400, 250, 880, 312), (30, 10, 10), 12, RD); d.text((W // 2, 281), f'⚠ La oferta termina en 00:{mm:02d}:{ss:02d}', font=F(26, True, True), fill=RD, anchor='mm')
    d.text((100, 366), '1.997 €', font=F(34, True), fill=DIM); d.line([(100, 384), (222, 384)], fill=RD, width=4); d.text((250, 358), '997 €', font=F(56, True), fill=GR)
    pulso = 1.0 + 0.04 * math.sin(p * 40); bw = int(330 * pulso)
    rr(d, (W - 80 - bw, 352, W - 80, 420), (240, 90, 60), 18); d.text((W - 80 - bw // 2, 386), '¡QUIERO SER RICO!', font=F(24, True), fill=(255, 255, 255), anchor='mm')
    for i, (n, t) in enumerate((('Carlos, 24', '"Pasé de pobre a rico"'), ('Marta, 31', '"¡Ahora tengo un Lambo!"'), ('Pablo, 28', '"Gané 40.000 € dormido"'))):
        x = 80 + i * 380; rr(d, (x, 450, x + 350, 560), (34, 32, 56), 14, LINE); d.ellipse((x + 16, 470, x + 76, 530), fill=mezcla((90, 90, 130), OR, i / 3)); d.text((x + 92, 478), n, font=F(18, True), fill=TXT); d.text((x + 92, 508), t, font=F(15), fill=YE)
    d.text((80, 590), '*Resultados no típicos. Garantizado 100 % (no preguntes cómo).', font=F(14), fill=DIM)
    # banderas rojas de Claude: aparecen una a una
    caj = [(400, 250, 880, 312, 'Contador falso: se reinicia'), (80, 450, 1210, 560, 'Testimonios de stock'), (200, 140, 1080, 240, '«Garantizado» = ilegal'), (60, 340, 700, 430, 'Precio inventado')]
    for k, (x0, y0, x1, y1, t) in enumerate(caj):
        a = tramo(p, 0.35 + k * 0.14, 0.45 + k * 0.14)
        if a <= 0: continue
        ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov); od.rounded_rectangle((x0 - 6, y0 - 6, x1 + 6, y1 + 6), 14, outline=(255, 70, 80, int(255 * a)), width=5)
        im.paste(ov, (0, 0), ov); d = ImageDraw.Draw(im); w_ = d.textlength('✖ ' + t, font=F(19, True)) + 24
        by = y0 - 40 if y0 > 130 else y1 + 10; rr(d, (x0, by, x0 + w_, by + 34), (200, 30, 50), 8); d.text((x0 + 12, by + 17), '✖ ' + t, font=F(19, True), fill=(255, 255, 255), anchor='lm')
    return im

def p_checkout(p, datos):
    im, d = base(datos.get('titulo', 'Pago seguro (¿seguro?)')); tarjeta(d, (330, 60, 950, 650)); d.text((360, 84), 'FINALIZAR COMPRA', font=F(22, True), fill=DIM)
    d.text((360, 124), datos.get('curso', 'Curso: Millonario en 7 días'), font=F(24, True), fill=TXT); d.text((920, 124), '997,00 €', font=F(28, True, True), fill=GR, anchor='ra')
    num = '4532  8821  0093  4417'; n = int(len(num) * tramo(p, 0.05, 0.5)); nom = 'TU NOMBRE (ILUSIONADO)'
    for i, (lab, txt) in enumerate((('Número de tarjeta', num[:n]), ('Titular', nom if p > 0.5 else ''), ('Caducidad / CVV', '08/28   ···' if p > 0.55 else ''))):
        y = 180 + i * 96; d.text((360, y), lab, font=F(17), fill=DIM); rr(d, (360, y + 28, 920, y + 72), (14, 16, 32), 10, LINE); d.text((380, y + 50), txt + ('▌' if int(p * 20) % 2 == 0 and i == 0 and p < 0.5 else ''), font=F(23, True, True), fill=TXT, anchor='lm')
    rr(d, (360, 490, 920, 560), (240, 90, 60), 16); d.text((640, 525), 'PAGAR 997 €', font=F(30, True), fill=(255, 255, 255), anchor='mm')
    d.text((640, 596), '¡Solo quedan 3 plazas! (siempre quedan 3 plazas)', font=F(17, True), fill=RD, anchor='mm')
    if p > 0.6:
        a = tramo(p, 0.6, 0.72); ov = Image.new('RGBA', im.size, (0, 0, 0, int(150 * a))); im.paste(ov, (0, 0), ov)
        sello = Image.new('RGBA', (760, 220), (0, 0, 0, 0)); sd = ImageDraw.Draw(sello); sd.rounded_rectangle((6, 6, 754, 214), 24, outline=(255, 70, 80, 255), width=10, fill=(40, 8, 14, 235))
        sd.text((380, 80), 'PAGO BLOQUEADO', font=F(64, True), fill=(255, 80, 90), anchor='mm'); sd.text((380, 160), 'por Claude · de nada', font=F(30, True), fill=(255, 200, 200), anchor='mm')
        sello = sello.rotate(-6, expand=True, resample=Image.BICUBIC); es = 0.45 + 0.3 * a; sello = sello.resize((int(sello.width * es), int(sello.height * es)))
        im.paste(sello, ((W - sello.width) // 2, 320 - sello.height // 2 + 40), sello)
    return im

def p_telegram(p, datos):
    chat = datos.get('modo', 'pump') == 'chat'      # chat: solo mensajes y la grafica sube; pump: sube y se desploma + 'vendido'
    im, d = base(datos.get('titulo', 'Canal "VIP SIGNALS" — 4.213 miembros')); rr(d, (40, 56, 760, 650), (20, 24, 38), 14, LINE)
    d.text((70, 82), '★ VIP SIGNALS ★', font=F(24, True), fill=(120, 200, 255)); d.text((70, 112), '4.213 miembros · 49 €/mes', font=F(15), fill=DIM)
    msgs = [('Admin', 'COMPRA YA $PERRO !!! ▲▲▲', (60, 120, 200)), ('Admin', '+3.400 % en 2 horas (captura)', (60, 120, 200)), ('Admin', 'Quedan 2 plazas VIP+. NO SEAS POBRE.', (60, 120, 200)),
            ('Admin', 'Yo ya estoy dentro. Compra ahora.', (60, 120, 200)), ('Admin', 'Vendido ✔ gracias por la liquidez', (200, 60, 70))]
    y = 150
    for i, (a_, t, col) in enumerate(msgs[:4] if chat else msgs):
        k = tramo(p, i * 0.15, i * 0.15 + 0.1)
        if k <= 0: continue
        w_ = d.textlength(t, font=F(20, True)) + 36; by = y + int((1 - k) * 30)
        rr(d, (70, by, 70 + w_, by + 58), mezcla((20, 24, 38), col, 0.55), 14); d.text((88, by + 12), a_, font=F(13, True), fill=(200, 220, 255)); d.text((88, by + 30), t, font=F(20, True), fill=(255, 255, 255)); y += 70
    tarjeta(d, (790, 56, W - 40, 650), '$PERRO / USDT'); serie = [0.1 + 0.04 * i for i in range(14)] + [0.7, 1.0, 0.9, 0.5, 0.2, 0.08, 0.04, 0.02]
    if chat: serie = serie[:15]; pc = 9.0
    else: pc = 0.62
    grafica(im, (820, 130, W - 70, 470), serie, p / 0.95, GR if p < pc else RD); d = ImageDraw.Draw(im)
    pr = 0.0001 * (1 + 9 * ease(p / 0.6)) if p < pc else 0.0001 * (10 - 9.9 * ease((p - 0.62) / 0.3)); d.text((820, 490), f'{pr:.5f} $'.replace('.', ','), font=F(40, True, True), fill=GR if p < pc else RD)
    chip(d, (820, 556), 'Tú compraste aquí' if p > 0.5 else 'Esperando…', OR if p > 0.5 else DIM, 18)
    if p > pc: rr(d, (800, 600, W - 50, 642), (70, 25, 35), 10, RD); d.text(((800 + W - 50) // 2, 621), '☠ PUMP & DUMP', font=F(20, True), fill=RD, anchor='mm')
    return im

def p_apalanc(p, datos):
    cap = datos.get('capital', 500); lev = datos.get('apal', 100); im, d = base(datos.get('titulo', 'Futuros — calculadora de posición')); tarjeta(d, (40, 60, 620, 650))
    d.text((70, 84), 'CAPITAL', font=F(16, True), fill=DIM); d.text((70, 108), fmt(cap, 0, '', ' €'), font=F(44, True), fill=TXT)
    a = ease(p / 0.35); x_ = int(2 + (lev - 2) * a); d.text((70, 184), 'APALANCAMIENTO', font=F(16, True), fill=DIM); d.text((70, 208), f'x{x_}', font=F(60, True), fill=OR)
    rr(d, (70, 290, 590, 306), (40, 44, 78), 8); rr(d, (70, 290, 70 + 520 * x_ / 100, 306), OR, 8); d.ellipse((60 + 520 * x_ / 100, 284, 80 + 520 * x_ / 100, 312), fill=(255, 255, 255))
    d.text((70, 340), 'TAMAÑO DE LA POSICIÓN', font=F(16, True), fill=DIM); d.text((70, 364), fmt(cap * x_, 0, '', ' €'), font=F(44, True), fill=CY)
    d.text((70, 440), 'SE LIQUIDA SI BAJA SOLO', font=F(16, True), fill=DIM); d.text((70, 464), f'-{100 / max(1, x_):.1f} %'.replace('.', ','), font=F(52, True), fill=RD)
    rr(d, (70, 560, 590, 626), (30, 33, 60), 14, OR, 2); d.text((330, 593), 'Ganar 1 % = +500 €  ·  Perder 1 % = TODO', font=F(18, True), fill=OR, anchor='mm')
    tarjeta(d, (650, 60, W - 40, 650), 'BTC/USDT'); bal = cap if p < 0.62 else cap * (1 - ease((p - 0.62) / 0.06))
    serie = [0.5 + 0.015 * math.sin(i * 1.3) for i in range(20)] + [0.46, 0.44, 0.46, 0.5, 0.52]; grafica(im, (680, 130, W - 70, 400), serie, p / 0.9, CY if p < 0.62 else RD); d = ImageDraw.Draw(im)
    d.text((680, 430), 'SALDO', font=F(16, True), fill=DIM); d.text((680, 454), fmt(max(0, bal), 0, '', ' €'), font=F(56, True), fill=GR if bal > 0 else RD)
    if p > 0.66:
        ov = Image.new('RGBA', im.size, (255, 0, 0, int(90 * tramo(p, 0.66, 0.72)))); im.paste(ov, (0, 0), ov); d = ImageDraw.Draw(im)
        rr(d, (330, 250, 950, 400), (70, 10, 20), 20, RD, 6); d.text((640, 325), '☠ LIQUIDADO', font=F(70, True), fill=(255, 90, 100), anchor='mm')
    if p > 0.85: rr(d, (670, 560, W - 60, 626), (25, 60, 45), 14, GR, 2); d.text((960, 593), 'Con x2: -1 % = -10 €. Sigues vivo.', font=F(18, True), fill=GR, anchor='mm')
    return im

VERDADES = {
    'esma': ('74–89 %', 'de las cuentas minoristas de CFD pierden dinero', 0.82, 'Fuente: ESMA (2018) — advertencia de riesgo obligatoria de los brokers', RD),
    'brasil': ('97 %', 'de los day traders que insistieron +300 días perdió dinero', 0.97, 'Fuente: Chague, De-Losso y Giovannetti — «Day Trading for a Living?» (2020)', RD),
    'brasil2': ('0,5 %', 'ganó más que un sueldo básico (8 de 1.551)', 0.005, 'Fuente: Chague, De-Losso y Giovannetti — «Day Trading for a Living?» (2020)', OR),
    'apalanc': ('30:1', 'límite UE para minoristas en divisas principales (2:1 en criptos)', 0.3, 'Fuente: ESMA (2018) — restricciones a los CFD para minoristas', CY),
}
def p_verdad(p, datos):
    n, t, frac, fuente, col = VERDADES[datos.get('tipo', 'esma')]; im, d = base(datos.get('titulo', 'Datos reales (no del gurú)')); tarjeta(d, (100, 70, W - 100, 640))
    d.text((W // 2, 150), 'DATO REAL', font=F(22, True), fill=DIM, anchor='mm'); a = ease(p / 0.5)
    d.text((W // 2, 270), n, font=F(150, True), fill=col, anchor='mm'); d.text((W // 2, 380), t, font=F(30, True), fill=TXT, anchor='mm')
    rr(d, (200, 440, W - 200, 474), (40, 44, 78), 17); rr(d, (200, 440, 200 + (W - 400) * frac * a, 474), col, 17)
    if p > 0.5: d.text((W // 2, 560), fuente, font=F(17), fill=DIM, anchor='mm')
    return im

# ====================================================================================================== DROPSHIPPING
def p_catalogo(p, datos):
    im, d = base(datos.get('titulo', 'Mi tienda — Productos')); tarjeta(d, (40, 60, W - 40, 650)); d.text((70, 80), 'PRODUCTOS', font=F(20, True), fill=DIM)
    n = int(len(PRODUCTOS) * ease(p / 0.85) + 0.001); d.text((W - 70, 70), f'{n}', font=F(44, True), fill=OR, anchor='ra')
    for i, (k, nom, pr, col) in enumerate(PRODUCTOS):
        a = tramo(p, i * 0.12, i * 0.12 + 0.12)
        if a <= 0: continue
        x = 70 + (i % 3) * 380; y = 124 + (i // 3) * 260 + int((1 - a) * 30); rr(d, (x, y, x + 350, y + 236), (28, 32, 58), 14, LINE)
        icono(d, k, x + 14, y + 14, 150, col); d.text((x + 180, y + 40), nom, font=F(21, True), fill=TXT); d.text((x + 180, y + 82), pr, font=F(30, True, True), fill=GR)
        d.text((x + 180, y + 128), 'Stock: ∞ (el proveedor)', font=F(15), fill=DIM); chip(d, (x + 180, y + 170), 'Publicado ✔' if a > 0.9 else '…', GR if a > 0.9 else DIM, 14)
    return im

def p_proveedor(p, datos):
    k = datos.get('producto', 'taza'); nom = datos.get('nombre', 'Taza térmica 450 ml'); coste = datos.get('coste', '8,10 €'); im, d = base(datos.get('titulo', 'Proveedor — ficha de producto'))
    tarjeta(d, (40, 60, W - 40, 650)); icono(d, k, 80, 100, 360, (50, 56, 100)); d.text((480, 110), nom, font=F(34, True), fill=TXT)
    d.text((480, 170), '★★★★☆ 4,1 (1.203 opiniones)', font=F(20), fill=YE); d.text((480, 230), 'PRECIO PROVEEDOR', font=F(16, True), fill=DIM)
    d.text((480, 256), coste, font=F(64, True, True), fill=GR if p < 0.2 else GR)
    filas = [('Pedido mínimo', '1 unidad', TXT), ('Stock', '999+', TXT), ('Envío', 'Gratis (¡18–35 días!)', RD), ('Marca blanca', 'Sí (la tuya)', CY)]
    for i, (a_, b_, c_) in enumerate(filas):
        kk = tramo(p, 0.1 + i * 0.12, 0.2 + i * 0.12)
        if kk <= 0: continue
        y = 380 + i * 52; d.text((480, y), a_, font=F(19), fill=DIM); d.text((880, y), b_, font=F(21, True), fill=c_)
    if p > 0.7: rr(d, (480, 600, W - 70, 640), (70, 25, 35), 10, RD); d.text((W // 2 + 205, 620), '⚠ Tu cliente esperará un MES (y no lo sabe)', font=F(19, True), fill=RD, anchor='mm')
    return im

def p_margen(p, datos):
    precio = datos.get('precio', 29.90); coste = datos.get('coste', 8.10); anuncio = datos.get('anuncio', 12.00); com = round(precio * 0.029 + 0.30, 2); iva = round(precio / 1.21 * 0.21, 2)
    ben = round(precio - coste - anuncio - com - iva, 2); roas = precio / (precio - coste - com - iva)
    im, d = base(datos.get('titulo', 'Calculadora — ¿cuánto ganas DE VERDAD?')); tarjeta(d, (40, 60, W - 40, 650))
    barras = [('Precio de venta', precio, GR), ('Coste del producto', -coste, RD), ('Anuncios (1 venta)', -anuncio, RD), ('Comisión de cobro', -com, RD), ('IVA (21 %)', -iva, RD), ('BENEFICIO REAL', ben, OR)]
    acum = 0.0; escala = 520 / precio
    for i, (n_, v, col) in enumerate(barras):
        a = tramo(p, i * 0.13, i * 0.13 + 0.12); y = 100 + i * 80
        d.text((70, y + 14), n_, font=F(21, True), fill=TXT)
        if i == 0: x0, x1 = 420, 420 + v * escala * a; acum = v
        elif i == len(barras) - 1: x0, x1 = 420, 420 + ben * escala * a
        else: x1 = 420 + acum * escala; x0 = x1 + v * escala * a; acum += v
        rr(d, (min(x0, x1), y, max(x0, x1) + 2, y + 54), col, 10); d.text((1190, y + 14), fmt(v * a, 2, '+' if v > 0 else '', ' €'), font=F(26, True, True), fill=col if i < 5 else OR, anchor='ra')
    if p > 0.8: rr(d, (70, 580, W - 70, 636), (30, 33, 60), 12, OR, 2); d.text((W // 2, 608), f'ROAS mínimo para no perder: {roas:.2f}'.replace('.', ',') + '   (precio ÷ lo que te queda antes de anuncios)', font=F(19, True), fill=OR, anchor='mm')
    return im

def p_producto(p, datos):
    k = datos.get('producto', 'cactus'); nom = datos.get('nombre', 'Lámpara cactus'); im, d = base(datos.get('titulo', 'Investigación de producto')); tarjeta(d, (40, 60, 420, 650)); icono(d, k, 70, 90, 320, (50, 62, 96))
    d.text((70, 430), nom, font=F(28, True), fill=TXT); d.text((70, 474), 'Coste 6,50 € · Venta 27,90 €', font=F(18), fill=DIM); d.text((70, 510), 'Margen bruto', font=F(16), fill=DIM); d.text((70, 534), f'{int(76 * ease(p / 0.5))} %', font=F(46, True), fill=GR)
    tarjeta(d, (450, 60, W - 40, 360), 'INTERÉS EN BÚSQUEDAS (12 meses)'); serie = [0.1, 0.1, 0.12, 0.14, 0.2, 0.5, 1.0, 0.8, 0.5, 0.3, 0.2, 0.15]; serie = [serie[int(i / 4)] * (0.9 + 0.1 * math.sin(i)) for i in range(48)]
    grafica(im, (480, 120, W - 70, 340), serie, p / 0.6, PU); d = ImageDraw.Draw(im); d.text((W - 80, 100), 'moda pasajera', font=F(15, True), fill=RD, anchor='ra') if p > 0.5 else None
    tarjeta(d, (450, 380, 830, 650), 'COMPETENCIA'); d.text((480, 430), f'{int(214 * ease(p / 0.6))}', font=F(70, True), fill=RD); d.text((480, 520), 'tiendas venden lo mismo', font=F(18, True), fill=TXT); d.text((480, 560), 'Vendedor top: 2.300 reseñas', font=F(16), fill=DIM)
    tarjeta(d, (860, 380, W - 40, 650), 'VEREDICTO')
    for i, (t, c) in enumerate((('Demanda: tendencia a la baja', YE), ('Competencia: ALTA', RD), ('Margen: bueno', GR))):
        if p > 0.45 + i * 0.12: d.text((884, 430 + i * 44), '● ' + t, font=F(17, True), fill=c)
    if p > 0.85 and not datos.get('sin_veredicto'): rr(d, (884, 574, W - 64, 630), (50, 38, 36), 12, OR, 2); d.text((W - 64 - 175, 602), 'Pruébalo con 50 €, no con 5.000 €', font=F(16, True), fill=OR, anchor='mm')
    return im

def p_pedido(p, datos):
    im, d = base(datos.get('titulo', 'Mi tienda — Pedidos')); tarjeta(d, (40, 60, W - 40, 650)); d.text((70, 80), 'PEDIDOS', font=F(20, True), fill=DIM)
    a = tramo(p, 0.05, 0.2); rr(d, (80, 124, W - 80, 214), (28, 32, 58), 14, GR if a > 0.5 else LINE); icono(d, 'cactus', 96, 134, 70, (50, 62, 96))
    d.text((190, 144), '#1001 · Lámpara cactus · Ana M.', font=F(24, True), fill=TXT); d.text((190, 180), 'Hace 3 segundos', font=F(15), fill=DIM); d.text((W - 110, 156), '+27,90 €', font=F(34, True, True), fill=GR, anchor='ra')
    if a > 0:
        ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov); r_ = random.Random(1)
        for _ in range(60):
            x = r_.randint(60, W - 60); y = int(r_.randint(0, 300) + 420 * tramo(p, 0.05, 0.5)) - 100; od.rectangle((x, y, x + 8, y + 14), fill=r_.choice([(255, 200, 80, 220), (110, 215, 235, 220), (240, 125, 85, 220), (60, 230, 150, 220)]))
        if p < 0.55: im.paste(ov, (0, 0), ov)
        d = ImageDraw.Draw(im)
    if p > 0.2: d.text((W // 2, 300), '¡PRIMER PEDIDO!', font=F(70, True), fill=OR, anchor='mm')
    if p > 0.4: rr(d, (80, 380, W - 80, 440), (30, 33, 60), 12, LINE); d.text((110, 410), 'Siguiente paso: pedírselo al proveedor', font=F(22, True), fill=TXT, anchor='lm')
    if p > 0.6: rr(d, (W - 480, 390, W - 100, 430), OR, 10); d.text((W - 290, 410), 'Comprar al proveedor →', font=F(18, True), fill=(20, 12, 8), anchor='mm')
    if p > 0.8: rr(d, (80, 480, W - 80, 560), (25, 60, 45), 14, GR); d.text((W // 2, 520), '✔ Pedido enviado al proveedor  ·  Ganas 3,44 € (si nada falla)', font=F(24, True), fill=GR, anchor='mm')
    return im

def p_tracking(p, datos):
    im, d = base(datos.get('titulo', 'Seguimiento del envío')); tarjeta(d, (40, 60, W - 40, 650)); dias = int(25 * ease(p / 0.9))
    d.text((70, 84), 'PEDIDO #1001 · Lámpara cactus', font=F(22, True), fill=TXT); d.text((W - 70, 70), f'{dias}', font=F(86, True), fill=RD if dias > 14 else OR, anchor='ra'); d.text((W - 70, 160), 'días esperando', font=F(18, True), fill=DIM, anchor='ra')
    hitos = [(0, 'Pedido confirmado', 'Día 0'), (3, 'Sale de China', 'Día 3'), (10, 'En aduana (¿perdido?)', 'Día 10'), (21, 'Llega a tu país', 'Día 21'), (25, 'Entregado', 'Día 25')]
    x0, x1, y = 120, 1160, 360; d.line([(x0, y), (x1, y)], fill=(50, 56, 98), width=10); xp = x0 + (x1 - x0) * dias / 25; d.line([(x0, y), (xp, y)], fill=OR, width=10)
    for i_, (dd, t, s) in enumerate(hitos):
        x = x0 + (x1 - x0) * dd / 25; ok = dias >= dd; d.ellipse((x - 16, y - 16, x + 16, y + 16), fill=GR if ok else (40, 44, 78), outline=(255, 255, 255) if ok else DIM, width=3); off = 44 if i_ % 2 == 0 else 112
        d.text((x, y + off), t, font=F(16, True), fill=TXT if ok else DIM, anchor='mm'); d.text((x, y + off + 24), s, font=F(14), fill=DIM, anchor='mm')
    rr(d, (xp - 30, y - 70, xp + 30, y - 30), YE, 10); d.text((xp, y - 50), '▣▶', font=F(20, True), fill=(30, 20, 5), anchor='mm')
    if dias > 14: rr(d, (150, 520, W - 150, 600), (70, 25, 35), 14, RD); d.text((W // 2, 560), 'El cliente ya está escribiendo… en mayúsculas', font=F(26, True), fill=RD, anchor='mm')
    return im

def p_cliente(p, datos):
    im, d = base(datos.get('titulo', 'Correo — Atención al cliente')); tarjeta(d, (40, 60, W - 40, 650))
    d.text((70, 82), '¡¿DÓNDE ESTÁ MI PEDIDO?!', font=F(32, True), fill=RD); d.text((70, 128), 'De: Ana M.  ·  hace 1 min', font=F(15), fill=DIM)
    txt = 'Pedí una lámpara hace 25 días. Nadie contesta. Si no llega YA quiero mi dinero y voy a llamar a consumo.'; n = int(len(txt) * tramo(p, 0.0, 0.3)); y = 170; ln = ''
    for w_ in txt[:n].split(' '):
        if d.textlength(ln + w_, font=F(21)) > W - 160: d.text((70, y), ln, font=F(21), fill=TXT); y += 32; ln = ''
        ln += w_ + ' '
    d.text((70, y), ln, font=F(21), fill=TXT)
    rr(d, (70, 330, W - 70, 600), (18, 20, 38), 14, OR); chip(d, (90, 346), 'Borrador de Claude', OR, 14)
    resp = 'Hola Ana, perdona la espera: tu pedido viene de ultramar y tarda más de lo que prometimos. Te paso el seguimiento y, si prefieres, te devuelvo el dinero hoy mismo. Gracias por avisarnos.'
    n2 = int(len(resp) * tramo(p, 0.35, 0.85)); y = 392; ln = ''
    for w_ in resp[:n2].split(' '):
        if d.textlength(ln + w_, font=F(20)) > W - 200: d.text((90, y), ln, font=F(20), fill=TXT); y += 32; ln = ''
        ln += w_ + ' '
    d.text((90, y), ln, font=F(20), fill=TXT)
    if p > 0.9: rr(d, (W - 320, 540, W - 90, 584), GR, 12); d.text((W - 205, 562), 'Enviado ✔', font=F(19, True), fill=(8, 20, 14), anchor='mm')
    return im

def p_ley(p, datos):
    im, d = base(datos.get('titulo', 'Lo que dice la ley (UE)')); tarjeta(d, (40, 60, 620, 650)); a = ease(p / 0.5)
    d.text((330, 130), 'DEVOLUCIÓN', font=F(20, True), fill=DIM, anchor='mm'); d.text((330, 260), f'{int(14 * a)}', font=F(150, True), fill=OR, anchor='mm'); d.text((330, 360), 'días naturales para desistir', font=F(24, True), fill=TXT, anchor='mm')
    d.text((330, 410), 'sin dar motivos (compras a distancia)', font=F(18), fill=DIM, anchor='mm'); d.text((330, 470), 'Te devuelven el dinero… incluso el envío', font=F(18, True), fill=CY, anchor='mm')
    d.text((330, 600), 'Directiva 2011/83/UE', font=F(15), fill=DIM, anchor='mm')
    tarjeta(d, (650, 60, W - 40, 650)); d.text((945, 130), 'IVA EN IMPORTACIONES', font=F(20, True), fill=DIM, anchor='mm')
    if p > 0.3: d.text((945, 250), 'desde 1/7/2021', font=F(40, True), fill=YE, anchor='mm'); d.text((945, 320), 'se paga IVA desde el primer euro', font=F(22, True), fill=TXT, anchor='mm')
    if p > 0.5: d.text((945, 390), '(adiós a la exención de 22 €)', font=F(20), fill=DIM, anchor='mm'); chip(d, (845, 440), 'IOSS: ventanilla única hasta 150 €', CY, 16)
    if p > 0.7: d.text((945, 600), 'Tu margen: revísalo con el IVA', font=F(16, True), fill=OR, anchor='mm')
    return im


# ====================================================================================================== EXTRAS: presupuesto, interes compuesto, anuncios
def p_presupuesto(p, datos):
    im, d = base(datos.get('titulo', 'Presupuesto — ¿a dónde se va tu sueldo?')); tarjeta(d, (40, 60, 560, 650), 'TU SUELDO')
    cats = datos.get('categorias') or [('Vivienda', 35, (110, 215, 235)), ('Comida', 15, (60, 230, 150)), ('Ocio', 12, (170, 125, 255)), ('Suscripciones (que no usas)', 9, (255, 200, 85)), ('Cafés y caprichos', 14, (240, 125, 85)), ('Ahorro', 4, (255, 85, 100)), ('Resto', 11, (90, 100, 150))]
    cx, cy, r = 300, 300, 150; ang = -90.0; tot = sum(c[1] for c in cats); barrido = ease(p / 0.7) * 360
    for n_, v, col in cats:
        a1 = ang + 360.0 * v / tot; lim = -90 + barrido
        if ang < lim: d.pieslice((cx - r, cy - r, cx + r, cy + r), ang, min(a1, lim), fill=col, outline=(20, 22, 40), width=3)
        ang = a1
    d.ellipse((cx - 80, cy - 80, cx + 80, cy + 80), fill=PANEL); d.text((cx, cy - 8), '2.100 €', font=F(34, True), fill=TXT, anchor='mm'); d.text((cx, cy + 28), 'al mes', font=F(16), fill=DIM, anchor='mm')
    tarjeta(d, (590, 60, W - 40, 650), 'DONDE SE VA')
    for i, (n_, v, col) in enumerate(cats):
        k = tramo(p, 0.1 + i * 0.08, 0.25 + i * 0.08); y = 112 + i * 62
        if k <= 0: continue
        rr(d, (620, y + 4, 640, y + 24), col, 5); d.text((652, y), n_, font=F(19, True), fill=TXT); d.text((W - 70, y), f'{int(v * k)} %', font=F(24, True, True), fill=RD if n_ == 'Ahorro' else TXT, anchor='ra')
    if p > 0.8: rr(d, (620, 560, W - 64, 628), (70, 25, 35), 12, RD); d.text((W // 2 + 290, 594), 'Ahorro 4 %. Orientación habitual: 20 %', font=F(19, True), fill=RD, anchor='mm')
    return im

def p_interes(p, datos):
    cuota = datos.get('cuota', 100); tasa = datos.get('tasa', 0.07); años = datos.get('años', 30); n = años * 12
    serie = []; v = 0.0
    for m in range(n + 1):
        serie.append(v); v = v * (1 + tasa / 12) + cuota
    aportado = cuota * n; final = serie[-1]; hasta = int(ease(p / 0.85) * n)
    im, d = base(datos.get('titulo', 'Interés compuesto — el tiempo hace el trabajo')); tarjeta(d, (40, 60, W - 40, 650))
    d.text((70, 84), f'{cuota} €/mes durante {años} años al {int(tasa * 100)} % anual (ejemplo)', font=F(22, True), fill=DIM)
    x0, y0, x1, y1 = 90, 150, 1190, 520; mx = final
    d.line([(x0, y1), (x1, y1)], fill=LINE, width=2)
    pts_total = [(x0 + (x1 - x0) * m / n, y1 - serie[m] / mx * (y1 - y0)) for m in range(0, hasta + 1, 3)]
    pts_apor = [(x0 + (x1 - x0) * m / n, y1 - (cuota * m) / mx * (y1 - y0)) for m in range(0, hasta + 1, 3)]
    if len(pts_apor) > 1: d.line(pts_apor, fill=DIM, width=4)
    if len(pts_total) > 1:
        ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov); od.polygon(pts_total + [(pts_total[-1][0], y1), (pts_total[0][0], y1)], fill=(*GR, 55)); im.paste(ov, (0, 0), ov); d = ImageDraw.Draw(im); d.line(pts_total, fill=GR, width=5)
    val = serie[min(hasta, n)]; d.text((70, 540), fmt(val, 0, '', ' €'), font=F(66, True), fill=GR); d.text((70, 618), 'lo que tendrías', font=F(16), fill=DIM)
    d.text((W - 70, 540), fmt(cuota * min(hasta, n), 0, '', ' €'), font=F(46, True), fill=DIM, anchor='ra'); d.text((W - 70, 600), 'lo que habrías puesto tú', font=F(16), fill=DIM, anchor='ra')
    if p > 0.9: d.text((W // 2, 118), 'Rentabilidad constante de ejemplo: la real varía y no está garantizada', font=F(15), fill=OR, anchor='mm')
    return im

def p_anuncios(p, datos):
    im, d = base(datos.get('titulo', 'Panel de anuncios — campaña «Lámpara cactus»')); tarjeta(d, (40, 60, 830, 400), 'EMBUDO (últimos 7 días)')
    emb = [('Impresiones', 15800, 1.0, CY), ('Clics', 126, 0.5, PU), ('Al carrito', 12, 0.25, YE), ('Compras', 3, 0.1, RD)]
    for i, (n_, v, f, col) in enumerate(emb):
        a = tramo(p, i * 0.15, i * 0.15 + 0.2); y = 110 + i * 70; d.text((70, y + 8), n_, font=F(19, True), fill=TXT)
        rr(d, (260, y, 800, y + 50), (40, 44, 78), 10); rr(d, (260, y, 260 + 540 * f * a, y + 50), col, 10); d.text((790, y + 25), fmt(v * a), font=F(24, True, True), fill=(10, 10, 20) if i < 3 else TXT, anchor='rm')
    for i, (t, val, col) in enumerate((('CTR', '0,8 %', YE), ('CPC', '0,98 €', YE), ('GASTADO', '124 €', RD))):
        x = 860 + (i % 2) * 190 if i < 2 else 860; y = 64 + (i // 2) * 130 if i < 2 else 194
        tarjeta(d, (x, y, x + 170, y + 110), t); d.text((x + 20, y + 50), val, font=F(32, True), fill=col)
    tarjeta(d, (40, 420, 830, 650), 'RESULTADO'); roas = 0.75 * ease(p / 0.8); d.text((70, 470), f'ROAS {roas:.2f}'.replace('.', ','), font=F(64, True), fill=RD); d.text((70, 560), 'ingresos ÷ gasto en anuncios (menos de 1 = pierdes)', font=F(17), fill=DIM)
    d.text((70, 596), '3 ventas × 31 € = 93 € de ingresos con 124 € gastados', font=F(17), fill=TXT)
    tarjeta(d, (860, 340, W - 40, 650), 'CLAUDE DICE')
    for i, t in enumerate(('1. Cambia la creatividad', '2. Prueba otro público', '3. Revisa la web y el precio', '4. Pausa lo que no vende')):
        if p > 0.5 + i * 0.1: d.text((884, 392 + i * 58), '✔ ' + t, font=F(17, True), fill=GR)
    return im

# recorte automatico (zona 1280x720) para el plano `pantalla_completa` en video VERTICAL: ampliar lo importante
ZOOM_AUTO = {'checkout': (330, 60, 950, 650), 'apalanc': (40, 60, 1240, 650), 'verdad': (100, 70, 1180, 640), 'cliente': (40, 60, 1240, 650), 'ley': (40, 60, 1240, 650), 'cartera': (40, 64, W - 40, 650), 'orden': (300, 64, 980, 650), 'chat': (40, 60, 900, 650), 'dashboard': (40, 64, 830, 650), 'tienda': (40, 64, 830, 650), 'tareas': (40, 64, 830, 650), 'email': (490, 64, 1240, 650)}

PANTALLAS = {'presupuesto': p_presupuesto, 'interes': p_interes, 'anuncios': p_anuncios, 'curso': p_curso, 'checkout': p_checkout, 'telegram': p_telegram, 'apalanc': p_apalanc, 'verdad': p_verdad,
             'catalogo': p_catalogo, 'proveedor': p_proveedor, 'margen': p_margen, 'producto': p_producto, 'pedido': p_pedido, 'tracking': p_tracking, 'cliente': p_cliente, 'ley': p_ley,
             'chat': p_chat, 'dashboard': p_dashboard, 'tienda': p_tienda, 'calendario': p_calendario, 'email': p_email,
             'analitica': p_analitica, 'trading': p_trading, 'cartera': p_cartera, 'orden': p_orden, 'resultado': p_resultado, 'tareas': p_tareas, 'hoja': p_hoja}

def dibujar(nombre, p=1.0, datos=None):
    datos = datos or {}; p = max(0.0, min(1.0, p))
    if datos.get('desde') is not None: p = datos['desde'] + p * (1 - datos['desde'])      # empieza la animacion ya avanzada (p. ej. 0.6)
    return PANTALLAS[nombre](p, datos)

if __name__ == '__main__':
    import sys, os
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for n in PANTALLAS:
        for p in (0.4, 1.0): dibujar(n, p).save(f'{out}/{n}_{int(p * 100)}.png')
    print('ok')
