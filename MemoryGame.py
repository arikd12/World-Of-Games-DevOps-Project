import random

def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        sequence.append(random.randint(1, 101))
    return sequence

def play(difficulty):
    return False