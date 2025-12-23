import streamlit as st
from game_logic import new_game, check_guess, get_suggestions
from image_utils import get_zoomed_logo

st.set_page_config(page_title="Logo Guessr", layout="centered")

st.title("🎯 Logo Guessr")

# Initialize game
if "game" not in st.session_state:
    st.session_state.game = new_game()

game = st.session_state.game

# Center content
_, center, _ = st.columns([1, 2, 1])

with center:
    image = get_zoomed_logo(
        game["logo_path"],
        game["zoom"],
        game["crop_x"],
        game["crop_y"]
    )
    st.image(image)

    if game["over"]:
        if game["won"]:
            st.success(f"🎉 Correct! It was **{game['answer']}**")
        else:
            st.error(f"❌ Out of guesses! It was **{game['answer']}**")

        if st.button("Play Again"):
            st.session_state.game = new_game()
            st.rerun()

    else:
        guess = st.text_input("Enter your guess:")

        suggestions = get_suggestions(guess)

        # STACKED VERTICAL BUTTONS
        for suggestion in suggestions:
            if st.button(suggestion):
                check_guess(game, suggestion)
                st.rerun()

        if st.button("Submit Guess"):
            if guess.strip():
                check_guess(game, guess)
                st.rerun()

        st.caption(f"Guesses remaining: {4 - game['guesses']}")
