from pathlib import Path
import random
from rapidfuzz import process, fuzz

BASE_DIR = Path(__file__).resolve().parent
LOGO_DIR = BASE_DIR / "Logos"

MAX_GUESSES = 4

# Difficulty tuning
START_ZOOM = 5.0


def get_team_names():
    return sorted([
        f.stem
        for f in LOGO_DIR.iterdir()
        if f.suffix.lower() == ".png"
    ])


def new_game():
    team = random.choice(get_team_names())

    # Deceptive but safe crop
    crop_x = random.uniform(0.15, 0.65)
    crop_y = random.uniform(0.15, 0.65)

    return {
        "answer": team,
        "logo_path": LOGO_DIR / f"{team}.png",
        "guesses": 0,
        "zoom": START_ZOOM,
        "crop_x": crop_x,
        "crop_y": crop_y,
        "over": False,
        "won": False,
    }


def get_suggestions(user_input, limit=5):
    if not user_input.strip():
        return []

    matches = process.extract(
        user_input,
        get_team_names(),
        scorer=fuzz.partial_ratio,
        limit=limit
    )

    return [m[0] for m in matches if m[1] >= 60]


def check_guess(game, guess):
    game["guesses"] += 1

    if guess.lower().strip() == game["answer"].lower():
        game["won"] = True
        game["over"] = True
        return True

    # Progressive zoom-out (harder → easier)
    if game["guesses"] == 1:
        zoom_step = 0.4
    elif game["guesses"] == 2:
        zoom_step = 0.6
    elif game["guesses"] == 3:
        zoom_step = 1.0
    else:
        zoom_step = 1.5

    game["zoom"] = max(1.4, game["zoom"] - zoom_step)

    if game["guesses"] >= MAX_GUESSES:
        game["over"] = True

    return False
