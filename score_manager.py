import json

SCORES_FILE = "scores.json"

def save_score(attempts):
    try:
        with open(SCORES_FILE, "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []
    
    scores.append({"attempts": attempts})
    scores = sorted(scores, key=lambda x: x["attempts"])[:10]

    with open(SCORES_FILE, "w") as file:
        json.dump(scores, file)

def get_leaderboard():
    try:
        with open(SCORES_FILE, "r") as file:
            scores = json.load(file)
        return scores
    except FileNotFoundError:
        return []
