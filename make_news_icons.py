"""Generate category icons for the news grid."""
from PIL import Image, ImageDraw, ImageFont
import math, os

OUT = "images/pubpic"
W, H = 400, 220

def font(size, bold=False):
    path = "/System/Library/Fonts/Helvetica.ttc"
    try:
        return ImageFont.truetype(path, size, index=1 if bold else 0)
    except Exception:
        return ImageFont.load_default()

def gradient(d, top, bot, w, h):
    for i in range(h):
        t = i / h
        r = int(top[0] + (bot[0]-top[0])*t)
        g = int(top[1] + (bot[1]-top[1])*t)
        b = int(top[2] + (bot[2]-top[2])*t)
        d.line([(0,i),(w,i)], fill=(r,g,b))

# ── Conference ─────────────────────────────────────────────────────────────────
img = Image.new("RGB", (W, H))
d   = ImageDraw.Draw(img)
gradient(d, (41,128,185), (21,67,96), W, H)

cx, cy = W//2, H//2 - 18

# podium
d.rectangle([cx-50, cy+20, cx+50, cy+55], fill="#D5E8F3", outline="#AED6F1", width=2)
d.rectangle([cx-35, cy+5,  cx+35, cy+25], fill="#AED6F1", outline="#85C1E9", width=2)
# microphone stand
d.rectangle([cx-4, cy-45, cx+4, cy+5], fill="#FFFFFF")
# microphone head
d.ellipse([cx-16, cy-75, cx+16, cy-42], fill="#FFFFFF", outline="#AED6F1", width=2)
# microphone grille lines
for yy in range(cy-68, cy-48, 8):
    d.line([cx-14, yy, cx+14, yy], fill="#AED6F1", width=1)
# stand base
d.line([cx-22, cy+5, cx+22, cy+5], fill="#FFFFFF", width=3)

# small figures at podium bottom
for i, fx in enumerate([cx-80, cx-45, cx+45, cx+80]):
    d.ellipse([fx-8, cy+25, fx+8, cy+41], fill="#5DADE2")
    d.line([fx, cy+41, fx, cy+52], fill="#5DADE2", width=3)

bf  = font(18, bold=True)
sf  = font(12)
lbl = "Conference"
d.text(((W - d.textlength(lbl, bf))//2, H-48), lbl, font=bf, fill="#FFFFFF")
sub = "Talks · Presentations · Meetings"
d.text(((W - d.textlength(sub, sf))//2, H-24), sub, font=sf, fill="#AED6F1")

img.save(f"{OUT}/news_conference.png")
print("news_conference.png")

# ── Project / Funding ──────────────────────────────────────────────────────────
img = Image.new("RGB", (W, H))
d   = ImageDraw.Draw(img)
gradient(d, (39,174,96), (27,79,45), W, H)

cx, cy = W//2, H//2 - 15

# lightbulb body
d.ellipse([cx-38, cy-60, cx+38, cy+20], fill="#F9E79F", outline="#F4D03F", width=2)
# bulb base segments
for k, (y1, y2) in enumerate([(cy+20, cy+30), (cy+30, cy+40), (cy+40, cy+48)]):
    w_seg = 28 - k*4
    d.rectangle([cx-w_seg, y1, cx+w_seg, y2],
                fill="#F4D03F" if k%2==0 else "#D4AC0D", outline="#B7950B", width=1)
# base flat
d.line([cx-20, cy+48, cx+20, cy+48], fill="#B7950B", width=2)

# glow rays
for angle in range(0, 360, 45):
    rad = math.radians(angle)
    x1 = cx + 44*math.cos(rad)
    y1 = cy - 20 + 44*math.sin(rad)
    x2 = cx + 58*math.cos(rad)
    y2 = cy - 20 + 58*math.sin(rad)
    d.line([x1, y1, x2, y2], fill="#F9E79F", width=2)

# filament inside bulb
d.arc([cx-18, cy-35, cx+18, cy+5], 200, 340, fill="#E67E22", width=2)

bf  = font(18, bold=True)
sf  = font(12)
lbl = "Project"
d.text(((W - d.textlength(lbl, bf))//2, H-48), lbl, font=bf, fill="#FFFFFF")
sub = "Funding · Launches · Milestones"
d.text(((W - d.textlength(sub, sf))//2, H-24), sub, font=sf, fill="#A9DFBF")

img.save(f"{OUT}/news_project.png")
print("news_project.png")

# ── Publication ────────────────────────────────────────────────────────────────
img = Image.new("RGB", (W, H))
d   = ImageDraw.Draw(img)
gradient(d, (142,68,173), (74,35,90), W, H)

cx, cy = W//2, H//2 - 10

# open book
bw, bh = 80, 60
# left page
d.polygon([(cx-bw, cy-bh), (cx, cy-bh+8), (cx, cy+bh-8), (cx-bw, cy+bh)],
          fill="#FDFEFE", outline="#D7BDE2", width=2)
# right page
d.polygon([(cx+bw, cy-bh), (cx, cy-bh+8), (cx, cy+bh-8), (cx+bw, cy+bh)],
          fill="#F5EEF8", outline="#D7BDE2", width=2)
# text lines on left page
for ly in range(cy-bh+20, cy+bh-10, 10):
    lw = 50 - abs(ly - cy)//4
    d.line([cx-lw-8, ly, cx-12, ly], fill="#BB8FCE", width=2)
# text lines on right page
for ly in range(cy-bh+20, cy+bh-10, 10):
    lw = 50 - abs(ly - cy)//4
    d.line([cx+12, ly, cx+lw+8, ly], fill="#BB8FCE", width=2)
# spine
d.line([cx, cy-bh+8, cx, cy+bh-8], fill="#7D3C98", width=3)

bf  = font(18, bold=True)
sf  = font(12)
lbl = "Publication"
d.text(((W - d.textlength(lbl, bf))//2, H-48), lbl, font=bf, fill="#FFFFFF")
sub = "New papers · Accepted manuscripts"
d.text(((W - d.textlength(sub, sf))//2, H-24), sub, font=sf, fill="#D7BDE2")

img.save(f"{OUT}/news_publication.png")
print("news_publication.png")

print("\nDone.")
