"""Texturas procedurales (PIL): 3 pantallas de PC, ventana con ciudad nocturna, neon, poster."""
import sys, os, random, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
MONOB = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
SANSB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
F = lambda p, s: ImageFont.truetype(p, s)
W, H = 1280, 720
BG = (13, 15, 30); PANEL = (22, 25, 46); LINE = (45, 50, 85)
GREEN = (60, 230, 150); RED = (255, 80, 95); ORANGE = (240, 125, 85); CYAN = (110, 215, 235); TXT = (210, 215, 235); DIM = (110, 118, 150)

def rr(d, box, fill, r=14, outline=None, w=2): d.rounded_rectangle(box, r, fill=fill, outline=outline, width=w)

def base(title):
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    # fondo con degradado suave
    for y in range(H):
        c = int(8 + 20 * y / H); d.line([(0, y), (W, y)], fill=(c, c + 2, c + 18))
    rr(d, (0, 0, W, 38), (10, 11, 22), 0)
    for i, c in enumerate(((255, 95, 90), (255, 190, 60), (60, 210, 110))): d.ellipse((16 + i * 26, 12, 30 + i * 26, 26), fill=c)
    d.text((W // 2, 19), title, font=F(SANSB, 18), fill=DIM, anchor='mm')
    d.text((W - 24, 19), '23:41  ▮▮▮  WiFi', font=F(SANS, 16), fill=DIM, anchor='rm')
    # dock
    rr(d, (W // 2 - 270, H - 66, W // 2 + 270, H - 12), (25, 28, 52), 20, LINE)
    for i, c in enumerate((ORANGE, CYAN, GREEN, (170, 120, 255), (255, 200, 80), RED, (120, 160, 255))):
        rr(d, (W // 2 - 246 + i * 74, H - 58, W // 2 - 246 + i * 74 + 46, H - 20), c, 10)
    return im, d

def cursor(d, x, y):
    pts = [(x, y), (x, y + 34), (x + 9, y + 26), (x + 16, y + 40), (x + 23, y + 37), (x + 16, y + 23), (x + 28, y + 23)]
    d.polygon([(px + 2, py + 2) for px, py in pts], fill=(0, 0, 0)); d.polygon(pts, fill=(255, 255, 255), outline=(0, 0, 0))

def candles(d, box, n=26, seed=3, dip_at=13):
    x0, y0, x1, y1 = box; random.seed(seed)
    rr(d, box, PANEL, 12, LINE)
    for k in range(1, 5):
        yy = y0 + (y1 - y0) * k / 5; d.line([(x0 + 10, yy), (x1 - 70, yy)], fill=(35, 40, 70), width=1)
    price = 0.35; pts = []
    for i in range(n):
        dlt = 0.045 if i < dip_at else (-0.085 if i < dip_at + 5 else 0.03)
        dlt += random.uniform(-0.03, 0.03); o, c = price, price + dlt; price = c
        hi, lo = max(o, c) + random.uniform(0.01, 0.04), min(o, c) - random.uniform(0.01, 0.04)
        pts.append((o, c, hi, lo))
    ys = [v for p in pts for v in (p[2], p[3])]; mn, mx = min(ys), max(ys)
    def Y(v): return y1 - 20 - (v - mn) / (mx - mn) * (y1 - y0 - 50)
    step = (x1 - x0 - 90) / n
    for i, (o, c, hi, lo) in enumerate(pts):
        x = x0 + 24 + i * step; col = GREEN if c >= o else RED
        d.line([(x, Y(hi)), (x, Y(lo))], fill=col, width=3)
        d.rectangle((x - step * 0.3, Y(max(o, c)), x + step * 0.3, Y(min(o, c)) + 2), fill=col)
    last = Y(pts[-1][1]); d.line([(x0 + 10, last), (x1 - 70, last)], fill=(255, 255, 255), width=1)
    rr(d, (x1 - 68, last - 13, x1 - 6, last + 13), RED if pts[-1][1] < pts[-1][0] else GREEN, 6)
    d.text((x1 - 37, last), '61.2k', font=F(MONOB, 14), fill=(10, 10, 20), anchor='mm')
    return Y(pts[-1][1])

# ---- A: grafico con el dip y la linea de stop vacia
im, d = base('TradeDesk — BTC/USDT  ·  15m');
d.text((40, 62), 'BTC/USDT', font=F(SANSB, 30), fill=TXT); d.text((235, 66), '61,240.50', font=F(MONOB, 30), fill=RED)
d.text((470, 70), '▼ -6.21%', font=F(SANSB, 24), fill=RED)
for i, t in enumerate(('1m', '5m', '15m', '1h', '4h', '1D')):
    rr(d, (900 + i * 55, 60, 945 + i * 55, 92), ORANGE if t == '15m' else (30, 34, 62), 8); d.text((922 + i * 55, 76), t, font=F(SANSB, 16), fill=(10, 10, 20) if t == '15m' else DIM, anchor='mm')
ly = candles(d, (40, 110, 900, 590))
d.line([(50, ly + 70), (830, ly + 70)], fill=ORANGE, width=3)
rr(d, (60, ly + 48, 250, ly + 92), (60, 35, 25), 8, ORANGE); d.text((155, ly + 70), 'STOP LOSS  ???', font=F(MONOB, 17), fill=ORANGE, anchor='mm')
rr(d, (920, 110, 1240, 590), PANEL, 12, LINE); d.text((940, 130), 'ORDER BOOK', font=F(SANSB, 18), fill=DIM)
random.seed(5)
for i in range(14):
    y = 165 + i * 28; w = random.randint(60, 220); col = RED if i < 7 else GREEN
    d.rectangle((1230 - w, y, 1230, y + 20), fill=tuple(int(c * 0.35) for c in col)); d.text((940, y + 10), f'{61300 - i * 12 + (0 if i < 7 else -20)}', font=F(MONO, 16), fill=col, anchor='lm')
rr(d, (940, 530, 1220, 575), RED, 10); d.text((1080, 552), '⚠  Sin stop definido', font=F(SANSB, 18), fill=(255, 255, 255), anchor='mm')
cursor(d, 700, 300)
im.save(f'{OUT}/screen_chart.png')

# ---- B: chat tipo terminal con Claude
im, d = base('claude — ~/trading')
rr(d, (40, 60, 800, 650), (16, 18, 34), 14, LINE)
lines = [(TXT, '> Claude, ¿compro el dip?'), (DIM, ''), (CYAN, '● Revisando tu plan…'), (GREEN, '  ✔ Entrada: 61,200'), (GREEN, '  ✔ Tamaño: 0.5 BTC'),
         (RED, '  ✖ Stop loss: (vacío)'), (DIM, ''), (ORANGE, '● Antes de entrar, define tu stop.'), (TXT, '  Si no sabes dónde sales,'), (TXT, '  todavía no estás operando.'), (DIM, ''), (TXT, '> _')]
for i, (c, t) in enumerate(lines): d.text((64, 82 + i * 42), t, font=F(MONOB, 25), fill=c)
rr(d, (830, 60, 1240, 340), PANEL, 14, LINE); d.text((852, 78), 'POSICIÓN', font=F(SANSB, 18), fill=DIM)
for i, (a, b, c) in enumerate((('Par', 'BTC/USDT', TXT), ('Entrada', '61,200', TXT), ('P&L', '-1,240 $', RED), ('Riesgo', '▲▲▲ Alto', ORANGE))):
    d.text((852, 120 + i * 50), a, font=F(SANS, 20), fill=DIM); d.text((1220, 120 + i * 50), b, font=F(MONOB, 22), fill=c, anchor='ra')
candles(d, (830, 360, 1240, 650), n=14, seed=9, dip_at=7)
cursor(d, 1010, 250)
im.save(f'{OUT}/screen_chat.png')

# ---- C: ticket de orden con boton de comprar
im, d = base('TradeDesk — Nueva orden')
rr(d, (300, 70, 980, 640), PANEL, 20, LINE)
rr(d, (330, 98, 640, 150), GREEN, 12); d.text((485, 124), 'COMPRAR', font=F(SANSB, 24), fill=(8, 20, 14), anchor='mm')
rr(d, (650, 98, 950, 150), (40, 28, 40), 12, RED); d.text((800, 124), 'VENDER', font=F(SANSB, 24), fill=RED, anchor='mm')
fields = [('Entrada', '61,200.00', TXT, LINE), ('Tamaño', '0.50 BTC', TXT, LINE), ('Take profit', '64,000.00', GREEN, LINE), ('Stop loss', '— — —', RED, RED)]
for i, (a, b, c, ol) in enumerate(fields):
    y = 185 + i * 82; d.text((332, y), a, font=F(SANS, 19), fill=DIM)
    rr(d, (332, y + 28, 948, y + 66), (14, 16, 32), 10, ol, 3 if ol == RED else 2); d.text((350, y + 47), b, font=F(MONOB, 24), fill=c, anchor='lm')
rr(d, (332, 520, 948, 600), GREEN, 16); d.text((640, 560), 'CONFIRMAR COMPRA', font=F(SANSB, 30), fill=(8, 20, 14), anchor='mm')
rr(d, (1000, 120, 1250, 230), (70, 25, 35), 14, RED); d.text((1125, 150), '⚠ Falta el stop', font=F(SANSB, 20), fill=(255, 255, 255), anchor='mm'); d.text((1125, 190), 'Riesgo sin límite', font=F(SANS, 16), fill=(255, 190, 190), anchor='mm')
cursor(d, 760, 548)
im.save(f'{OUT}/screen_order.png')

# ---- pantalla neutra (por defecto en la biblioteca: no enfoca nada de trading)
im, d = base('')
im.save(f'{OUT}/screen_vacia.png')

# ---- ventana: ciudad nocturna
w, h = 800, 920; im = Image.new('RGB', (w, h)); d = ImageDraw.Draw(im); random.seed(21)
for y in range(h):
    k = y / h; d.line([(0, y), (w, y)], fill=(int(24 + 190 * k ** 2.2), int(14 + 70 * k ** 2.2), int(70 + 20 * k - 30 * k ** 2)))
for _ in range(90): d.point((random.randint(0, w), random.randint(0, int(h * 0.5))), fill=(255, 255, 255))
d.ellipse((560, 90, 650, 180), fill=(255, 240, 200))
for layer, (col, base_h, wcol) in enumerate((((50, 30, 90), 420, (255, 190, 120)), ((24, 16, 52), 300, (255, 215, 140)))):
    x = -20
    while x < w:
        bw = random.randint(70, 130); bh = base_h + random.randint(-140, 160)
        d.rectangle((x, h - bh, x + bw, h), fill=col)
        for yy in range(h - bh + 16, h - 10, 26):
            for xx in range(x + 10, x + bw - 14, 22):
                if random.random() < 0.45: d.rectangle((xx, yy, xx + 9, yy + 13), fill=wcol)
        x += bw + random.randint(-10, 8)
im.save(f'{OUT}/window.png')

# ---- neon "TRADE"
nw, nh = 640, 220; neon = Image.new('RGB', (nw, nh), (8, 6, 16)); nd = ImageDraw.Draw(neon)
nd.text((nw // 2, nh // 2), 'TRADE', font=F(SANSB, 130), fill=(255, 80, 200), anchor='mm')
glow = neon.filter(ImageFilter.GaussianBlur(14)); out = Image.blend(neon, glow, 0.0)
from PIL import ImageChops
out = ImageChops.add(neon, glow); nd2 = ImageDraw.Draw(out); nd2.text((nw // 2, nh // 2), 'TRADE', font=F(SANSB, 130), fill=(255, 190, 240), anchor='mm')
out.save(f'{OUT}/neon.png')

# ---- poster pixel-art
pw, ph = 420, 560; im = Image.new('RGB', (pw, ph), (235, 225, 200)); d = ImageDraw.Draw(im)
d.rectangle((14, 14, pw - 14, ph - 14), outline=(40, 30, 60), width=6)
d.text((pw // 2, 70), 'BUY THE DIP', font=F(SANSB, 44), fill=(40, 30, 60), anchor='mm'); d.text((pw // 2, 118), '(con stop loss)', font=F(SANS, 24), fill=(200, 60, 60), anchor='mm')
random.seed(2); x = 50; y = 380
for i in range(11):
    dy = random.randint(-45, 18) if i < 6 else random.randint(-10, 50)
    col = (60, 170, 110) if dy < 0 else (210, 70, 80); d.rectangle((x, min(y, y + dy), x + 20, max(y, y + dy) + 6), fill=col); y += dy; x += 30
im.save(f'{OUT}/poster.png')
# ---- ventanas de dia y atardecer
def ventana(nombre, cielo, sol, edif, ventanas, nubes):
    w, h = 800, 920; im = Image.new('RGB', (w, h)); d = ImageDraw.Draw(im); rnd = random.Random(5)
    for y in range(h):
        k = y / h; d.line([(0, y), (w, y)], fill=tuple(int(cielo[0][i] + (cielo[1][i] - cielo[0][i]) * k) for i in range(3)))
    d.ellipse((sol[0] - sol[2], sol[1] - sol[2], sol[0] + sol[2], sol[1] + sol[2]), fill=sol[3])
    if nubes:
        cl = Image.new('RGBA', (w, h), (0, 0, 0, 0)); cd = ImageDraw.Draw(cl)
        for _ in range(7):
            x, y = rnd.randint(0, w), rnd.randint(40, 420)
            for k in range(5): cd.ellipse((x + k * 40 - 20, y - 18, x + k * 40 + 70, y + 26), fill=(255, 255, 255, 190))
        im.paste(cl.filter(ImageFilter.GaussianBlur(5)), (0, 0), cl.filter(ImageFilter.GaussianBlur(5)))
        d = ImageDraw.Draw(im)
    for capa, (col, base_h) in enumerate(((edif[0], 400), (edif[1], 290))):
        x = -20
        while x < w:
            bw = rnd.randint(70, 130); bh = base_h + rnd.randint(-120, 150); d.rectangle((x, h - bh, x + bw, h), fill=col)
            for yy in range(h - bh + 16, h - 10, 26):
                for xx in range(x + 10, x + bw - 14, 22):
                    if rnd.random() < 0.4: d.rectangle((xx, yy, xx + 9, yy + 13), fill=ventanas)
            x += bw + rnd.randint(-10, 8)
    im.save(f'{OUT}/{nombre}.png')
ventana('window_dia', ((95, 160, 232), (196, 228, 252)), (640, 130, 50, (255, 244, 190)), ((150, 165, 200), (112, 124, 160)), (205, 225, 245), True)
ventana('window_atardecer', ((64, 44, 112), (255, 150, 84)), (400, 640, 110, (255, 214, 120)), ((120, 62, 110), (58, 30, 74)), (255, 200, 110), False)

# ---- neon y poster de TIENDA
nw, nh = 640, 220; neon = Image.new('RGB', (nw, nh), (8, 6, 16)); nd = ImageDraw.Draw(neon)
nd.text((nw // 2, nh // 2 - 8), 'OPEN', font=F(SANSB, 130), fill=(60, 230, 215), anchor='mm'); nd.text((nw // 2, nh - 22), 'TIENDA ONLINE 24h', font=F(SANSB, 26), fill=(255, 120, 190), anchor='mm')
glow = neon.filter(ImageFilter.GaussianBlur(14)); out = ImageChops.add(neon, glow); nd2 = ImageDraw.Draw(out)
nd2.text((nw // 2, nh // 2 - 8), 'OPEN', font=F(SANSB, 130), fill=(190, 255, 250), anchor='mm'); out.save(f'{OUT}/neon_tienda.png')
pw, ph = 420, 560; im = Image.new('RGB', (pw, ph), (244, 236, 216)); d = ImageDraw.Draw(im)
d.rectangle((14, 14, pw - 14, ph - 14), outline=(60, 40, 40), width=6)
d.text((pw // 2, 76), 'ENVÍO', font=F(SANSB, 60), fill=(200, 60, 60), anchor='mm'); d.text((pw // 2, 140), 'GRATIS*', font=F(SANSB, 60), fill=(200, 60, 60), anchor='mm')
d.text((pw // 2, 188), '*en 15-30 días (a veces)', font=F(SANS, 22), fill=(90, 70, 70), anchor='mm')
d.rectangle((110, 260, 310, 440), fill=(196, 150, 100), outline=(120, 84, 52), width=5); d.rectangle((195, 260, 225, 440), fill=(238, 220, 175)); d.polygon([(110, 260), (140, 225), (330, 225), (310, 260)], fill=(214, 168, 118))
d.text((pw // 2, 500), 'dropshipping', font=F(SANSB, 30), fill=(60, 40, 40), anchor='mm'); im.save(f'{OUT}/poster_tienda.png')
print('tex ok')
