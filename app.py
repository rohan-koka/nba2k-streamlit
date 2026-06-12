import streamlit as st
import random

st.set_page_config(page_title="NBA 2K Rating Guessing Game", layout="centered")

players = [
    {"name": "LeBron James", "team": "Lakers", "position": "SF", "rating": 94},
    {"name": "Stephen Curry", "team": "Warriors", "position": "PG", "rating": 96},
    {"name": "Ja Morant", "team": "Grizzlies", "position": "PG", "rating": 90},
    {"name": "Jayson Tatum", "team": "Celtics", "position": "SF", "rating": 95},
    {"name": "Nikola Jokic", "team": "Nuggets", "position": "C", "rating": 98},
    {"name": "Luka Doncic", "team": "Lakers", "position": "PG", "rating": 97},
    {"name": "Giannis Antetokounmpo", "team": "Bucks", "position": "PF", "rating": 97},
    {"name": "Anthony Edwards", "team": "Timberwolves", "position": "SG", "rating": 93},
    {"name": "Shai Gilgeous-Alexander", "team": "Thunder", "position": "PG", "rating": 97},
    {"name": "Kevin Durant", "team": "Suns", "position": "SF", "rating": 95},
]

# Session state init
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.score = 0
    st.session_state.used = []
    st.session_state.game_over = False
    st.session_state.show_answer = False
    st.session_state.message = ""
    st.session_state.points_earned = None
    available = players[:]
    st.session_state.current = random.choice(available)
    st.session_state.used.append(st.session_state.current)

def get_new_player():
    available = [p for p in players if p not in st.session_state.used]
    if not available:
        st.session_state.used = []
        available = players[:]
    player = random.choice(available)
    st.session_state.used.append(player)
    st.session_state.current = player

def check_guess(guess):
    actual = st.session_state.current["rating"]
    diff = abs(guess - actual)
    if diff == 0:
        points, msg = 10, f"Perfect! {actual} was correct."
    elif diff <= 2:
        points, msg = 7, f"Close! Actual rating: {actual}."
    elif diff <= 5:
        points, msg = 4, f"Not bad. Actual rating: {actual}."
    else:
        points, msg = 0, f"Too far off. Actual rating: {actual}."
    st.session_state.score += points
    st.session_state.points_earned = points
    st.session_state.message = msg
    st.session_state.show_answer = True

def next_round():
    if st.session_state.round >= 10:
        st.session_state.game_over = True
        return
    st.session_state.round += 1
    st.session_state.show_answer = False
    st.session_state.message = ""
    st.session_state.points_earned = None
    get_new_player()

def reset_game():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# UI
st.title("🏀 NBA 2K Rating Guessing Game")

col1, col2 = st.columns(2)
col1.metric("Round", f"{st.session_state.round}/10")
col2.metric("Score", st.session_state.score)

st.divider()

if st.session_state.game_over:
    st.markdown(f"## 🏆 Game Over!")
    st.markdown(f"### Final Score: {st.session_state.score} / 100")
    if st.session_state.score >= 80:
        st.success("Elite 2K knowledge!")
    elif st.session_state.score >= 50:
        st.info("Solid effort!")
    else:
        st.warning("Keep playing to learn the ratings!")
    if st.button("🔄 Play Again"):
        reset_game()
else:
    player = st.session_state.current
    with st.container(border=True):
        st.markdown(f"## {player['name']}")
        st.markdown(f"**Team:** {player['team']}  |  **Position:** {player['position']}")

    if not st.session_state.show_answer:
        with st.form("guess_form"):
            guess = st.number_input("Guess the 2K Overall Rating (1-99):", min_value=1, max_value=99, step=1)
            submitted = st.form_submit_button("Submit Guess")
            if submitted:
                check_guess(guess)
                st.rerun()
    else:
        st.markdown(f"### {st.session_state.message}")
        if st.session_state.points_earned == 10:
            st.success(f"+{st.session_state.points_earned} points 🔥")
        elif st.session_state.points_earned >= 4:
            st.info(f"+{st.session_state.points_earned} points")
        else:
            st.error(f"+0 points")

        if st.button("Next Round ➡️"):
            next_round()
            st.rerun()