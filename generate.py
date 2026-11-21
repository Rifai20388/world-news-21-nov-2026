#!/usr/bin/env python3
"""Draw the front page for 21 November 2026 and write entry.png.

Front-page newspaper style, 1024x1024, drawn with PIL (stdlib + Pillow).
Run: python3 generate.py  -> writes entry.png next to this file.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 44
PAPER = (248, 244, 232)
INK = (18, 18, 18)
RED = (178, 28, 28)
GREY = (90, 86, 76)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured with the real font."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill=INK, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.28)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x, y, width, weight=2):
    draw.line([(x, y), (x + width, y)], fill=INK, width=weight)
    return y + weight


def tracked(draw, text, x, y, fnt, fill=INK, tracking=3):
    """Draw caps text with letter spacing."""
    cx = x
    for ch in text:
        draw.text((cx, y), ch, font=fnt, fill=fill)
        cx += draw.textlength(ch, font=fnt) + tracking
    return cx


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Outer frame
    d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=4)
    d.rectangle([20, 20, W - 21, H - 21], outline=INK, width=1)

    content_w = W - 2 * MARGIN
    y = 34

    # Masthead
    mast = font(SERIF, 96)
    name = "THE WORLD"
    d.text(((W - d.textlength(name, font=mast)) / 2, y), name, font=mast, fill=INK)
    y += 110
    y = rule(d, MARGIN, y, content_w, 3)
    y += 10

    # Dateline strip
    date_f = font(SANS, 25)
    date_txt = "SATURDAY, 21 NOVEMBER 2026"
    d.text(((W - d.textlength(date_txt, font=date_f)) / 2, y), date_txt,
           font=date_f, fill=INK)
    y += 34
    small = font(SANS_REG, 17)
    sub = "ONE DAY  ·  SIX STORIES  ·  THE NEWS THAT MADE SATURDAY"
    d.text(((W - d.textlength(sub, font=small)) / 2, y), sub,
           font=small, fill=GREY)
    y += 26
    y = rule(d, MARGIN, y, content_w, 3)
    y += 16

    # ---- TOP STORY ----
    kick = font(SANS, 21)
    tracked(d, "WAR IN EUROPE", MARGIN, y, kick, fill=RED, tracking=4)
    y += 28
    head = font(SERIF, 58)
    d.text((MARGIN, y), "RUSSIA'S MISSILES", font=head, fill=INK)
    y += 62
    d.text((MARGIN, y), "LAND IN POLAND", font=head, fill=INK)
    y += 64
    deck = font(SERIF_REG, 25)
    deck_txt = ("Moscow fires more than 400 drones and 110 missiles at Ukraine — "
                "eight killed in Kyiv — as a Kh-101 cruise missile crashes into "
                "Polish farmland beside allied drills. PM Tusk calls it “an "
                "intentional provocation”; NATO calls it a grave violation.")
    y = draw_lines(d, wrap(d, deck_txt, deck, content_w), MARGIN, y, deck)
    y += 8
    y = rule(d, MARGIN, y, content_w, 2)
    y += 16

    # ---- ROW 2: two columns ----
    col_w = (content_w - 28) // 2
    x2 = MARGIN + col_w + 28
    y_row2 = y
    y_end = y_row2

    h2 = font(SANS, 27)
    b2 = font(SERIF_REG, 21)

    # Left: markets
    yy = draw_lines(d, wrap(d, "AI ROUT ON WALL STREET", h2, col_w), MARGIN,
                    y_row2, h2, leading=32)
    yy += 4
    yy = draw_lines(d, wrap(d, "The S&P 500 and the Dow slide into correction "
                               "as the AI sell-off deepens; the Nasdaq wipes "
                               "out all its 2026 gains. Anthropic shares slide "
                               "after their record debut.", b2, col_w),
                    MARGIN, yy, b2, leading=27)
    y_end = max(y_end, yy)

    # Right: bitcoin
    yy = draw_lines(d, wrap(d, "BITCOIN CRASHES BELOW $60,000", h2, col_w), x2,
                    y_row2, h2, leading=32)
    yy += 4
    yy = draw_lines(d, wrap(d, "Bitcoin falls to about $55,770 on Saturday, "
                               "down almost 10% on the day, as the crypto rout "
                               "deepens. Fear & Greed: 12 — Extreme Fear.",
                            b2, col_w), x2, yy, b2, leading=27)
    y_end = max(y_end, yy)

    y = y_end + 8
    y = rule(d, MARGIN, y, content_w, 2)
    y += 12

    # ---- ROW 3: three columns ----
    col3_w = (content_w - 56) // 3
    xs = [MARGIN, MARGIN + col3_w + 28, MARGIN + 2 * (col3_w + 28)]
    h3 = font(SANS, 22)
    b3 = font(SERIF_REG, 19)
    stories = [
        ("MISSILES OVER RIYADH",
         "Saudi defences intercept three Houthi ballistic missiles fired at "
         "Riyadh early on Saturday — the second attack on the capital in days."),
        ("AKVAN FADES OVER INDIA",
         "Cyclone Akvan weakens into a low-pressure area over Odisha after "
         "300,000 people were evacuated. Ganjam records 209 mm of rain."),
        ("MATH'S BIGGEST PRIZE — CLAIMED",
         "Anthropic's Levent Alpöge says he and Claude have proved the "
         "Riemann Hypothesis, unsolved since 1859. Not yet verified."),
    ]
    y_end = y
    for (title, body), x in zip(stories, xs):
        yy = draw_lines(d, wrap(d, title, h3, col3_w), x, y, h3, leading=27)
        yy += 4
        yy = draw_lines(d, wrap(d, body, b3, col3_w), x, yy, b3, leading=24)
        y_end = max(y_end, yy)

    y = y_end + 10
    y = rule(d, MARGIN, y, content_w, 3)
    y += 10

    # Footer
    foot = font(SANS_REG, 16)
    foot_txt = "THE WORLD — SATURDAY, 21 NOVEMBER 2026"
    d.text(((W - d.textlength(foot_txt, font=foot)) / 2, y), foot_txt,
           font=foot, fill=INK)
    y += 24
    src = font(SANS_REG, 13)
    src_txt = "Sources: AP · BBC · Reuters · The Guardian · Financial Times · Finnhub"
    d.text(((W - d.textlength(src_txt, font=src)) / 2, y), src_txt,
           font=src, fill=GREY)

    img.save("entry.png", "PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
