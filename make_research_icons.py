"""Generate refined geometric header images for the six research lines.
Portrait format (160×300 px) — displayed as left-floating sidebar next to text.
"""
from PIL import Image, ImageDraw
import math

PURPLE = (123, 50, 165)
ORANGE = (242, 158, 0)
WHITE  = (255, 255, 255)

SCALE  = 2
W, H   = 160, 300
WS, HS = W * SCALE, H * SCALE   # 320 × 600 drawing canvas


def canvas():
    return Image.new("RGBA", (WS, HS), (*WHITE, 255))


def save(img, name):
    out = img.resize((W, H), Image.LANCZOS).convert("RGB")
    path = f"images/respic/{name}.png"
    out.save(path)
    print(f"Saved {path}  ({W}×{H})")


def draw_person(d, cx, cy, sz, color, lw):
    """Outline-style person icon: circle head + shoulder arc."""
    rh  = int(sz * 0.20)
    hcy = int(cy - sz * 0.27)
    d.ellipse([cx-rh, hcy-rh, cx+rh, hcy+rh], outline=(*color, 255), width=lw)
    rb  = int(sz * 0.46)
    bcy = int(cy + sz * 0.18)
    d.arc([cx-rb, bcy-rb, cx+rb, bcy+rb], 200, 340, fill=(*color, 255), width=lw)


# ── 1. Empowerment Narratives ──────────────────────────────────────────────
# Ascending chevrons from bottom to top, growing larger upward
img = canvas(); d = ImageDraw.Draw(img)
n   = 9
lw  = 7 * SCALE
cx  = WS // 2
for i in range(n):
    frac = i / (n - 1)
    y    = int(HS * 0.88 - HS * 0.76 * frac)
    size = int(WS * 0.13 + WS * 0.30 * frac)
    color = PURPLE if i % 2 == 0 else ORANGE
    pts = [
        (cx - size // 2, y + size // 3),
        (cx,             y - size // 2),
        (cx + size // 2, y + size // 3),
    ]
    d.line([pts[0], pts[1]], fill=(*color, 240), width=lw)
    d.line([pts[1], pts[2]], fill=(*color, 240), width=lw)
save(img, "res_narratives")


# ── 2. Intergroup Interactions ─────────────────────────────────────────────
# Two clusters (top purple, bottom orange) connected by bridge nodes
img = canvas(); d = ImageDraw.Draw(img)
c1 = [(int(WS*f[0]), int(HS*f[1])) for f in
      [(0.30, 0.10), (0.70, 0.12), (0.50, 0.22), (0.20, 0.20)]]
c2 = [(int(WS*f[0]), int(HS*f[1])) for f in
      [(0.30, 0.90), (0.70, 0.88), (0.50, 0.78), (0.80, 0.80)]]
br = [(int(WS*0.35), int(HS*0.42)), (int(WS*0.65), int(HS*0.58))]

edges1 = [(0,1),(1,2),(2,0),(0,3),(3,2)]
edges2 = [(0,1),(1,2),(2,0),(0,3),(3,2)]
cross  = [(c1[2], br[0]), (br[0], br[1]), (br[1], c2[2]),
          (c1[0], br[0]), (c2[0], br[1])]
mid    = tuple(PURPLE[i]//2 + ORANGE[i]//2 for i in range(3))

for a, b in edges1:
    d.line([c1[a], c1[b]], fill=(*PURPLE, 80), width=3*SCALE)
for a, b in edges2:
    d.line([c2[a], c2[b]], fill=(*ORANGE, 80), width=3*SCALE)
for p1, p2 in cross:
    d.line([p1, p2], fill=(*mid, 160), width=4*SCALE)

R = 14 * SCALE
for pt in c1:
    d.ellipse([pt[0]-R, pt[1]-R, pt[0]+R, pt[1]+R], fill=(*PURPLE, 255))
for pt in c2:
    d.ellipse([pt[0]-R, pt[1]-R, pt[0]+R, pt[1]+R], fill=(*ORANGE, 255))
for pt in br:
    rb = 11 * SCALE
    d.ellipse([pt[0]-rb, pt[1]-rb, pt[0]+rb, pt[1]+rb], fill=(*mid, 255))
save(img, "res_interactions")


# ── 3. Discrimination & Stigma ─────────────────────────────────────────────
# Top: 3 purple people grouped. Bottom: 1 orange person isolated.
img = canvas(); d = ImageDraw.Draw(img)
sz     = int(WS * 0.38)
lw_p   = 6 * SCALE
gap_g  = int(sz * 0.42)
cx     = WS // 2

# Group of 3 (top half)
grp_cy = int(HS * 0.28)
for j in [-1, 0, 1]:
    draw_person(d, cx + j * gap_g, grp_cy, sz, PURPLE, lw_p)

# Isolated person (bottom half, offset)
iso_cy = int(HS * 0.72)
draw_person(d, cx + int(WS * 0.10), iso_cy, int(sz * 0.90), ORANGE, lw_p)
save(img, "res_discrimination")


# ── 4. Emotions ────────────────────────────────────────────────────────────
# Two sets of concentric ellipses stacked vertically
img = canvas(); d = ImageDraw.Draw(img)
n_rings = 4
cy_list = [HS // 4, 3 * HS // 4]
rx_max  = WS // 2 - 6 * SCALE
ry_max  = HS // 4 - 6 * SCALE
for cy in cy_list:
    for i in range(n_rings, 0, -1):
        rx = i * rx_max // n_rings
        ry = i * ry_max // n_rings
        color = PURPLE if i % 2 == 0 else ORANGE
        lw = (n_rings - i + 2) * SCALE
        d.ellipse([WS//2-rx, cy-ry, WS//2+rx, cy+ry],
                  outline=(*color, 220), width=lw)
    r = 9 * SCALE
    d.ellipse([WS//2-r, cy-r, WS//2+r, cy+r], fill=(*PURPLE, 255))
save(img, "res_emotions")


# ── 5. Social Rituals ──────────────────────────────────────────────────────
# Two starburst patterns stacked vertically
img = canvas(); d = ImageDraw.Draw(img)
cy_list = [HS // 4, 3 * HS // 4]
n       = 18
r_in    = int(WS * 0.07)
r_out   = min(WS // 2 - 8 * SCALE, HS // 4 - 8 * SCALE)
for cy in cy_list:
    cx = WS // 2
    for i in range(n):
        angle = 2 * math.pi * i / n - math.pi / 2
        color = PURPLE if i % 3 != 0 else ORANGE
        xi = cx + int(r_in  * math.cos(angle))
        yi = cy + int(r_in  * math.sin(angle))
        xo = cx + int(r_out * math.cos(angle))
        yo = cy + int(r_out * math.sin(angle))
        d.line([(xi, yi), (xo, yo)], fill=(*color, 170), width=3*SCALE)
        rd = 9 * SCALE
        d.ellipse([xo-rd, yo-rd, xo+rd, yo+rd], fill=(*color, 255))
    rc = 12 * SCALE
    d.ellipse([cx-rc, cy-rc, cx+rc, cy+rc], fill=(*PURPLE, 255))
save(img, "res_rituals")


# ── 6. Collective Memory ───────────────────────────────────────────────────
# Stacked horizontal bands of decreasing width — geological strata
img = canvas(); d = ImageDraw.Draw(img)
n      = 8
pad_y  = int(HS * 0.05)
band_h = (HS - 2 * pad_y) // n
gap    = 5 * SCALE
for i in range(n):
    shrink = i * int(WS * 0.07)
    x1 = shrink
    x2 = WS - shrink
    y1 = pad_y + i * band_h
    y2 = y1 + band_h - gap
    color = PURPLE if i % 2 == 0 else ORANGE
    d.rectangle([x1, y1, x2, y2], fill=(*color, 230 - i * 15))
save(img, "res_memory")


print("\nAll 6 portrait research images done.")
