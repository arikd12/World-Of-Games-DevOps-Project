# World of Games

A Python command-line game collection.

## Requirements

- Python 3.8 or later.
- Internet access may be required for Currency Roulette.

Install the dependencies with `py -m pip install -r requirements.txt`.

## Run

From the project root, run:

```powershell
py -m app.MainGame
```

Enter your name, choose a game from 1 to 3, and select a difficulty from 1 to 5.

To start the score web server locally, run:

```powershell
py -m app.MainScores
```

The score page is available at `http://127.0.0.1:5000/`.

## Run with Docker

Build the image from the project root and publish its internal port `5000` on
host port `8777`:

```powershell
docker build -t world-of-games-scores .
docker run --rm -p 8777:5000 world-of-games-scores
```

The score page is available at `http://localhost:8777/`. The container listens
on `0.0.0.0:5000` with debug mode disabled. The image includes an initial
`/Scores.txt` file containing `0`.

## Games

- **Memory Game** — Remember a sequence of numbers and enter it correctly.
- **Guess Game** — Guess the number selected by the computer.
- **Currency Roulette** — Guess the value of a currency conversion.

The score file location is configured in `app/Utils.py`. It is `/Scores.txt`
inside Linux containers and the project-root `Scores.txt` on Windows, and is
initialized on the first win.

## Project structure

- `app/` — Application startup script, game modules, scoring, and shared utilities.
- `README.md` — Project documentation.
- `requirements.txt` — Python dependencies, including Flask for the score server.