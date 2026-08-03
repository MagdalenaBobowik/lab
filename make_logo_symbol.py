"""Generate symbol-only logo (circles, transparent background) for navbar."""
from PIL import Image, ImageDraw, ImageChops

SZ = 120   # square canvas

PURPLE = (123,  50, 165)
ORANGE = (242, 158,   0)

R  = 46
D  = 58
cx1 = 12 + R       # 58
cx2 = cx1 + D      # 116
cy  = SZ // 2      # 60

b1 = [cx1-R, cy-R, cx1+R, cy+R]
b2 = [cx2-R, cy-R, cx2+R, cy+R]

img = Image.new("RGBA", (SZ + D, SZ), (0, 0, 0, 0))   # transparent
d   = ImageDraw.Draw(img)

# Filled circles
d.ellipse(b1, fill=(*PURPLE, 255))
d.ellipse(b2, fill=(*ORANGE, 255))

# Cut out intersection (white → transparent)
mask1 = Image.new("L", img.size, 0)
ImageDraw.Draw(mask1).ellipse(b1, fill=255)
mask2 = Image.new("L", img.size, 0)
ImageDraw.Draw(mask2).ellipse(b2, fill=255)
intersection = ImageChops.multiply(mask1, mask2)

# Set intersection pixels to transparent
r, g, b, a = img.split()
a = ImageChops.subtract(a, intersection)
img = Image.merge("RGBA", (r, g, b, a))

img.save("images/logo_symbol.png")
print(f"Saved images/logo_symbol.png  ({img.size[0]}×{img.size[1]}px)")
