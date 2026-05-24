"""Generate refined geometric header images for the six research lines."""
from PIL import Image, ImageDraw
import math

PURPLE = (123, 50, 165)
ORANGE = (242, 158, 0)
WHITE  = (255, 255, 255)

# Draw at 2× then downscale for smooth edges
SCALE  = 2
W, H   = 800, 150
WS, HS = W * SCALE, H * SCALE


def canvas():
    return Image.new("RGBA", (WS, HS), (*WHITE, 255))


def save(img, name):
    out = img.resize((W, H), Image.LANCZOS).convert("RGB")
    path = f"images/respic/{name}.png"
    out.save(path)
    print(f"Saved {path}  ({W}×{H})")


# ── 1. Empowerment Narratives ──────────────────────────────────────────────
# More chevrons (13) spread evenly across full width
img = canvas(); d = ImageDraw.Draw(img)
n = 13
xs = [int(WS * (i + 1) / (n + 1)) for i in range(n)]
base_size = int(HS * 0.22)
for i, x in enumerate(xs):
    frac = (i % 7) / 6          # repeat the rising pattern across groups
    size = int(base_size + HS * 0.42 * frac)
    color = PURPLE if i % 2 == 0 else ORANGE
    lw = 7 * SCALE
    cy = HS // 2 + int(HS * 0.04)
    pts = [
        (x - size // 2, cy + size // 3),
        (x,             cy - size // 2),
        (x + size // 2, cy + size // 3),
    ]
    d.line([pts[0], pts[1]], fill=(*color, 240), width=lw)
    d.line([pts[1], pts[2]], fill=(*color, 240), width=lw)
save(img, "res_narratives")


# ── 2. Intergroup Interactions ─────────────────────────────────────────────
# Two clusters spread to edges, with more bridging nodes in between
img = canvas(); d = ImageDraw.Draw(img)
c1 = [(int(WS*f[0]), int(HS*f[1])) for f in
      [(0.05, 0.35), (0.12, 0.70), (0.21, 0.48), (0.14, 0.15)]]
c2 = [(int(WS*f[0]), int(HS*f[1])) for f in
      [(0.95, 0.35), (0.88, 0.70), (0.79, 0.48), (0.86, 0.15)]]
br = [(int(WS*0.38), int(HS*0.32)), (int(WS*0.50), int(HS*0.68)),
      (int(WS*0.62), int(HS*0.32))]

edges1 = [(0,1),(1,2),(2,0),(0,3),(3,2)]
edges2 = [(0,1),(1,2),(2,0),(0,3),(3,2)]
cross  = [(c1[2], br[0]), (br[0], br[1]), (br[1], br[2]), (br[2], c2[2]),
          (c1[0], br[0]), (c2[0], br[2]), (br[0], br[2])]

for a, b in edges1:
    d.line([c1[a], c1[b]], fill=(*PURPLE, 80), width=3*SCALE)
for a, b in edges2:
    d.line([c2[a], c2[b]], fill=(*ORANGE, 80), width=3*SCALE)
mid = (PURPLE[0]//2 + ORANGE[0]//2,
       PURPLE[1]//2 + ORANGE[1]//2,
       PURPLE[2]//2 + ORANGE[2]//2)
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
# Parallel horizontal bands — one band cut short and highlighted differently
img = canvas(); d = ImageDraw.Draw(img)
n_bars = 7
pad_y  = int(HS * 0.10)
bar_h  = (HS - 2 * pad_y) // n_bars
gap    =  4 * SCALE
for i in range(n_bars):
    y1 = pad_y + i * bar_h
    y2 = y1 + bar_h - gap
    if i == 2:
        x1 = int(WS * 0.20)
        x2 = int(WS * 0.60)
        d.rectangle([x1, y1, x2, y2], fill=(*ORANGE, 230))
        for xm in (x1, x2):
            d.line([(xm, y1), (xm, y2)], fill=(*WHITE, 255), width=5*SCALE)
    else:
        x1 = int(WS * 0.04)
        x2 = int(WS * 0.96)
        d.rectangle([x1, y1, x2, y2], fill=(*PURPLE, 190))
save(img, "res_discrimination")


# ── 4. Emotions ────────────────────────────────────────────────────────────
# Three sets of concentric ellipses tiled across full width
img = canvas(); d = ImageDraw.Draw(img)
n_rings  = 5
cx_list  = [WS // 6, WS // 2, 5 * WS // 6]
rx_max   = WS // 6                    # reaches neighbour's centre
ry_max   = HS // 2 - 4 * SCALE       # fills height
for cx in cx_list:
    cy = HS // 2
    for i in range(n_rings, 0, -1):
        rx = i * rx_max // n_rings
        ry = i * ry_max // n_rings
        color = PURPLE if i % 2 == 0 else ORANGE
        lw = (n_rings - i + 2) * SCALE
        d.ellipse([cx-rx, cy-ry, cx+rx, cy+ry], outline=(*color, 220), width=lw)
    r = 10 * SCALE
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(*PURPLE, 255))
save(img, "res_emotions")


# ── 5. Social Rituals ──────────────────────────────────────────────────────
# Three starburst patterns tiled across full width
img = canvas(); d = ImageDraw.Draw(img)
cx_list = [WS // 6, WS // 2, 5 * WS // 6]
n       = 18
r_in    = int(HS * 0.10)
r_out   = int(HS * 0.42)
for cx in cx_list:
    cy = HS // 2
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
    rc = 13 * SCALE
    d.ellipse([cx-rc, cy-rc, cx+rc, cy+rc], fill=(*PURPLE, 255))
save(img, "res_rituals")


# ── 6. Collective Memory ───────────────────────────────────────────────────
# Stacked shrinking rectangles — geological strata / layers of history
img = canvas(); d = ImageDraw.Draw(img)
n      = 7
pad_y  = int(HS * 0.08)
band_h = (HS - 2 * pad_y) // n
gap    = 5 * SCALE
for i in range(n):
    shrink = i * int(WS * 0.055)
    x1 = shrink
    x2 = WS - shrink
    y1 = pad_y + i * band_h
    y2 = y1 + band_h - gap
    alpha = 230 - i * 15
    color = PURPLE if i % 2 == 0 else ORANGE
    d.rectangle([x1, y1, x2, y2], fill=(*color, alpha))
save(img, "res_memory")


print("\nAll 6 research images done.")
