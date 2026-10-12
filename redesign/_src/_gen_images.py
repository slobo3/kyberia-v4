"""Generate invented user icons (50x50 GIFs, some animated) and node images for the v4 showcase.

Everything is procedural and invented — no real kyberia user's icon is used.
Needs Pillow (pip install pillow). Run from anywhere: python redesign/_src/_gen_images.py
"""
import os
import random
import sys
import unicodedata

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _content import MAIN, USERS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UDIR = os.path.join(ROOT, "img", "u")
NDIR = os.path.join(ROOT, "img", "n")
os.makedirs(UDIR, exist_ok=True)
os.makedirs(NDIR, exist_ok=True)


def slug(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return "".join(c if c.isalnum() else "_" for c in s.lower())


# ── tiny 3x5 pixel font for marquees ─────────────────────────────────────
FONT = {
    "a": "010101111101101", "b": "110101110101110", "c": "011100100100011", "d": "110101101101110",
    "e": "111100110100111", "f": "111100110100100", "g": "011100101101011", "h": "101101111101101",
    "i": "111010010010111", "j": "001001001101010", "k": "101101110101101", "l": "100100100100111",
    "m": "101111111101101", "n": "110101101101101", "o": "010101101101010", "p": "110101110100100",
    "q": "010101101110011", "r": "110101110101101", "s": "011100010001110", "t": "111010010010010",
    "u": "101101101101111", "v": "101101101101010", "w": "101101111111101", "x": "101101010101101",
    "y": "101101010010010", "z": "111001010100111", "_": "000000000000111", " ": "000000000000000",
    "0": "111101101101111", "1": "010110010010111", "2": "110001010100111", "3": "110001010001110",
    "4": "101101111001001", "5": "111100110001110", "6": "011100110101010", "7": "111001010010010",
    "8": "010101010101010", "9": "010101011001110",
}


def text_strip(text, color, bg, scale=2):
    text = slug(text).replace("_", " ") + "   "
    w = len(text) * 4 * scale
    img = Image.new("RGB", (w, 5 * scale), bg)
    px = img.load()
    for i, ch in enumerate(text):
        bits = FONT.get(ch, FONT[" "])
        for b, v in enumerate(bits):
            if v == "1":
                x0, y0 = (i * 4 + b % 3) * scale, (b // 3) * scale
                for dx in range(scale):
                    for dy in range(scale):
                        px[x0 + dx, y0 + dy] = color
    return img


# ── 10x10 sprites, scaled x5 → 50x50 ─────────────────────────────────────
SPRITES = {
    "cat": ["..........", ".X......X.", ".XX....XX.", ".XXXXXXXX.", ".X.XXXX.X.", ".XXXXXXXX.", ".XXX..XXX.", "..XXXXXX..", "...X..X...", ".........."],
    "ghost": ["...XXXX...", "..XXXXXX..", ".XXXXXXXX.", ".XX.XX.XX.", ".XX.XX.XX.", ".XXXXXXXX.", ".XXXXXXXX.", ".XXXXXXXX.", ".X.XX.XX.X", ".........."],
    "mushroom": ["...XXXX...", ".XXXXXXXX.", "XX.XXXX.XX", "XXXXXXXXXX", "XXX.XX.XXX", "..XXXXXX..", "...X..X...", "...XXXX...", "...XXXX...", ".........."],
    "invader": ["..X....X..", "...X..X...", "..XXXXXX..", ".XX.XX.XX.", "XXXXXXXXXX", "X.XXXXXX.X", "X.X....X.X", "...XX.XX..", "..........", ".........."],
    "tree": ["....XX....", "...XXXX...", "..XXXXXX..", ".XXXXXXXX.", "..XXXXXX..", ".XXXXXXXX.", "XXXXXXXXXX", "....XX....", "....XX....", "..XXXXXX.."],
    "moon": ["...XXXX...", "..XXX.....", ".XXX......", ".XX.......", ".XX.......", ".XX.......", ".XXX......", "..XXX.....", "...XXXX...", ".........."],
    "fish": ["..........", "....XXX...", "X..XXXXX..", "XXXXX.XXX.", "XXXXXXXXXX", "XXXXXXXXX.", "X..XXXXX..", "....XXX...", "..........", ".........."],
    "key": ["..........", ".XXX......", "X...X.....", "X...XXXXXX", "X...X..X.X", ".XXX...X..", "..........", "..........", "..........", ".........."],
    "robot": ["....X.....", "..XXXXXX..", "..X.XX.X..", "..XXXXXX..", "..X....X..", "XXXXXXXXXX", "X.XXXXXX.X", "..XXXXXX..", "..X....X..", "..XX...XX."],
    "planet": ["..........", "...XXXX...", "..XXXXXX..", "XXXXXXXXXX", ".XXXXXXXX.", "XXXXXXXXXX", "..XXXXXX..", "...XXXX...", "..........", ".........."],
    "skullfree_bird": ["..........", "...XX.....", "..XXXX....", ".XXXXXXX..", "XX.XXXXXXX", "...XXXXX..", "....XXX...", "....X.X...", "..........", ".........."],
    "eye": ["..........", "...XXXX...", ".XX....XX.", "X..XXXX..X", "X.XX..XX.X", "X.XX..XX.X", "X..XXXX..X", ".XX....XX.", "...XXXX...", ".........."],
    "cup": ["..........", ".X..X..X..", "..X..X..X.", "..........", "XXXXXXXX..", "X......XXX", "X......X.X", "X......XXX", ".X....X...", "..XXXX...."],
    "house": ["....XX....", "...XXXX...", "..XXXXXX..", ".XXXXXXXX.", "XXXXXXXXXX", ".X......X.", ".X.XX.X.X.", ".X.XX...X.", ".X.XX...X.", ".XXXXXXXX."],
    "note": ["......XXXX", "....XXXX.X", "....X....X", "....X....X", "....X....X", "....X..XXX", "..XXX.XXXX", ".XXXX.XXX.", ".XXX......", ".........."],
    "leaf": ["........XX", "......XXXX", "....XXXXXX", "...XXXXX.X", "..XXXXX.XX", "..XXXX.XXX", ".XXX.XXXX.", ".X.XXXX...", "X.........", ".........."],
}

PALETTE_BG = [(0, 0, 0), (10, 18, 6), (20, 12, 30), (30, 10, 10), (5, 20, 30), (25, 25, 25)]
COLORS = [(109, 174, 66), (255, 255, 255), (255, 204, 0), (255, 90, 60), (90, 200, 255), (220, 120, 255),
          (255, 150, 200), (160, 255, 120), (255, 255, 120), (120, 160, 255)]


def sprite_img(name, fg, bg, eyes_closed=False):
    img = Image.new("RGB", (50, 50), bg)
    d = ImageDraw.Draw(img)
    rows = SPRITES[name]
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            on = c == "X"
            if eyes_closed and name in ("ghost", "cat", "invader", "robot") and not on and 2 <= y <= 4 and 1 <= x <= 8:
                on = True  # blink: fill the eye holes
            if on:
                d.rectangle([x * 5, y * 5, x * 5 + 4, y * 5 + 4], fill=fg)
    return img


def identicon(rng, fg, bg):
    img = Image.new("RGB", (50, 50), bg)
    d = ImageDraw.Draw(img)
    for y in range(5):
        for x in range(3):
            if rng.random() < 0.5:
                for xx in {x, 4 - x}:
                    d.rectangle([xx * 10, y * 10, xx * 10 + 9, y * 10 + 9], fill=fg)
    return img


def dithered(rng, fg, bg, letter):
    img = Image.new("L", (50, 50))
    px = img.load()
    cx, cy = rng.randint(10, 40), rng.randint(10, 40)
    for y in range(50):
        for x in range(50):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** .5
            px[x, y] = max(0, min(255, int(255 - dist * 6 + rng.randint(-30, 30))))
    one = img.convert("1")  # Floyd–Steinberg dither, very 1998
    out = Image.new("RGB", (50, 50), bg)
    out.paste(Image.new("RGB", (50, 50), fg), mask=one)
    return out


def save_gif(frames, path, duration=400):
    frames = [f.convert("P", palette=Image.ADAPTIVE, colors=16) for f in frames]
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=duration, loop=0, optimize=True)


_SEQ = None
_used = [0]


def next_sprite():
    global _SEQ
    if _SEQ is None:
        _SEQ = list(SPRITES)
        random.Random("kyberia").shuffle(_SEQ)
    sp = _SEQ[_used[0] % len(_SEQ)]
    _used[0] += 1
    return sp


def make_user_icon(user, i):
    rng = random.Random(user)
    fg = COLORS[rng.randrange(len(COLORS))]
    bg = PALETTE_BG[rng.randrange(len(PALETTE_BG))]
    kind = i % 6
    names = list(SPRITES)
    path = os.path.join(UDIR, slug(user) + ".gif")
    if kind == 0:  # blinking sprite
        sp = next_sprite()
        save_gif([sprite_img(sp, fg, bg)] * 6 + [sprite_img(sp, fg, bg, eyes_closed=True)], path, 250)
    elif kind == 1:  # static sprite
        save_gif([sprite_img(next_sprite(), fg, bg)], path)
    elif kind == 2:  # identicon
        save_gif([identicon(rng, fg, bg)], path)
    elif kind == 3:  # scrolling login marquee over a sprite
        base = sprite_img(next_sprite(), tuple(c // 3 for c in fg), bg)
        strip = text_strip(user, fg, bg, scale=2)
        frames = []
        for off in range(0, strip.width - 50 + 1 if strip.width > 50 else 1, 4):
            f = base.copy()
            f.paste(strip.crop((off, 0, off + 50, 10)), (0, 38))
            frames.append(f)
        save_gif(frames or [base], path, 120)
    elif kind == 4:  # dithered "photo" with initial
        save_gif([dithered(rng, fg, bg, user[0])], path)
    else:  # colour-cycling sprite
        sp = next_sprite()
        save_gif([sprite_img(sp, COLORS[(i + k) % len(COLORS)], bg) for k in range(6)], path, 300)
    return path


# ── node images for stories on main (120x150, dithered illustrations) ────
def scene(i, title):
    rng = random.Random(title)
    w, h = 120, 150
    img = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(img)
    t = title.lower()
    if "strom" in t or "zelená stena" in t or "záhrada" in t:
        for k in range(7):
            x = rng.randint(5, 110)
            d.ellipse([x - 22, 30 + k * 6, x + 22, 80 + k * 6], fill=rng.randint(90, 200))
            d.rectangle([x - 3, 80 + k * 6, x + 3, 150], fill=60)
    elif "session" in t or "hudb" in t:
        for k in range(10):
            hh = rng.randint(20, 120)
            d.rectangle([6 + k * 11, h - hh, 14 + k * 11, h], fill=120 + k * 12)
    elif "zelená" in t:
        for r in range(70, 0, -10):
            d.ellipse([60 - r, 75 - r, 60 + r, 75 + r], fill=255 - r * 3)
    elif "električk" in t:
        d.rectangle([0, 100, 120, 104], fill=200)
        d.rectangle([0, 115, 120, 119], fill=200)
        d.rectangle([15, 55, 105, 98], fill=170)
        for k in range(4):
            d.rectangle([22 + k * 21, 63, 36 + k * 21, 80], fill=40)
    elif "účelom" in t or "čítame" in t or "wittgenstein" in t:
        for k in range(6):
            d.rectangle([10 + k * 17, 30 + (k % 2) * 8, 24 + k * 17, 140], fill=90 + k * 25)
    elif "self-hosting" in t or "x230" in t:
        for k in range(6):
            d.rectangle([20, 15 + k * 21, 100, 31 + k * 21], fill=110 + k * 20)
            d.rectangle([28, 21 + k * 21, 34, 25 + k * 21], fill=255)
    elif "atkinson" in t:
        d.text((18, 40), "Aa", fill=255, font_size=60) if hasattr(d, "text") else None
    elif "langoš" in t:
        d.ellipse([15, 35, 105, 125], fill=200)
        d.ellipse([40, 60, 80, 100], fill=150)
    else:  # hmla, fog
        for y in range(h):
            d.line([0, y, w, y], fill=int(80 + 120 * (1 - abs(y - 75) / 75)))
    noise = Image.effect_noise((w, h), 40)
    img = Image.blend(img, noise, 0.18)
    one = img.convert("1")
    green, black = (109, 174, 66), (0, 0, 0)
    tints = [green, (255, 255, 255), (200, 220, 180)]
    out = Image.new("RGB", (w, h), black)
    out.paste(Image.new("RGB", (w, h), tints[i % len(tints)]), mask=one)
    path = os.path.join(NDIR, f"main{i}.gif")
    save_gif([out], path)
    return path


if __name__ == "__main__":
    for i, u in enumerate(USERS):
        make_user_icon(u, i)
    for j, u in enumerate(["slobo", "ozvena", "lúč"]):
        make_user_icon(u, 30 + j)
    for i, row in enumerate(MAIN):
        scene(i, row[0])
    print("icons:", len(os.listdir(UDIR)), "node images:", len(os.listdir(NDIR)))
