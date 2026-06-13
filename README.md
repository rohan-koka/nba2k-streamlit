# 🏀 NBA 2K Rating Guessing Game

A web app where you guess the NBA 2K overall ratings of current NBA players and earn points based on accuracy.

## How to Play
- You are shown a player's name, team, and position
- Guess their NBA 2K overall rating (1-99)
- Points are awarded based on how close your guess is:
  - Exact: +10 points
  - Within 2: +7 points
  - Within 5: +4 points
  - More than 5 off: +0 points
- 10 rounds per game, max score is 100

## Live Demo
[Play the game here](https://rohan-koka-nba2k-streamlit.streamlit.app)

## Built With
- Python
- Streamlit

## Run Locally
```bash
pip3 install streamlit
streamlit run app.py
```
