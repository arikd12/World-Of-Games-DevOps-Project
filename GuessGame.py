import random

def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {difficulty}: "))
            if 1 <= guess <= difficulty:
                return guess
            print(f"Please enter a number between 1 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def compare_results(guess, secret_number):
    return guess == secret_number

def play(difficulty):
    return False