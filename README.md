# World of Games

A Python command-line game collection.

## Requirements

- Python 3.8 or later.
- Internet access may be required for Currency Roulette.

`requirements.txt` is intentionally empty because the application uses only Python standard-library modules and requires no third-party packages.

## Run

From the project root, run:

```powershell
py -m app.MainGame
```

Enter your name, choose a game from 1 to 3, and select a difficulty from 1 to 5.

## Games

- **Memory Game** — Remember a sequence of numbers and enter it correctly.
- **Guess Game** — Guess the number selected by the computer.
- **Currency Roulette** — Guess the value of a currency conversion.

The shared score is stored in `Scores.txt` in the project root and is initialized
on the first win.

## Project structure

- `app/` — Application startup script, game modules, scoring, and shared utilities.
- `README.md` — Project documentation.
- `requirements.txt` — Empty; the application uses only standard-library modules.