from flask import Flask

from .Score import ScoreError, get_score


app = Flask(__name__)


def _score_page(body):
    return (
        "<!doctype html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        "  <title>Scores Game</title>\n"
        "</head>\n"
        "<body>\n"
        f"  {body}\n"
        "</body>\n"
        "</html>\n"
    )


@app.route("/", methods=["GET"])
def index():
    try:
        score = get_score()
    except ScoreError as error:
        app.logger.error("Could not load the score: %s", error)
        return _score_page("<p>Score is unavailable.</p>"), 500

    return _score_page(f"<h1>Scores Game</h1><p>Current score: {score}</p>")


def score_server():
    app.run(host="127.0.0.1", port=5000, debug=False)


if __name__ == "__main__":
    score_server()
