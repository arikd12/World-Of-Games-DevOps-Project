# World of Games

A Python command-line game collection.

## Requirements

- Python 3.8 or later.
- Internet access is needed for Currency Roulette if its exchange-rate service requires it.

`requirements.txt` is intentionally empty: the application uses Python standard-library modules and does not require third-party packages.

## Run

From the project root, run:

```powershell
py MainGame.py
```

Enter your name, choose a game from 1 to 3, and select a difficulty from 1 to 5.

## Games

- **Memory Game** — Remember a sequence of numbers and enter it correctly.
- **Guess Game** — Guess the number selected by the computer.
- **Currency Roulette** — Guess the value of a currency conversion.

## Project files

The game modules and startup script are currently kept in the project root. As the project grows, they can be moved into a dedicated application directory while keeping `README.md` and `requirements.txt` at the root.