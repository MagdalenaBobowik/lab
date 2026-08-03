"""Common Futures Research Collective logo — overlapping circles."""
from PIL import Image, ImageDraw, ImageFont, ImageChops

W, H = 980, 200

PURPLE = (123,  50, 165)
ORANGE = (242, 158,   0)
GREY   = (110, 110, 120)

def font(size, bold=False):
    path = "/System/Library/Fonts/Helvetica.ttc"
    try:
        return ImageFont.truetype(path, size, index=1 if bold else 0)
    except Exception:
        return ImageFont.load_default()

# ── Circle geometry ────────────────────────────────────────────────────────────
R   = 82
D   = 108
cx1 = R + 6
cx2 = cx1 + D
cy  = H // 2

b1 = [cx1-R, cy-R, cx1+R, cy+R]
b2 = [cx2-R, cy-R, cx2+R, cy+R]

img = Image.new("RGBA", (W, H), (255, 255, 255, 255))
d   = ImageDraw.Draw(img)

d.ellipse(b1, fill=(*PURPLE, 255))
d.ellipse(b2, fill=(*ORANGE, 255))

mask1 = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask1).ellipse(b1, fill=255)
mask2 = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask2).ellipse(b2, fill=255)
intersection = ImageChops.multiply(mask1, mask2)

white = Image.new("RGBA", (W, H), (255, 255, 255, 255))
img   = Image.composite(white, img, intersection)
d     = ImageDraw.Draw(img)

# ── Text ──────────────────────────────────────────────────────────────────────
tx = cx2 + R + 24
ty = cy - 62

fb   = font(54, bold=True)
fmed = font(20)
fsm  = font(13)

# "Common " purple, "Futures" orange
common_w = d.textlength("Common ", font=fb)
d.text((tx, ty),              "Common ",  font=fb, fill=(*PURPLE, 255))
d.text((tx + common_w, ty),   "Futures",  font=fb, fill=(*ORANGE, 255))

# "Research Collective" in grey below
d.text((tx, ty + 62), "Research Collective", font=fmed, fill=(*GREY, 200))

# Divider and institution
ry = ty + 95
d.line([(tx, ry), (tx + 460, ry)], fill=(*GREY, 100), width=1)
d.text((tx, ry + 8), "University of the Basque Country  ·  UPV/EHU",
       font=fsm, fill=(*GREY, 180))

# ── Save ──────────────────────────────────────────────────────────────────────
img.convert("RGB").save("images/logo_idl_white.png")
img.save("images/logo_idl.png")
print("Done.")
