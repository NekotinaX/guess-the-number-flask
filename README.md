# Guess the Number - Flask Game

A simple web-based game built using Flask. The objective of the game is to guess a randomly generated number between 1 and 100. Players have a limited number of attempts to guess the number, and their attempts are tracked.

## Features

- Random number generation between 1 and 100.
- User input for guesses.
- Feedback after each guess (whether the guess is too high or too low).
- A leaderboard that displays the number of attempts for previous players.
- A clean, user-friendly interface built with HTML, CSS, and Flask.

## How to Play

1. Visit the home page and click "Start Game" to begin a new round.
2. Enter a number between 1 and 100 and submit your guess.
3. The game will tell you if your guess is too high, too low, or correct.
4. Once you guess correctly, your number of attempts will be saved in the leaderboard.

## Installation

### Prerequisites

- Python 3.x
- Flask

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/guess-the-number-flask.git
   ```

2. Navigate to the project directory:
   ```bash
   cd guess-the-number-flask
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000` to play the game.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with improvements or bug fixes.
