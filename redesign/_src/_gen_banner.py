"""Animated main banner for v4: a rework of the historical kyberia glitch banner.

Logo = the original node-101 GIF, pasted unmodified (the logo is holy).
Everything else (frame, text layers, glitch) is generated. Needs Pillow.
"""
import os
import random

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1180, 240
BLACK, GREEN, DIM, DIMMER, LIGHT, PALE, WHITE = (0, 0, 0), (109, 174, 66), (47, 74, 31), (29, 46, 19), (140, 207, 90), (190, 232, 150), (255, 255, 255)


def font(names, size):
    for n in names:
        for d in ("C:/Windows/Fonts", "/usr/share/fonts/truetype/dejavu", "/Library/Fonts"):
            p = os.path.join(d, n)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()


SANS = ["tahoma.ttf", "verdana.ttf", "DejaVuSans.ttf"]
BOLD = ["tahomabd.ttf", "verdanab.ttf", "DejaVuSans-Bold.ttf"]
MONO = ["consola.ttf", "cour.ttf", "DejaVuSansMono.ttf"]

FRAGMENTS = [
    "od: kvasar [Odpovedať] 12.10. 20:52", "beriem jedno miesto, platím benzín aj langoš",
    "od: polly [Odpovedať] 11.10. 21:40", "Kyberia session 2026: zostava, miesto, lístky",
    "Re[3]: kde kúpiť dobrý chlieb v BA", "nodeshell:: Compz & Net :: (236 children)",
    "Re[9]: ozvena :: level 10 :: UP", "Ad hominem na úrovni 10. Osobný rekord.",
    "forum:: 101 silence justification arXiv", "Prečo je kyberia zelená?", "čo sa dáva ako kameň, je kameň",
    "dendrites & axones", "000001010006352809184022", "K+ book fook put", "158 NEW Child :: descdnt :: changed",
]


def base_layer(rng):
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    small, mono = font(SANS, 11), font(MONO, 11)
    # faint text columns (the UI underneath)
    for col, x0 in enumerate((170, 430, 700, 930)):
        y = 6
        while y < H - 20:
            frag = rng.choice(FRAGMENTS)
            d.text((x0 + rng.randint(-6, 6), y), frag, fill=rng.choice((DIM, DIMMER, DIM, GREEN)), font=rng.choice((small, mono)))
            y += rng.choice((13, 14, 26))
    # circuit-board frame with angled cut-outs (after the original)
    d.rectangle([0, 0, W - 1, H - 1], outline=GREEN)
    d.line([(0, 168), (290, 168), (330, 196), (W - 260, 196), (W - 230, 176), (W - 1, 176)], fill=GREEN)
    d.line([(160, 0), (160, 168)], fill=DIM)
    d.line([(420, 196), (420, H)], fill=DIM)
    d.line([(W - 330, 0), (W - 330, 22), (W - 1, 22)], fill=DIM)
    d.rectangle([0, 176, 290, 186], fill=(40, 40, 40))
    d.text((W - 320, 4), "mail:", fill=GREEN, font=font(SANS, 14))
    # tagline + the classic answer
    d.text((180, 70), "Something smarter than us", fill=WHITE, font=font(BOLD, 34))
    d.text((180, 110), "is going to emerge", fill=WHITE, font=font(BOLD, 34))
    d.text((W - 300, 60), "I say fook", fill=WHITE, font=font(SANS, 18))
    d.text((W - 300, 84), "ako sa máš, kyberia.sk?", fill=GREEN, font=font(SANS, 14))
    # the logo, unmodified
    logo = Image.open(os.path.join(ROOT, "img", "kyberia.gif")).convert("RGB")
    img.paste(logo, (18, 8))
    return img


def glitch(base, rng, strength):
    img = base.copy()
    d = ImageDraw.Draw(img)
    for _ in range(int(14 * strength)):  # horizontal tears: shift a band of the image sideways
        y = rng.randint(4, H - 30)
        h = rng.randint(2, 18)
        x0 = rng.randint(150, W - 300)
        band = base.crop((x0, y, min(W, x0 + rng.randint(120, 520)), y + h))
        img.paste(band, (max(0, x0 + rng.randint(-90, 90)), y))
    for _ in range(int(9 * strength)):  # light-green blocks, the signature of the original
        x = rng.randint(380, W - 240)
        y = rng.randint(10, H - 70)
        w, h = rng.randint(30, 260), rng.randint(6, 46)
        d.rectangle([x, y, x + w, y + h], fill=rng.choice((LIGHT, PALE, GREEN, LIGHT)))
        for yy in range(y, y + h, 3):  # scanline breakup inside the block
            if rng.random() < .35:
                d.line([(x + rng.randint(0, w // 2), yy), (x + w, yy)], fill=BLACK)
    return img


def main():
    rng = random.Random("kyberia v4")
    base = base_layer(rng)
    frames, durations = [], []
    frames.append(base); durations.append(2600)            # clean, readable
    for s in (0.4, 1.0, 1.4, 0.8, 1.2, 0.5):                 # tear
        frames.append(glitch(base, rng, s)); durations.append(90)
    frames.append(base); durations.append(1800)
    for s in (1.1, 0.6, 1.3):
        frames.append(glitch(base, rng, s)); durations.append(80)
    pal = [f.convert("P", palette=Image.ADAPTIVE, colors=16) for f in frames]
    out = os.path.join(ROOT, "img", "banner.gif")
    pal[0].save(out, save_all=True, append_images=pal[1:], duration=durations, loop=0, optimize=True)
    print("banner:", out, os.path.getsize(out) // 1024, "KB")


if __name__ == "__main__":
    main()
