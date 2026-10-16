"""Render the README cover from actual toy screenshots. Requires Pillow."""
from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'readme'
OUT.mkdir(parents=True, exist_ok=True)
PAPER, INK, MUTED, ACCENT, LINE = '#f4f1e9', '#282922', '#696b60', '#9c492f', '#d5d3c8'
canvas = Image.new('RGB', (1800, 1050), PAPER)
draw = ImageDraw.Draw(canvas)


def font(size, italic=False, sans=False):
    win = Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts'
    candidates = ([win / 'arial.ttf', Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')]
                  if sans else [win / ('georgiai.ttf' if italic else 'georgia.ttf'),
                                Path('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf')])
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default(size=size)


def tracked(text, xy, spacing=4, size=17, fill=MUTED):
    x, y = xy
    f = font(size, sans=True)
    for char in text:
        draw.text((x, y), char, font=f, fill=fill)
        x += draw.textlength(char, font=f) + spacing


tracked('SMALL GAMES / TACTILE GOODS', (80, 58), size=17)
tracked('A COLLECTION TO PLAY WITH', (1185, 58), size=15, spacing=3)
draw.line((80, 108, 1720, 108), fill=INK, width=2)
tracked('MATERIAL. MOTION. A MOMENT.', (85, 210), size=14, spacing=2)
draw.text((70, 260), 'Small', font=font(176), fill=INK)
draw.text((135, 435), 'Games.', font=font(176, italic=True), fill=ACCENT)
draw.text((86, 674), 'Soft things, small gestures,', font=font(29), fill=INK)
draw.text((86, 720), 'a little room to play.', font=font(29), fill=INK)
draw.line((86, 822, 700, 822), fill=LINE, width=2)
tracked('17 WEB TOYS', (86, 855), size=17, spacing=2)
tracked('01 REUSABLE SKILL', (375, 855), size=17, spacing=2)
tracked('HTML / THREE.JS / NO BUILD STEP', (86, 940), size=12, spacing=2)

tiles = [
    ('caramel-pudding', '22 / CARAMEL PUDDING', (835, 172), (35, 220, 1100, 785)),
    ('jelly-bricks', '09 / JELLY BRICKS', (1288, 172), (70, 225, 1090, 835)),
    ('mochi-pets', '13 / MOCHI PETS', (835, 596), (0, 210, 1110, 840)),
    ('soap-bubbles', '10 / SOAP BUBBLES', (1288, 596), (70, 210, 1100, 835)),
]
for name, label, (x, y), crop in tiles:
    shot = Image.open(ROOT / 'assets' / 'previews' / f'{name}.jpg').convert('RGB')
    shot = ImageOps.contain(shot.crop(crop), (405, 326), Image.Resampling.LANCZOS)
    tile = Image.new('RGB', (430, 350), '#ffffff')
    tile.paste(shot, ((430 - shot.width) // 2, (350 - shot.height) // 2))
    canvas.paste(tile, (x, y))
    draw.rectangle((x, y, x + 429, y + 349), outline=LINE)
    tracked(label, (x, y + 369), size=12, spacing=2)

canvas.save(OUT / 'cover.png', optimize=True)
detail = Image.new('RGB', (1200, 1000), '#ffffff')
shot = Image.open(ROOT / 'assets' / 'previews' / 'caramel-pudding.jpg').convert('RGB')
shot = ImageOps.contain(shot.crop((35, 220, 1100, 785)), (1140, 860), Image.Resampling.LANCZOS)
detail.paste(shot, ((1200 - shot.width) // 2, (1000 - shot.height) // 2))
detail.save(OUT / 'pudding-detail.jpg', quality=91, optimize=True)
icon = Image.new('RGB', (128, 128), PAPER)
idraw = ImageDraw.Draw(icon)
idraw.text((27, 8), 'g', font=font(94, italic=True), fill=ACCENT)
icon.save(ROOT / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)])
print(OUT / 'cover.png')
