# World of Games

A Python command-line game collection with a Flask score page and a Selenium
end-to-end browser test.

## Components

- `app/MainGame.py` and `app/Live.py` start the console game flow and dispatch
  to the games.
- `app/MemoryGame.py`, `app/GuessGame.py`, and
  `app/CurrencyRouletteGame.py` implement the games.
- `app/Score.py` reads and updates the saved score; `app/Utils.py` configures
  the score file path.
- `app/MainScores.py` serves the current score as a web page.
- `tests/e2e.py` opens the score page in Chrome and validates the displayed
  score.

## Dependencies

- Python 3.8 or later.
- Flask (`Flask>=2.3`) for the score service.
- Selenium (`selenium>=4.0`) for the browser test; Chrome must be installed.
- Currency Roulette may require internet access.

Install the Python dependencies from the project root:

```powershell
py -m pip install -r requirements.txt
```

`requirements.txt` lists Flask and Selenium. The games otherwise use Python's
standard library.

## Configuration and score storage

The score file path is selected in `app/Utils.py`. When the console game runs
on Windows, it reads and writes `Scores.txt` in the project root. On Linux,
including the service container, the path is `/Scores.txt`.

The score service listens inside its environment on `0.0.0.0:5000` with debug
mode disabled. Docker Compose publishes that internal port as
`http://localhost:8777/` on the host. The standard Docker image starts with an
initial `/Scores.txt` containing `0`.

## Start the console game

From the project root:

```powershell
py -m app.MainGame
```

To run the score page directly on the host:

```powershell
py -m app.MainScores
```

On Windows, the local score page uses the project-root `Scores.txt` file and
is available at `http://127.0.0.1:5000/`.

## Start the Docker service

From the project root:

```powershell
docker compose up --build -d
```

Open `http://localhost:8777/`. Stop the service with:

```powershell
docker compose down
```

The image is tagged `docker.io/arikd12/world-of-games-scores:latest` for
publishing to Docker Hub. The direct `docker run` command is recorded in
`docker-run-command.txt`.

## Run the isolated browser test

The isolated test uses `tests/Scores.txt`, which contains `100`. The test
Compose override mounts this dedicated fixture read-only at `/Scores.txt`;
it does not mount or modify the console's real `Scores.txt`. Ensure the fixture
exists before starting the container. The test accepts scores from 1 through
1000; this is only the browser test's acceptance condition and is not a maximum
score for the application.

With Chrome installed, run these commands from the project root in
PowerShell:

```powershell
py -m pip install -r requirements.txt
if (-not (Test-Path .\tests\Scores.txt -PathType Leaf)) { throw "Missing tests\Scores.txt fixture" }
docker compose -f docker-compose.yml -f docker-compose.test.yml up --build -d
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
py tests\e2e.py
$e2eExitCode = $LASTEXITCODE
docker compose -f docker-compose.yml -f docker-compose.test.yml down
if ($e2eExitCode -ne 0) { exit $e2eExitCode }
```

The test waits for the visible `score` element. It exits with status `0` on
success and a nonzero status on failure.
