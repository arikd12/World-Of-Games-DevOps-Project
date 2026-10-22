from Live import welcome, load_game
name = input("Please enter your name: ")
print(welcome(name))
game, difficulty = load_game()