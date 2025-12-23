from PIL import Image
import random


def get_zoomed_logo(path, zoom_level):
    img = Image.open(path).convert("RGBA")

    # Add white background
    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    img = Image.alpha_composite(white_bg, img)

    width, height = img.size

    crop_w = width // zoom_level
    crop_h = height // zoom_level

    max_x = width - crop_w
    max_y = height - crop_h

    x = random.randint(0, max_x)
    y = random.randint(0, max_y)

    cropped = img.crop((x, y, x + crop_w, y + crop_h))
    return cropped.resize((400, 400), Image.LANCZOS)
