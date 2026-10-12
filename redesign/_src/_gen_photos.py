"""Invented 'photos' for the K page: dithered 1-bit scenes, 640x420. Needs Pillow."""
import os
import random

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "img", "k")
os.makedirs(OUT, exist_ok=True)
W, H = 640, 420


def finish(img, name, tint=(255, 255, 255), noise=0.16):
    img = Image.blend(img, Image.effect_noise((W, H), 50), noise)
    one = img.convert("1")
    out = Image.new("RGB", (W, H), (0, 0, 0))
    out.paste(Image.new("RGB", (W, H), tint), mask=one)
    out.convert("P", palette=Image.ADAPTIVE, colors=4).save(os.path.join(OUT, name + ".gif"), optimize=True)


def fog_bridge():
    img = Image.new("L", (W, H)); d = ImageDraw.Draw(img)
    for y in range(H):
        d.line([0, y, W, y], fill=int(110 + 120 * (1 - abs(y - 190) / 210)))
    d.polygon([(0, 250), (W, 238), (W, 262), (0, 274)], fill=70)                     # deck
    d.polygon([(300, 250), (330, 40), (360, 250)], fill=60)                          # pylon
    for x in range(40, 600, 40):
        d.line([(330, 60), (x, 250)], fill=85)                                       # cables
    d.rectangle([0, 300, W, H], fill=150)                                            # river
    for y in range(305, H, 9):
        d.line([0, y, W, y], fill=175)
    return img


def panel_blocks(rng):
    img = Image.new("L", (W, H), 40); d = ImageDraw.Draw(img)
    for y in range(H):
        d.line([0, y, W, y], fill=int(60 + 70 * y / H))
    for bx in (20, 230, 430):
        d.rectangle([bx, 90, bx + 180, H], fill=35)
        for wy in range(105, H, 22):
            for wx in range(bx + 10, bx + 170, 24):
                d.rectangle([wx, wy, wx + 12, wy + 12], fill=230 if rng.random() < .28 else 55)
    return img


def tree_avenue(rng):
    img = Image.new("L", (W, H), 200); d = ImageDraw.Draw(img)
    d.polygon([(260, H), (380, H), (330, 200), (310, 200)], fill=230)                # path
    for side in (-1, 1):
        for k in range(7):
            x = 320 + side * (60 + k * 45); r = 70 - k * 7
            d.ellipse([x - r, 120 - r + k * 6, x + r, 120 + r + k * 6], fill=rng.randint(40, 90))
            d.rectangle([x - 4, 160 + k * 6, x + 4, 300 - k * 12], fill=30)
    return img


def stage(rng):
    img = Image.new("L", (W, H), 10); d = ImageDraw.Draw(img)
    for k in range(6):
        x = 60 + k * 105
        d.polygon([(x, 0), (x - 70, 330), (x + 70, 330)], fill=110 + k * 10)        # light beams
    d.rectangle([0, 330, W, 350], fill=160)
    for x in range(0, W, 14):                                                        # crowd
        h = rng.randint(30, 70)
        d.ellipse([x, H - h - 14, x + 14, H - h], fill=20)
        d.rectangle([x + 1, H - h, x + 13, H], fill=15)
    return img


def window_cat():
    img = Image.new("L", (W, H), 30); d = ImageDraw.Draw(img)
    d.rectangle([140, 40, 500, 330], fill=215)                                       # window light
    d.rectangle([316, 40, 324, 330], fill=40); d.rectangle([140, 180, 500, 188], fill=40)
    d.rectangle([100, 330, 540, 350], fill=90)                                       # sill
    d.ellipse([250, 230, 370, 335], fill=15)                                         # cat body
    d.ellipse([280, 175, 345, 240], fill=15)                                         # head
    d.polygon([(285, 190), (292, 160), (305, 185)], fill=15); d.polygon([(320, 185), (333, 160), (340, 190)], fill=15)
    d.line([(365, 320), (420, 300), (440, 330)], fill=15, width=12)                  # tail
    return img


def contact_sheet(rng):
    img = Image.new("L", (W, H), 25); d = ImageDraw.Draw(img)
    for row in range(3):
        y = 30 + row * 130
        d.rectangle([0, y, W, y + 110], fill=8)
        for x in range(10, W, 22):
            d.rectangle([x, y + 4, x + 10, y + 12], fill=120); d.rectangle([x, y + 98, x + 10, y + 106], fill=120)
        for f in range(4):
            fx = 20 + f * 155
            d.rectangle([fx, y + 20, fx + 140, y + 90], fill=rng.randint(90, 200))
            d.ellipse([fx + 30, y + 30, fx + 90, y + 85], fill=rng.randint(30, 240))
    return img


def chart(rng):
    img = Image.new("L", (W, H), 245); d = ImageDraw.Draw(img)
    for y in range(60, 380, 64):
        d.line([(50, y), (620, y)], fill=200)
    d.line([(50, 40), (50, 380), (620, 380)], fill=60, width=2)
    pts, v = [], 140
    for i, x in enumerate(range(55, 600, 9)):
        v += rng.uniform(-6, 6)
        if x > 520:
            v += 22                                                                  # the drop
        pts.append((x, max(60, min(370, v))))
    d.line(pts, fill=40, width=3)
    d.rectangle([540, 280, 600, 300], fill=30)
    return img


if __name__ == "__main__":
    rng = random.Random("K photos")
    finish(fog_bridge(), "hmla")
    finish(panel_blocks(rng), "panelaky", tint=(109, 174, 66))
    finish(tree_avenue(rng), "aleja")
    finish(stage(rng), "session", tint=(109, 174, 66))
    finish(window_cat(), "macka")
    finish(contact_sheet(rng), "film", tint=(200, 220, 180))
    finish(chart(rng), "graf", tint=(255, 255, 255), noise=0.04)
    print("photos:", sorted(os.listdir(OUT)))
