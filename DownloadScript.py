import os

LOGO_DIR = r"C:\Users\Austin\OneDrive - Blanke Advisors\Desktop\Logo Guessing Game\Logos"

# Map CURRENT filename (without .png) → DESIRED elegant name
rename_map = {
    # NFL (examples)
    "OAK": "Las Vegas Raiders",
    "Oakland Raiders": "Las Vegas Raiders",
    "Washington Football Team": "Washington Commanders",

    # MLB
    "Angels": "Los Angeles Angels",
    "LA Angels": "Los Angeles Angels",
    "LA Dodgers": "Los Angeles Dodgers",

    # Generic abbreviations / edge cases
    "ATL": "Atlanta Falcons",
    "LAR": "Los Angeles Rams",
    "LAC": "Los Angeles Chargers",
    "NYG": "New York Giants",
    "NYJ": "New York Jets",
}

for filename in os.listdir(LOGO_DIR):
    if not filename.lower().endswith(".png"):
        continue

    name, ext = os.path.splitext(filename)

    if name in rename_map:
        new_name = rename_map[name] + ext
        old_path = os.path.join(LOGO_DIR, filename)
        new_path = os.path.join(LOGO_DIR, new_name)

        if not os.path.exists(new_path):
            print(f"Renaming: {filename} → {new_name}")
            os.rename(old_path, new_path)
        else:
            print(f"Skipping {filename} (target already exists)")

print("Normalization complete.")
