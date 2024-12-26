from flask import Flask, render_template, request, redirect, url_for, session
from game_logic import generate_number, check_guess
from score_manager import save_score, get_leaderboard

app = Flask(__name__)
app.secret_key = "secret_key_for_session_management"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start_game():
    session['number'] = generate_number()
    session['attempts'] = 0
    return redirect(url_for("guess_page"))

@app.route("/guess", methods=["GET", "POST"])
def guess_page():
    if request.method == "POST":
        guess = int(request.form["guess"])
        session['attempts'] += 1
        result = check_guess(guess, session['number'])
        if result == "correct":
            save_score(session['attempts'])
            return redirect(url_for("leaderboard"))
        return render_template("guess.html", result=result)
    return render_template("guess.html", result=None)

@app.route("/leaderboard")
def leaderboard():
    scores = get_leaderboard()
    return render_template("leaderboard.html", scores=scores)

if __name__ == "__main__":
    app.run(debug=True)
