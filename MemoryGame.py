import random
import time

def show_sequence(sequence):
    print(sequence)
    time.sleep(0.7)
    print("\033[2J\033[H", end="")

def get_list_from_user(difficulty):
    while True:
        user_input = input(f"Enter {difficulty} whole numbers separated by spaces: ")
        try:
            numbers = [int(number) for number in user_input.split()]
            if len(numbers) == difficulty:
                return numbers
            print(f"Please enter exactly {difficulty} numbers.")
        except ValueError:
            print("Invalid input. Please enter whole numbers separated by spaces.")

def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        sequence.append(random.randint(1, 101))
    return sequence

def play(difficulty):
    return False