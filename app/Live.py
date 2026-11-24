from .MemoryGame import play as play_memory
from .GuessGame import play as play_guess
from .CurrencyRouletteGame import play as play_currency
from .Score import add_score


def welcome(name):
    return (
        f"Hello {name} and welcome to the World of Games (WoG).\n"
        "Here you can find many cool games to play."
    )


def _prompt_integer(prompt, minimum, maximum, field_name):
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print(
                f"Invalid {field_name}. "
                f"Please enter a whole number between {minimum} and {maximum}."
            )
            continue

        if minimum <= value <= maximum:
            return value

        print(
            f"Invalid {field_name}. "
            f"Please enter a whole number between {minimum} and {maximum}."
        )


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - Remember a sequence of numbers.")
    print("2. Guess Game - Guess the number chosen by the computer.")
    print("3. Currency Roulette - Guess the value of a currency conversion.")

    game_choice = _prompt_integer("Please choose a game (1-3): ", 1, 3, "choice")
    difficulty = _prompt_integer(
        "Please choose game difficulty from 1 to 5: ", 1, 5, "difficulty"
    )

    if game_choice == 1:
        result = play_memory(difficulty)
    elif game_choice == 2:
        result = play_guess(difficulty)
    else:
        result = play_currency(difficulty)

    if result is True:
        add_score(difficulty)
        print("Congratulations! You won!")
    elif result is None:
        print("The game round was cancelled because a required service was unavailable.")
    else:
        print("You lost. Better luck next time!")