#!/usr/bin/env python3
"""
Generate a branded 1200x630 Open Graph share image (og.png) for a page.

Requires Pillow:   pip3 install pillow

Usage:
    # Blog post -> writes assets/<slug>/og.png
    python3 scripts/make-og-image.py --slug react-con-aws-cognito-para-autenticacion-de-usuario \
        --title "React con AWS Cognito para autenticación de usuario"

    # Home page -> writes assets/og-home.png
    python3 scripts/make-og-image.py --home \
        --title "Software Developer & Software Architect"

The output matches the site's light theme: solid #f7f7f7 background, a left accent bar
(#80abc8), the logo + AJDELGADOS brand top-left, the wrapped title in dark text, and a
subtitle line at the bottom.
"""
import argparse
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow is required. Install it with:  pip3 install pillow")

# Resolve paths relative to the project root (parent of this script's dir)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

W, H = 1200, 630
BG = (247, 247, 247)      # #f7f7f7  (site --light)
HEADING = (51, 51, 51)    # #333     (site --heading)
ACCENT = (128, 171, 200)  # #80abc8

def font(size):
    for c in [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def make(out_path, title, subtitle):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # left accent bar
    d.rectangle([0, 0, 12, H], fill=ACCENT)

    # logo + brand (top-left)
    logo_path = os.path.join(ROOT, "assets", "logo_60x60.png")
    try:
        logo = Image.open(logo_path).convert("RGBA").resize((72, 72))
        img.paste(logo, (70, 70), logo)
    except Exception as e:
        print(f"warning: could not load logo ({e})")
    d.text((160, 88), "AJDELGADOS", font=font(26), fill=HEADING)

    # title (wrapped, centered vertically)
    f_title = font(64)
    lines = wrap(d, title, f_title, W - 140)
    line_h = 78
    y = (H - len(lines) * line_h) // 2 + 20
    for ln in lines:
        d.text((70, y), ln, font=f_title, fill=HEADING)
        y += line_h

    # subtitle (bottom)
    d.text((70, H - 90), subtitle, font=font(30), fill=ACCENT)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, "PNG")
    print(f"wrote {out_path}  ({W}x{H})")

def main():
    ap = argparse.ArgumentParser(description="Generate a 1200x630 OG share image.")
    ap.add_argument("--title", required=True, help="Text rendered on the image")
    ap.add_argument("--slug", help="Post slug -> assets/<slug>/og.png")
    ap.add_argument("--home", action="store_true", help="Home page -> assets/og-home.png")
    ap.add_argument("--subtitle", help="Bottom line (default depends on --home/--slug)")
    args = ap.parse_args()

    if args.home:
        out = os.path.join(ROOT, "assets", "og-home.png")
        subtitle = args.subtitle or "ajdelgados.com"
    elif args.slug:
        out = os.path.join(ROOT, "assets", args.slug, "og.png")
        subtitle = args.subtitle or "Blog · ajdelgados.com"
    else:
        ap.error("provide either --slug <slug> or --home")

    make(out, args.title, subtitle)

if __name__ == "__main__":
    main()
