import os
import random
from rapidfuzz import process, fuzz

LOGO_DIR = "logos"
MAX_GUESSES = 4

def get_team_names():
    return [
        os.path.splitext(f)[0]
        for f in os.listdir(LOGO_DIR)
        if f.lower().endswith(".png")
    ]

TEAM_NAMES = get_team_names()

def new_game():
    team = random.choice(TEAM_NAMES)
    return {
        "answer": team,
        "logo_path": os.path.join(LOGO_DIR, team + ".png"),
        "guesses": 0,
        "zoom_level": 4,  # starts zoomed in
        "over": False,
        "won": False
    }

def get_suggestions(user_input, limit=5):
    if not user_input:
        return []
    matches = process.extract(
        user_input,
        TEAM_NAMES,
        scorer=fuzz.partial_ratio,
        limit=limit
    )
    return [m[0] for m in matches if m[1] > 60]

def check_guess(game, guess):
    game["guesses"] += 1

    if guess.lower() == game["answer"].lower():
        game["won"] = True
        game["over"] = True
        return True

    game["zoom_level"] = max(1, game["zoom_level"] - 1)

    if game["guesses"] >= MAX_GUESSES:
        game["over"] = True

    return False
