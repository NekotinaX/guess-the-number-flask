import random

def generate_number():
    return random.randint(1, 100)

def check_guess(guess, target):
    if guess < target:
        return "too low"
    elif guess > target:
        return "too high"
    return "correct"
