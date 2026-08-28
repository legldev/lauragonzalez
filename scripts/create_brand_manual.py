from io import BytesIO
from pathlib import Path
from math import cos, sin, pi

from PIL import Image, ImageOps, ImageEnhance
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


ROOT = Path('/Users/luis.garces/dev/lauragonzalez')
OUT = ROOT / 'output/pdf/Manual_de_Marca_Laura_Gonzalez.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)

W, H = landscape(A4)

# Brand palette
INK = HexColor('#24141B')
BURGUNDY = HexColor('#842851')
ROSE = HexColor('#D79A9D')
BLUSH = HexColor('#EFD4D0')
IVORY = HexColor('#F8F0ED')
PAPER = HexColor('#FFFAF7')
GOLD = HexColor('#B68659')
MUTED = HexColor('#745E65')
NIGHT = HexColor('#160E12')
WHITE = HexColor('#FFF8F5')
GREEN = HexColor('#62866A')

pdfmetrics.registerFont(TTFont('Display', '/System/Library/Fonts/Supplemental/Georgia.ttf'))
pdfmetrics.registerFont(TTFont('DisplayItalic', '/System/Library/Fonts/Supplemental/Georgia Italic.ttf'))
pdfmetrics.registerFont(TTFont('Sans', '/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('SansBold', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'))

c = canvas.Canvas(str(OUT), pagesize=(W, H), pageCompression=1)
c.setTitle('Manual de Marca Visual - Laura González')
c.setAuthor('Laura González Estudio Creativo')
c.setSubject('Identidad visual, logo, color, tipografía, fotografía y aplicaciones')


def bg(color=IVORY):
    c.setFillColor(color)
    c.rect(0, 0, W, H, stroke=0, fill=1)


def txt(text, x, y, size=10, font='Sans', color=INK, align='left'):
    c.setFont(font, size)
    c.setFillColor(color)
    if align == 'center':
        c.drawCentredString(x, y, text)
    elif align == 'right':
        c.drawRightString(x, y, text)
    else:
        c.drawString(x, y, text)


def lines(text, x, y, width, size=10, leading=None, font='Sans', color=INK):
    leading = leading or size * 1.45
    words = text.split()
    row, rows = '', []
    for word in words:
        test = f'{row} {word}'.strip()
        if pdfmetrics.stringWidth(test, font, size) <= width:
            row = test
        else:
            if row:
                rows.append(row)
            row = word
    if row:
        rows.append(row)
    for i, row in enumerate(rows):
        txt(row, x, y - i * leading, size, font, color)
    return y - len(rows) * leading


def round_rect(x, y, w, h, radius=12, fill=PAPER, stroke=None, sw=1):
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke)
        c.setLineWidth(sw)
    c.roundRect(x, y, w, h, radius, stroke=1 if stroke else 0, fill=1)


def label(text, x, y, color=BURGUNDY):
    star(x + 4, y + 4, 4, color)
    txt(text.upper(), x + 17, y, 7.5, 'SansBold', color)


def title(text, x, y, size=37, color=INK, italic_word=None):
    if not italic_word or italic_word not in text:
        txt(text, x, y, size, 'Display', color)
        return
    before, after = text.split(italic_word, 1)
    txt(before, x, y, size, 'Display', color)
    bx = x + pdfmetrics.stringWidth(before, 'Display', size)
    txt(italic_word, bx, y, size, 'DisplayItalic', BURGUNDY)
    ax = bx + pdfmetrics.stringWidth(italic_word, 'DisplayItalic', size)
    txt(after, ax, y, size, 'Display', color)


def page_footer(num, dark=False):
    color = Color(1, 1, 1, alpha=.45) if dark else MUTED
    c.setStrokeColor(Color(1, 1, 1, alpha=.12) if dark else Color(0.13, .07, .1, alpha=.12))
    c.setLineWidth(.5)
    c.line(46, 31, W - 46, 31)
    txt('LAURA GONZÁLEZ · ESTUDIO CREATIVO', 46, 15, 6.2, 'SansBold', color)
    txt(f'{num:02d}', W - 46, 15, 6.2, 'SansBold', color, 'right')


def next_page(num, dark=False):
    page_footer(num, dark)
    c.showPage()


def draw_monogram(cx, cy, radius=48, color=INK, reverse=False):
    c.setStrokeColor(color)
    c.setLineWidth(max(1, radius * .025))
    c.circle(cx, cy, radius, stroke=1, fill=0)
    txt('LG', cx, cy - radius * .18, radius * .62, 'DisplayItalic', color, 'center')


def draw_wordmark(x, y, scale=1, color=INK, center=False, with_tag=True):
    size = 29 * scale
    anchor = x
    if center:
        anchor = x - pdfmetrics.stringWidth('LAURA GONZÁLEZ', 'Display', size) / 2
    txt('LAURA GONZÁLEZ', anchor, y, size, 'Display', color)
    if with_tag:
        subtitle = 'ESTRATEGIA DIGITAL · CONTENIDO · DISEÑO WEB'
        sub_size = 5.7 * scale
        sw = pdfmetrics.stringWidth(subtitle, 'SansBold', sub_size)
        sx = x - sw / 2 if center else anchor
        txt(subtitle, sx, y - 15 * scale, sub_size, 'SansBold', color)


def draw_lockup(cx, cy, scale=1, color=INK):
    draw_monogram(cx, cy + 41 * scale, 31 * scale, color)
    draw_wordmark(cx, cy - 16 * scale, scale, color, center=True)


def crop_image(path, x, y, w, h, focus=(.5, .5), tint=None):
    with Image.open(path) as im:
        im = im.convert('RGB')
        ratio = w / h
        ir = im.width / im.height
        if ir > ratio:
            new_w = int(im.height * ratio)
            left = int((im.width - new_w) * focus[0])
            im = im.crop((left, 0, left + new_w, im.height))
        else:
            new_h = int(im.width / ratio)
            top = int((im.height - new_h) * focus[1])
            im = im.crop((0, top, im.width, top + new_h))
        im = ImageOps.fit(im, (max(1, int(w * 2)), max(1, int(h * 2))), Image.Resampling.LANCZOS)
        if tint:
            overlay = Image.new('RGB', im.size, tint)
            im = Image.blend(im, overlay, .16)
        buf = BytesIO()
        im.save(buf, 'JPEG', quality=92)
        buf.seek(0)
        c.drawImage(ImageReader(buf), x, y, w, h, mask='auto')


def star(cx, cy, r=8, color=GOLD):
    pts = []
    for i in range(8):
        a = -pi / 2 + i * pi / 4
        rr = r if i % 2 == 0 else r * .22
        pts.append((cx + cos(a) * rr, cy + sin(a) * rr))
    p = c.beginPath(); p.moveTo(*pts[0])
    for point in pts[1:]: p.lineTo(*point)
    p.close()
    c.setFillColor(color); c.drawPath(p, stroke=0, fill=1)


# 01 Cover
bg(NIGHT)
c.setFillColor(BURGUNDY); c.circle(W - 100, H - 55, 205, stroke=0, fill=1)
c.setStrokeColor(Color(1, 1, 1, alpha=.14)); c.setLineWidth(1)
c.circle(W - 98, H - 55, 162, stroke=1, fill=0); c.circle(W - 98, H - 55, 115, stroke=1, fill=0)
label('Manual de marca visual · Versión 1.0', 56, H - 62, ROSE)
draw_monogram(98, 285, 42, WHITE)
txt('LAURA', 166, 315, 58, 'Display', WHITE)
txt('GONZÁLEZ', 166, 254, 58, 'DisplayItalic', ROSE)
txt('ESTUDIO CREATIVO', 170, 226, 8, 'SansBold', WHITE)
lines('Estrategia que conecta. Creatividad que deja huella.', 170, 186, 330, 13, 19, 'Sans', HexColor('#CDBBC1'))
txt('CÓRDOBA, ARGENTINA · PARA TODO EL MUNDO', 56, 54, 7, 'SansBold', GOLD)
next_page(1, True)

# 02 Brand essence
bg(IVORY)
label('01 · Fundamentos', 48, H - 55)
title('Una marca con sensibilidad estratégica.', 48, H - 110, 38, italic_word='sensibilidad')
lines('Laura combina organización, empatía y creatividad para ayudar a marcas y emprendedoras a expresarse con claridad y crecer con intención.', 49, H - 165, 510, 12, 18, 'Sans', MUTED)
values = [
    ('CLARIDAD', 'Ordenar ideas y convertirlas en una dirección concreta.'),
    ('CERCANÍA', 'Escuchar de verdad y acompañar cada proceso sin fórmulas rígidas.'),
    ('INTENCIÓN', 'Crear contenido atractivo que también cumpla un objetivo.'),
    ('CONFIANZA', 'Dar a cada marca una presencia segura, elegante y auténtica.'),
]
for i, (head, body) in enumerate(values):
    x = 48 + (i % 2) * 382; y = 273 - (i // 2) * 115
    round_rect(x, y, 350, 88, 8, PAPER, HexColor('#E3CAC8'))
    txt(f'0{i+1}', x + 18, y + 60, 7, 'SansBold', BURGUNDY)
    txt(head, x + 58, y + 57, 9, 'SansBold', INK)
    lines(body, x + 58, y + 36, 260, 8.7, 12, 'Sans', MUTED)
next_page(2)

# 03 Big idea
bg(BURGUNDY)
star(W/2, H - 88, 13, WHITE)
txt('IDEA RECTORA', W/2, H - 124, 7.5, 'SansBold', HexColor('#F5CDD6'), 'center')
txt('Estrategia que conecta.', W/2, 338, 43, 'Display', WHITE, 'center')
txt('Creatividad que deja huella.', W/2, 288, 43, 'DisplayItalic', HexColor('#F1C3CB'), 'center')
lines('La marca no necesita gritar. Se reconoce por su criterio, su calidez y la forma en que transforma lo complejo en algo claro y atractivo.', W/2 - 250, 224, 500, 11, 17, 'Sans', WHITE)
txt('POSICIONAMIENTO', W/2, 144, 7, 'SansBold', GOLD, 'center')
txt('Premium · humana · creativa · confiable', W/2, 119, 15, 'DisplayItalic', WHITE, 'center')
next_page(3, True)

# 04 Logo system
bg(PAPER)
label('02 · Identidad visual', 48, H - 55)
title('Sistema de logo', 48, H - 105, 39)
lines('Tres firmas, una misma personalidad. Elegir la versión según el espacio y la jerarquía necesaria.', 49, H - 145, 600, 10, 15, 'Sans', MUTED)
round_rect(48, 98, 340, 330, 10, IVORY)
draw_lockup(218, 255, 1.25, INK)
txt('01 · FIRMA PRINCIPAL', 70, 122, 7, 'SansBold', BURGUNDY)
round_rect(410, 272, 384, 156, 10, NIGHT)
draw_wordmark(602, 352, .9, WHITE, center=True)
txt('02 · WORDMARK HORIZONTAL', 432, 293, 7, 'SansBold', ROSE)
round_rect(410, 98, 184, 156, 10, BLUSH)
draw_monogram(502, 181, 39, BURGUNDY)
txt('03 · MONOGRAMA', 432, 120, 7, 'SansBold', BURGUNDY)
round_rect(610, 98, 184, 156, 10, BURGUNDY)
draw_monogram(702, 181, 39, WHITE)
txt('04 · REVERSO', 632, 120, 7, 'SansBold', WHITE)
next_page(4)

# 05 Construction and clear space
bg(IVORY)
label('02 · Identidad visual', 48, H - 55)
title('Construcción & área de protección', 48, H - 105, 36)
lines('La arquitectura combina un círculo - símbolo de conexión - con un monograma editorial de iniciales entrelazadas.', 49, H - 145, 620, 10, 15, 'Sans', MUTED)
round_rect(48, 96, 458, 334, 8, PAPER, HexColor('#E3CAC8'))
cx, cy, rr = 277, 267, 102
c.setStrokeColor(HexColor('#D9B7B7')); c.setDash(3, 3); c.setLineWidth(.6)
c.rect(cx-rr-42, cy-rr-42, (rr+42)*2, (rr+42)*2, stroke=1, fill=0)
c.line(cx-160, cy, cx+160, cy); c.line(cx, cy-145, cx, cy+145)
c.setDash()
draw_monogram(cx, cy, rr, BURGUNDY)
txt('x', cx + rr + 17, cy + 4, 10, 'DisplayItalic', BURGUNDY)
txt('x', cx - 3, cy + rr + 23, 10, 'DisplayItalic', BURGUNDY)
round_rect(530, 235, 264, 195, 8, PAPER)
txt('ÁREA DE PROTECCIÓN', 552, 394, 8, 'SansBold', BURGUNDY)
lines('Mantener un espacio libre equivalente a la mitad del radio del círculo. Ningún texto, borde o imagen debe invadirlo.', 552, 363, 220, 9, 14, 'Sans', MUTED)
txt('TAMAÑO MÍNIMO', 552, 294, 8, 'SansBold', BURGUNDY)
draw_monogram(590, 262, 18, INK); txt('36 px digital', 620, 258, 8, 'Sans', MUTED)
draw_monogram(590, 217, 14, INK); txt('10 mm impreso', 620, 213, 8, 'Sans', MUTED)
round_rect(530, 96, 264, 120, 8, BLUSH)
txt('PRINCIPIO', 552, 181, 7, 'SansBold', BURGUNDY)
lines('Si el logo se siente apretado, necesita más aire.', 552, 155, 210, 13, 18, 'DisplayItalic', INK)
next_page(5)

# 06 Correct/incorrect
bg(PAPER)
label('02 · Identidad visual', 48, H - 55)
title('Uso correcto', 48, H - 105, 37)
examples = [
    ('SÍ', 'Sobre fondos de marca', NIGHT, WHITE, True),
    ('SÍ', 'En una sola tinta', IVORY, BURGUNDY, True),
    ('NO', 'No deformar', BLUSH, INK, False),
    ('NO', 'No añadir efectos', ROSE, WHITE, False),
]
for i, (tag, desc, fill, color, correct) in enumerate(examples):
    x = 48 + i * 190
    round_rect(x, 170, 168, 270, 8, fill)
    if i == 2:
        c.saveState(); c.translate(x+84, 314); c.scale(1.4, .7); draw_monogram(0, 0, 43, color); c.restoreState()
    elif i == 3:
        c.setStrokeColor(Color(1,1,1,alpha=.25)); c.setLineWidth(9); c.circle(x+84, 314, 53, stroke=1, fill=0)
        draw_monogram(x+84, 314, 43, color)
    else:
        draw_monogram(x+84, 314, 43, color)
    pill = GREEN if correct else BURGUNDY
    c.setFillColor(pill); c.roundRect(x+18, 202, 28, 16, 8, stroke=0, fill=1)
    txt(tag, x+32, 207, 6, 'SansBold', WHITE, 'center')
    lines(desc, x+18, 244, 132, 8.5, 12, 'SansBold', color)
txt('EVITAR TAMBIÉN', 48, 120, 7, 'SansBold', BURGUNDY)
txt('Cambiar colores · rotar · encerrar en otra forma · usar baja resolución · alterar la tipografía', 48, 94, 9.5, 'Sans', MUTED)
next_page(6)

# 07 Color
bg(IVORY)
label('03 · Color', 48, H - 55)
title('Paleta con carácter y calidez', 48, H - 105, 37, italic_word='carácter')
colors = [
    ('BORGOÑA FIRMA', '#842851', BURGUNDY, WHITE, 'PMS aprox. 208 C'),
    ('ROSA EMPOLVADO', '#D79A9D', ROSE, INK, 'Calidez & cercanía'),
    ('MARFIL EDITORIAL', '#F8F0ED', IVORY, INK, 'Aire & sofisticación'),
    ('ORO SUAVE', '#B68659', GOLD, WHITE, 'Acento premium'),
    ('TINTA PROFUNDA', '#24141B', INK, WHITE, 'Contraste & autoridad'),
]
widths = [200, 135, 150, 130, 131]
x = 48
for (name, hexc, fill, tc, note), w in zip(colors, widths):
    c.setFillColor(fill); c.rect(x, 190, w, 250, stroke=0, fill=1)
    txt(name, x+14, 224, 7, 'SansBold', tc)
    txt(hexc, x+14, 204, 7, 'Sans', tc)
    txt(note, x+14, 175, 6.5, 'Sans', MUTED)
    x += w
txt('PROPORCIÓN RECOMENDADA', 48, 121, 7, 'SansBold', BURGUNDY)
proportions = [(IVORY, 50), (PAPER, 18), (INK, 12), (BURGUNDY, 12), (ROSE, 5), (GOLD, 3)]
px = 48
for color, percent in proportions:
    ww = 746 * percent / 100
    c.setFillColor(color); c.rect(px, 80, ww, 27, stroke=0, fill=1)
    if percent >= 8: txt(f'{percent}%', px+ww/2, 89, 6, 'SansBold', WHITE if color in (INK, BURGUNDY) else INK, 'center')
    px += ww
c.setStrokeColor(HexColor('#D9C5C1')); c.setLineWidth(.5); c.rect(48, 80, 746, 27, stroke=1, fill=0)
next_page(7)

# 08 Typography
bg(PAPER)
label('04 · Tipografía', 48, H - 55)
title('Editorial por fuera. Clara por dentro.', 48, H - 105, 36, italic_word='Editorial')
round_rect(48, 117, 445, 328, 8, IVORY)
txt('Georgia', 74, 356, 58, 'Display', INK)
txt('Elegancia con voz propia.', 76, 310, 28, 'DisplayItalic', BURGUNDY)
lines('Uso: titulares, manifiestos, frases destacadas y firma de marca.', 76, 252, 340, 9, 14, 'Sans', MUTED)
txt('Aa Bb Cc Dd  0123456789', 76, 185, 13, 'Display', INK)
txt('SERIF PRINCIPAL · GEORGIA REGULAR / ITALIC', 76, 142, 6.5, 'SansBold', BURGUNDY)
round_rect(515, 117, 279, 328, 8, NIGHT)
txt('Arial', 540, 364, 39, 'SansBold', WHITE)
txt('Simple. Precisa. Cercana.', 542, 320, 15, 'SansBold', ROSE)
lines('Uso: cuerpo de texto, navegación, datos, botones y piezas informativas.', 542, 266, 210, 9, 14, 'Sans', HexColor('#CDBBC1'))
txt('ABCDEFGHIJKLMN', 542, 201, 9, 'SansBold', WHITE)
txt('abcdefghijklmn', 542, 179, 9, 'Sans', WHITE)
txt('0123456789', 542, 157, 9, 'Sans', WHITE)
txt('SANS SECUNDARIA · ARIAL REGULAR / BOLD', 542, 142, 6.3, 'SansBold', ROSE)
txt('Jerarquía sugerida', 48, 84, 7, 'SansBold', BURGUNDY)
txt('H1 64/62 · H2 42/44 · H3 24/28 · Cuerpo 11/17 · Etiqueta 7/10', 158, 84, 8, 'Sans', MUTED)
next_page(8)

# 09 Graphic language
bg(IVORY)
label('05 · Lenguaje gráfico', 48, H - 55)
title('Detalles que dejan huella', 48, H - 105, 38, italic_word='huella')
items = [
    ('01', 'ARCO', 'Enmarca retratos y representa evolución.'),
    ('02', 'DESTELLO', 'Señala ideas, momentos clave y pequeños logros.'),
    ('03', 'LÍNEA FINA', 'Ordena la información sin endurecerla.'),
    ('04', 'CÍRCULO', 'Conexión, comunidad y acompañamiento.'),
]
for i, (num, head, body) in enumerate(items):
    x = 48 + i*190
    round_rect(x, 156, 168, 280, 8, PAPER, HexColor('#E5D0CD'))
    txt(num, x+18, 408, 7, 'SansBold', BURGUNDY)
    c.setStrokeColor(BURGUNDY); c.setFillColor(BLUSH); c.setLineWidth(1.2)
    if i == 0: c.roundRect(x+50, 276, 68, 92, 34, stroke=1, fill=1)
    elif i == 1: star(x+84, 323, 40, BURGUNDY)
    elif i == 2:
        for n in range(4): c.line(x+42, 296+n*18, x+126, 296+n*18)
    else:
        c.circle(x+84, 323, 39, stroke=1, fill=0); c.circle(x+84, 323, 26, stroke=1, fill=0)
    txt(head, x+18, 228, 9, 'SansBold', INK)
    lines(body, x+18, 204, 132, 8, 12, 'Sans', MUTED)
txt('Patrón de marca', 48, 114, 7, 'SansBold', BURGUNDY)
c.setStrokeColor(HexColor('#D9B7B7')); c.setLineWidth(.6)
for i in range(17):
    xx = 48+i*45
    c.circle(xx, 79, 13, stroke=1, fill=0)
    star(xx+22, 79, 4, GOLD)
next_page(9)

# 10 Photography
bg(NIGHT)
label('06 · Fotografía', 48, H - 55, ROSE)
txt('Laura, en primer plano.', 48, H - 111, 39, 'Display', WHITE)
lines('La fotografía debe sentirse real, luminosa y segura. Premium no significa distante: la cercanía es parte de la marca.', 49, H - 152, 545, 10, 15, 'Sans', HexColor('#CDBBC1'))
photos = [
    (ROOT/'public/images/laura-05.jpeg', 48, 87, 248, 300, (.5,.2)),
    (ROOT/'public/images/laura-02.jpeg', 312, 87, 226, 300, (.5,.18)),
    (ROOT/'public/images/laura-01.jpeg', 554, 87, 240, 300, (.5,.15)),
]
for path, x, y, w, h, focus in photos: crop_image(path, x, y, w, h, focus)
txt('SÍ', 48, 56, 7, 'SansBold', ROSE); txt('Luz cálida · gestos naturales · encuadres limpios · textura · mirada segura', 76, 56, 7.5, 'Sans', WHITE)
next_page(10, True)

# 11 Voice
bg(PAPER)
label('07 · Voz & mensaje', 48, H - 55)
title('Hablar como una aliada experta', 48, H - 105, 37, italic_word='aliada')
round_rect(48, 214, 360, 220, 8, IVORY)
txt('LA VOZ ES', 72, 397, 7, 'SansBold', BURGUNDY)
for i, item in enumerate(['Cercana, no informal en exceso', 'Segura, no arrogante', 'Clara, no simplista', 'Femenina, no estereotipada', 'Estratégica, no fría']):
    star(76, 358-i*35, 4, GOLD); txt(item, 91, 354-i*35, 10, 'Sans', INK)
round_rect(430, 214, 364, 220, 8, BURGUNDY)
txt('FRASES DE MARCA', 454, 397, 7, 'SansBold', ROSE)
quotes = ['“Hagamos que tu marca se sienta.”', '“Crecer con intención.”', '“Menos ruido. Más conexión.”', '“Ideas claras, contenido con alma.”']
for i, item in enumerate(quotes): txt(item, 454, 354-i*46, 13, 'DisplayItalic', WHITE)
txt('PRINCIPIO DE REDACCIÓN', 48, 162, 7, 'SansBold', BURGUNDY)
lines('Primero la persona, después la herramienta. Hablar del cambio que la clienta desea antes de explicar el servicio.', 48, 135, 746, 11, 17, 'Sans', MUTED)
txt('Ejemplo', 48, 82, 7, 'SansBold', BURGUNDY)
txt('“Ordenamos tu estrategia para que comunicar deje de sentirse pesado y empiece a generar oportunidades.”', 102, 80, 10, 'DisplayItalic', INK)
next_page(11)

# 12 Social applications
bg(IVORY)
label('08 · Aplicaciones', 48, H - 55)
title('Una presencia coherente', 48, H - 105, 38)
# Phone mockup
round_rect(49, 80, 230, 385, 26, NIGHT)
round_rect(61, 94, 206, 356, 18, PAPER)
c.setFillColor(NIGHT); c.roundRect(118, 437, 92, 7, 4, stroke=0, fill=1)
crop_image(ROOT/'public/images/laura-05.jpeg', 61, 286, 206, 164, (.5,.1))
c.setFillColor(Color(.13,.07,.1,alpha=.34)); c.rect(61,286,206,164,stroke=0,fill=1)
draw_monogram(91, 416, 17, WHITE)
txt('Tu marca merece', 78, 257, 20, 'Display', INK)
txt('ser inolvidable.', 78, 234, 20, 'DisplayItalic', BURGUNDY)
lines('Estrategia y contenido para crecer con intención.', 78, 204, 152, 8, 12, 'Sans', MUTED)
c.setFillColor(BURGUNDY); c.roundRect(78, 143, 142, 34, 3, stroke=0, fill=1); txt('HABLEMOS DE TU MARCA', 149, 155, 6.2, 'SansBold', WHITE, 'center')
# Social tiles
round_rect(316, 292, 216, 173, 8, BURGUNDY)
star(505, 433, 9, ROSE); txt('Menos ruido.', 338, 385, 25, 'Display', WHITE); txt('Más conexión.', 338, 354, 25, 'DisplayItalic', HexColor('#F1C3CB')); txt('@lauragonzalez', 338, 314, 6.5, 'SansBold', WHITE)
round_rect(551, 292, 242, 173, 8, PAPER)
draw_wordmark(672, 385, .58, INK, center=True)
c.setStrokeColor(BURGUNDY); c.line(580, 330, 764, 330)
txt('ESTRATEGIA · CONTENIDO · WEB', 672, 309, 6.2, 'SansBold', BURGUNDY, 'center')
round_rect(316, 80, 477, 190, 8, NIGHT)
crop_image(ROOT/'public/images/laura-03.jpeg', 316, 80, 185, 190, (.5,.25), '#6B3848')
txt('CRECER CON', 530, 212, 8, 'SansBold', ROSE); txt('intención.', 530, 160, 36, 'DisplayItalic', WHITE); lines('Consultoría digital para transformar ideas en una marca clara y deseada.', 531, 125, 220, 8.5, 13, 'Sans', HexColor('#CDBBC1'))
next_page(12)

# 13 Digital and CTA
bg(BURGUNDY)
label('09 · Implementación', 48, H - 55, ROSE)
txt('Checklist de consistencia', 48, H - 111, 39, 'Display', WHITE)
checks = [
    'Usar siempre una versión oficial del logo.',
    'Mantener el borgoña como color de reconocimiento.',
    'Reservar la cursiva para emoción y énfasis.',
    'Dar aire: menos elementos, mejor jerarquía.',
    'Elegir fotografías reales, cálidas y seguras.',
    'Escribir con claridad, empatía y una acción concreta.',
]
for i, item in enumerate(checks):
    x = 48 + (i%2)*385; y = 386 - (i//2)*92
    c.setStrokeColor(Color(1,1,1,alpha=.25)); c.circle(x+15, y+4, 14, stroke=1, fill=0)
    c.setStrokeColor(WHITE); c.setLineWidth(1.4)
    c.line(x+8, y+4, x+13, y-1); c.line(x+13, y-1, x+22, y+8)
    lines(item, x+42, y+8, 300, 10, 15, 'Sans', WHITE)
round_rect(48, 70, 746, 67, 8, HexColor('#6D1E42'))
txt('REGLA DE ORO', 72, 106, 7, 'SansBold', ROSE)
txt('Si se siente claro, cuidado y con intención, se siente Laura.', 185, 99, 16, 'DisplayItalic', WHITE)
next_page(13, True)

# 14 Closing
bg(NIGHT)
c.setFillColor(BURGUNDY); c.circle(W/2, H/2+28, 192, stroke=0, fill=1)
c.setStrokeColor(Color(1,1,1,alpha=.13)); c.circle(W/2, H/2+28, 155, stroke=1, fill=0); c.circle(W/2, H/2+28, 116, stroke=1, fill=0)
draw_monogram(W/2, H/2+82, 38, WHITE)
txt('LAURA GONZÁLEZ', W/2, H/2+5, 31, 'Display', WHITE, 'center')
txt('ESTUDIO CREATIVO', W/2, H/2-20, 7.5, 'SansBold', ROSE, 'center')
txt('Estrategia que conecta. Creatividad que deja huella.', W/2, H/2-65, 12, 'DisplayItalic', WHITE, 'center')
txt('laura-gonzalez-estudio-creativo.lgel.chatgpt.site', W/2, 72, 7, 'Sans', HexColor('#CDBBC1'), 'center')
next_page(14, True)

c.save()
print(OUT)
