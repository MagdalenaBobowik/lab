"""Generate thematic icon images for each highlighted publication."""
from PIL import Image, ImageDraw, ImageFont
import math, os

OUT = "images/pubpic"
W, H = 400, 260

def font(size, bold=False):
    path = "/System/Library/Fonts/Helvetica.ttc"
    try:
        return ImageFont.truetype(path, size, index=1 if bold else 0)
    except Exception:
        return ImageFont.load_default()

def wrap(text, fnt, max_w, draw):
    words = text.split()
    lines, line = [], []
    for w in words:
        test = " ".join(line + [w])
        if draw.textlength(test, font=fnt) <= max_w:
            line.append(w)
        else:
            if line:
                lines.append(" ".join(line))
            line = [w]
    if line:
        lines.append(" ".join(line))
    return lines

def text_block(draw, lines, fnt, x, y, fill, line_h):
    for l in lines:
        w = draw.textlength(l, font=fnt)
        draw.text((x - w / 2, y), l, font=fnt, fill=fill)
        y += line_h
    return y

def draw_figures(draw, cx, cy, n, r, color, size=18):
    """Draw n stick-figure heads arranged in a circle."""
    for i in range(n):
        angle = 2 * math.pi * i / n - math.pi / 2
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        draw.ellipse([x - size/2, y - size/2, x + size/2, y + size/2], fill=color)

# ── 1. Moral Exemplars ─────────────────────────────────────────────────────────
img = Image.new("RGB", (W, H), "#FFF8F0")
d = ImageDraw.Draw(img)
# warm gradient background via rectangles
for i in range(H):
    t = i / H
    r = int(255 * (1 - t * 0.15))
    g = int(240 * (1 - t * 0.12))
    b = int(220 * (1 - t * 0.05))
    d.line([(0, i), (W, i)], fill=(r, g, b))

# central glowing star / hero figure
cx, cy = W // 2, H // 2 - 15
for ring in range(6, 0, -1):
    alpha = int(255 * (0.08 * ring))
    r = ring * 18
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(255, 180, 60, alpha))

# hero circle
d.ellipse([cx-22, cy-22, cx+22, cy+22], fill="#F4A325")
d.ellipse([cx-16, cy-16, cx+16, cy+16], fill="#FFFFFF")

# surrounding group of people (smaller circles)
draw_figures(d, cx, cy, 8, 65, "#C0392B", 10)

# title label
lf = font(13, bold=True)
sf = font(11)
title_lines = wrap("Moral Exemplars & Self-Transcendent Emotions", lf, W - 40, d)
y = H - 55
text_block(d, title_lines, lf, W//2, y, "#5C3317", 17)
d.text((W//2 - d.textlength("Group Processes & Intergroup Relations, 2024", sf)//2, H-22),
       "Group Processes & Intergroup Relations, 2024", font=sf, fill="#888")

img.save(f"{OUT}/pub_moral_exemplars.png")
print("1. pub_moral_exemplars.png")

# ── 2. Hidden Side of Contact ──────────────────────────────────────────────────
img = Image.new("RGB", (W, H), "#EEF4FB")
d = ImageDraw.Draw(img)
for i in range(H):
    t = i / H
    r = int(220 + t * 10)
    g = int(232 + t * 5)
    b = int(248 - t * 20)
    d.line([(0, i), (W, i)], fill=(r, g, b))

# iceberg: visible part above, hidden below a waterline
waterline = H // 2 - 10
# water fill
d.rectangle([0, waterline, W, H], fill="#2471A3")
# iceberg tip (above water)
tip_pts = [(W//2, 40), (W//2-55, waterline), (W//2+55, waterline)]
d.polygon(tip_pts, fill="#AED6F1", outline="#1A5276")
# hidden bulk (below water, larger, slightly transparent-looking)
bulk_pts = [(W//2-55, waterline), (W//2+55, waterline),
            (W//2+100, H-20), (W//2-100, H-20)]
d.polygon(bulk_pts, fill="#1A5276")
# dashed waterline label
for x in range(20, W-20, 18):
    d.line([(x, waterline), (x+10, waterline)], fill="#FFFFFF", width=1)

lf = font(13, bold=True)
sf = font(11)
title_lines = wrap("The Hidden Side of Intergroup Contact", lf, W - 40, d)
y = H - 55
text_block(d, title_lines, lf, W//2, y, "#FFFFFF", 17)
d.text((W//2 - d.textlength("Group Processes & Intergroup Relations, 2024", sf)//2, H-22),
       "Group Processes & Intergroup Relations, 2024", font=sf, fill="#AED6F1")

img.save(f"{OUT}/pub_hidden_contact.png")
print("2. pub_hidden_contact.png")

# ── 3. When They Cry ───────────────────────────────────────────────────────────
img = Image.new("RGB", (W, H), "#EBF5FB")
d = ImageDraw.Draw(img)
for i in range(H):
    t = i / H
    r = int(220 - t * 20)
    g = int(235 - t * 15)
    b = int(248 - t * 10)
    d.line([(0, i), (W, i)], fill=(r, g, b))

# face circle
cx, cy = W // 2, H // 2 - 20
d.ellipse([cx-50, cy-50, cx+50, cy+50], fill="#F0D9B5", outline="#C9A96E", width=2)
# eyes (slightly sad)
d.ellipse([cx-20, cy-15, cx-8, cy-3], fill="#4A4A4A")
d.ellipse([cx+8, cy-15, cx+20, cy-3], fill="#4A4A4A")
# teardrop left
d.ellipse([cx-17, cy+2, cx-11, cy+10], fill="#5DADE2")
d.polygon([(cx-14, cy+2), (cx-11, cy+18), (cx-17, cy+18)], fill="#5DADE2")
# teardrop right
d.ellipse([cx+11, cy+2, cx+17, cy+10], fill="#5DADE2")
d.polygon([(cx+14, cy+2), (cx+17, cy+18), (cx+11, cy+18)], fill="#5DADE2")
# mouth (soft sad curve)
d.arc([cx-15, cy+18, cx+15, cy+35], 200, 340, fill="#C9A96E", width=2)

# two hands reaching from sides
d.ellipse([cx-90, cy-5, cx-65, cy+20], fill="#F0D9B5", outline="#C9A96E", width=1)
d.ellipse([cx+65, cy-5, cx+90, cy+20], fill="#F0D9B5", outline="#C9A96E", width=1)

lf = font(13, bold=True)
sf = font(11)
title_lines = wrap("Tears Facilitate Helping Toward Disadvantaged Groups", lf, W - 40, d)
y = H - 55
text_block(d, title_lines, lf, W//2, y, "#1A5276", 17)
d.text((W//2 - d.textlength("Emotion, 2023", sf)//2, H-22),
       "Emotion, 2023", font=sf, fill="#5D6D7E")

img.save(f"{OUT}/pub_when_they_cry.png")
print("3. pub_when_they_cry.png")

# ── 4. Ukrainian Refugees / European Identity ──────────────────────────────────
img = Image.new("RGB", (W, H), "#003087")
d = ImageDraw.Draw(img)
for i in range(H):
    t = i / H
    r = int(0 + t * 20)
    g = int(48 + t * 30)
    b = int(135 + t * 40)
    d.line([(0, i), (W, i)], fill=(r, g, b))

# EU stars ring
cx, cy = W // 2, H // 2 - 10
for i in range(12):
    angle = 2 * math.pi * i / 12 - math.pi / 2
    sx = cx + 70 * math.cos(angle)
    sy = cy + 70 * math.sin(angle)
    # simple 5-pointed star as small polygon
    pts = []
    for j in range(5):
        a_out = 2 * math.pi * j / 5 - math.pi / 2
        a_in  = a_out + math.pi / 5
        pts.extend([sx + 7*math.cos(a_out), sy + 7*math.sin(a_out)])
        pts.extend([sx + 3*math.cos(a_in),  sy + 3*math.sin(a_in)])
    d.polygon(pts, fill="#FFD700")

# heart of people in the centre
draw_figures(d, cx, cy, 6, 28, "#FFFFFF", 12)
d.ellipse([cx-8, cy-8, cx+8, cy+8], fill="#FFD700")

lf = font(13, bold=True)
sf = font(11)
title_lines = wrap("Solidarity with Ukrainian Refugees & European Identity", lf, W - 40, d)
y = H - 55
text_block(d, title_lines, lf, W//2, y, "#FFFFFF", 17)
d.text((W//2 - d.textlength("Journal of Community & Applied Social Psychology, 2023", sf)//2, H-22),
       "Journal of Community & Applied Social Psychology, 2023", font=sf, fill="#AED6F1")

img.save(f"{OUT}/pub_ukrainian_refugees.png")
print("4. pub_ukrainian_refugees.png")

# ── 5. United in Diversity / Social Networks ───────────────────────────────────
img = Image.new("RGB", (W, H), "#F9F9F9")
d = ImageDraw.Draw(img)
for i in range(H):
    t = i / H
    c = int(249 - t * 20)
    d.line([(0, i), (W, i)], fill=(c, c, c))

node_colors = ["#E74C3C","#3498DB","#2ECC71","#F39C12","#9B59B6","#1ABC9C","#E67E22","#34495E"]
nodes = [
    (200,  90), (120, 130), (280, 130), (90,  190),
    (160, 190), (240, 190), (310, 190), (200, 230),
]
edges = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(3,7),(4,7),(5,7),(6,7),(0,4),(0,5),(1,2)]
for a, b in edges:
    d.line([nodes[a], nodes[b]], fill="#CCCCCC", width=2)
for idx, (nx, ny) in enumerate(nodes):
    c = node_colors[idx]
    r = 18
    d.ellipse([nx-r, ny-r, nx+r, ny+r], fill=c)
    d.ellipse([nx-r+2, ny-r+2, nx+r-2, ny+r-2], outline="#FFFFFF", width=2)

lf = font(13, bold=True)
sf = font(11)
title_lines = wrap("United in Diversity: Social Networks & Outgroup Attitudes", lf, W - 40, d)
y = H - 55
text_block(d, title_lines, lf, W//2, y, "#2C3E50", 17)
d.text((W//2 - d.textlength("Group Processes & Intergroup Relations, 2022", sf)//2, H-22),
       "Group Processes & Intergroup Relations, 2022", font=sf, fill="#7F8C8D")

img.save(f"{OUT}/pub_united_diversity.png")
print("5. pub_united_diversity.png")

# ── 6. Tears Across 41 Countries ──────────────────────────────────────────────
img = Image.new("RGB", (W, H), "#0D2137")
d = ImageDraw.Draw(img)
for i in range(H):
    t = i / H
    r = int(13 + t * 15)
    g = int(33 + t * 20)
    b = int(55 + t * 30)
    d.line([(0, i), (W, i)], fill=(r, g, b))

# globe outline
cx, cy = W // 2, H // 2 - 10
R = 80
d.ellipse([cx-R, cy-R, cx+R, cy+R], outline="#5DADE2", width=2)
# latitude lines
for lat in [-40, -20, 0, 20, 40]:
    r_lat = int(R * math.cos(math.radians(lat)))
    if r_lat > 0:
        d.ellipse([cx-r_lat, cy-8+lat//5, cx+r_lat, cy+8+lat//5],
                  outline="#2E86C1", width=1)
# longitude lines (arcs)
for lon in range(-60, 70, 30):
    pts = []
    for lat_deg in range(-85, 86, 5):
        rad = math.radians(lat_deg)
        x = cx + R * math.sin(math.radians(lon)) * math.cos(rad)
        y = cy - R * math.sin(rad)
        pts.append((x, y))
    for k in range(len(pts)-1):
        d.line([pts[k], pts[k+1]], fill="#2E86C1", width=1)

# teardrops scattered on globe
drops = [(cx-30, cy-20), (cx+20, cy-35), (cx-10, cy+10), (cx+40, cy+15), (cx-50, cy+5)]
for (tx, ty) in drops:
    d.ellipse([tx-5, ty-5, tx+5, ty+5], fill="#5DADE2")
    d.polygon([(tx, ty-5), (tx+5, ty+8), (tx-5, ty+8)], fill="#5DADE2")

# "41" counter
bf = font(22, bold=True)
d.text((cx - d.textlength("41", bf)//2, cy + R + 5), "41", font=bf, fill="#FFD700")
smf = font(10)
d.text((cx - d.textlength("countries", smf)//2, cy + R + 28), "countries", font=smf, fill="#AED6F1")

lf = font(13, bold=True)
sf = font(11)
title_lines = wrap("Tears Evoke Social Support: 41-Country Study", lf, W - 40, d)
y = H - 50
text_block(d, title_lines, lf, W//2, y, "#FFFFFF", 17)
d.text((W//2 - d.textlength("Journal of Experimental Social Psychology, 2021", sf)//2, H-18),
       "Journal of Experimental Social Psychology, 2021", font=sf, fill="#85C1E9")

img.save(f"{OUT}/pub_tears_countries.png")
print("6. pub_tears_countries.png")

print("\nAll done.")
