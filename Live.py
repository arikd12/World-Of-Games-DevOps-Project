def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - Remember a sequence of numbers.")
    print("2. Guess Game - Guess the number chosen by the computer.")
    print("3. Currency Roulette - Guess the value of a currency conversion.")

    game_choice = ""
    while not game_choice.isdigit() or not 1 <= int(game_choice) <= 3:
        game_choice = input("Please choose a game (1-3): ").strip()
        if not game_choice.isdigit() or not 1 <= int(game_choice) <= 3:
            print("Invalid choice. Please enter a whole number between 1 and 3.")

    difficulty = ""
    while not difficulty.isdigit() or not 1 <= int(difficulty) <= 5:
        difficulty = input("Please choose game difficulty from 1 to 5: ").strip()
        if not difficulty.isdigit() or not 1 <= int(difficulty) <= 5:
            print("Invalid difficulty. Please enter a whole number between 1 and 5.")

    return int(game_choice), int(difficulty)