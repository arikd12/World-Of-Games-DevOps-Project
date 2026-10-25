import random
import time

def show_sequence(sequence):
    print(sequence)
    time.sleep(0.7)
    print("\033[2J\033[H", end="")


def get_list_from_user(difficulty):
    answer = []
    for i in range(difficulty):
        number = int(input(f"Enter number {i + 1}: "))
        answer.append(number)
    return answer

def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        sequence.append(random.randint(1, 101))
    return sequence

def play(difficulty):
    return False