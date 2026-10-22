def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - Remember a sequence of numbers.")
    print("2. Guess Game - Guess the number chosen by the computer.")
    print("3. Currency Roulette - Guess the value of a currency conversion.")

    game_choice = 0
    while game_choice < 1 or game_choice > 3:
        game_choice = int(input("Please choose a game (1-3): "))
        if game_choice < 1 or game_choice > 3:
            print("Invalid choice. Please enter a number between 1 and 3.")

    difficulty = 0
    while difficulty < 1 or difficulty > 5:
        difficulty = int(input("Please choose game difficulty from 1 to 5: "))
        if difficulty < 1 or difficulty > 5:
            print("Invalid difficulty. Please enter a number between 1 and 5.")

    return game_choice, difficulty