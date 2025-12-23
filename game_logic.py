from pathlib import Path
import random
from rapidfuzz import process, fuzz

# Base directory (where this file lives)
BASE_DIR = Path(__file__).resolve().parent

# Logos directory (CASE-SENSITIVE)
LOGO_DIR = BASE_DIR / "Logos"

MAX_GUESSES = 4


def get_team_names():
    return [
        f.stem
        for f in LOGO_DIR.iterdir()
        if f.suffix.lower() == ".png"
    ]


def new_game():
    team_names = get_team_names()
    team = random.choice(team_names)

    return {
        "answer": team,
        "logo_path": LOGO_DIR / f"{team}.png",
        "guesses": 0,
        "zoom_level": 4,  # start very zoomed in
        "over": False,
        "won": False
    }


def get_suggestions(user_input, limit=5):
    if not user_input:
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

    # Zoom out after wrong guess
    game["zoom_level"] = max(1, game["zoom_level"] - 1)

    if game["guesses"] >= MAX_GUESSES:
        game["over"] = True

    return False
