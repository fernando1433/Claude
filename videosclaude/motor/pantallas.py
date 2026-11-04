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

# recorte automatico (zona 1280x720) para el plano `pantalla_completa` en video VERTICAL: ampliar lo importante
ZOOM_AUTO = {'cartera': (40, 64, W - 40, 650), 'orden': (300, 64, 980, 650), 'chat': (40, 60, 900, 650), 'dashboard': (40, 64, 830, 650), 'tienda': (40, 64, 830, 650), 'tareas': (40, 64, 830, 650), 'email': (490, 64, 1240, 650)}

PANTALLAS = {'chat': p_chat, 'dashboard': p_dashboard, 'tienda': p_tienda, 'calendario': p_calendario, 'email': p_email,
             'analitica': p_analitica, 'trading': p_trading, 'cartera': p_cartera, 'orden': p_orden, 'resultado': p_resultado, 'tareas': p_tareas, 'hoja': p_hoja}

def dibujar(nombre, p=1.0, datos=None):
    return PANTALLAS[nombre](max(0.0, min(1.0, p)), datos or {})

if __name__ == '__main__':
    import sys, os
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for n in PANTALLAS:
        for p in (0.4, 1.0): dibujar(n, p).save(f'{out}/{n}_{int(p * 100)}.png')
    print('ok')
