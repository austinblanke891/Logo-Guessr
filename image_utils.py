from PIL import Image
import random

def get_zoomed_logo(path, zoom_level):
    img = Image.open(path).convert("RGBA")

    # white background
    bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    img = Image.alpha_composite(bg, img)

    w, h = img.size
    crop_w = w // zoom_level
    crop_h = h // zoom_level

    x = random.randint(0, w - crop_w)
    y = random.randint(0, h - crop_h)

    cropped = img.crop((x, y, x + crop_w, y + crop_h))
    return cropped.resize((400, 400), Image.LANCZOS)
