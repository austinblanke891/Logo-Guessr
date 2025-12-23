from PIL import Image


def get_zoomed_logo(path, zoom, crop_x, crop_y, size=600):
    img = Image.open(path).convert("RGBA")

    # White background
    bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    img = Image.alpha_composite(bg, img)

    w, h = img.size
    crop_w = int(w / zoom)
    crop_h = int(h / zoom)

    # Constrain crop to safe center zone
    x = int((w - crop_w) * crop_x)
    y = int((h - crop_h) * crop_y)

    cropped = img.crop((x, y, x + crop_w, y + crop_h))

    return cropped.resize((size, size), Image.Resampling.LANCZOS)
