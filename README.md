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

Build and start the score service from the project root with Docker Compose:

```text
docker compose up --build -d
```

Stop it with `docker compose down`. The score page is available at
`http://localhost:8777/`; Compose publishes host port `8777` to the container's
internal port `5000`. The image is tagged
`docker.io/arikd12/world-of-games-scores:latest` for future Docker Hub
publishing. The container listens on `0.0.0.0:5000` with debug mode disabled
and includes an initial `/Scores.txt` file containing `0`. A direct
`docker run` command is recorded in `docker-run-command.txt`.

## End-to-end score test

The browser test uses `tests/Scores.txt`, a dedicated fixture containing `100`.
Compose mounts it read-only at `/Scores.txt`; the real game score file is not
mounted or modified. Keep the fixture in place before starting the test service.
The test's accepted range (1–1000) is only a browser-test condition, not an
application score limit.

Start the test service, run the test with Chrome available, then stop the
service:

```powershell
docker compose -f docker-compose.yml -f docker-compose.test.yml up --build -d
py -m pip install -r requirements.txt
py tests/e2e.py
docker compose -f docker-compose.yml -f docker-compose.test.yml down
```

The test waits for the score element and exits with status `0` on success or a
nonzero status on failure.

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