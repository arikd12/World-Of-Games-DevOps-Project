import os
import tempfile
from pathlib import Path

from .Utils import SCORES_FILE_NAME


class ScoreError(Exception):
    """Raised when the saved score cannot be read or updated."""


def _read_score(score_path):
    try:
        with score_path.open("r", encoding="utf-8") as score_file:
            saved_score = score_file.read().strip()
    except FileNotFoundError:
        return 0
    except OSError as error:
        raise ScoreError(f"Could not read {SCORES_FILE_NAME}: {error}") from error

    if not saved_score:
        raise ScoreError(
            f"{SCORES_FILE_NAME} is empty; it must contain one "
            "non-negative whole number."
        )
    if not saved_score.isascii() or not saved_score.isdecimal():
        raise ScoreError(
            f"Invalid score in {SCORES_FILE_NAME}; it must contain exactly "
            "one non-negative whole number."
        )

    return int(saved_score)


def _write_score(score_path, score):
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=score_path.parent,
            prefix=f".{score_path.name}.",
            suffix=".tmp",
            delete=False,
        ) as score_file:
            temporary_path = Path(score_file.name)
            score_file.write(f"{score}\n")
            score_file.flush()
            os.fsync(score_file.fileno())

        os.replace(temporary_path, score_path)
    except OSError as error:
        cleanup_error = None
        if temporary_path is not None:
            try:
                temporary_path.unlink()
            except FileNotFoundError:
                pass
            except OSError as cleanup_exception:
                cleanup_error = cleanup_exception

        message = f"Could not write {SCORES_FILE_NAME}: {error}"
        if cleanup_error is not None:
            message += f" Temporary score file cleanup also failed: {cleanup_error}"
        raise ScoreError(message) from error


def get_score():
    return _read_score(Path(SCORES_FILE_NAME))


def add_score(difficulty):
    if type(difficulty) is not int or not 1 <= difficulty <= 5:
        raise ValueError("difficulty must be a whole number between 1 and 5")

    score_path = Path(SCORES_FILE_NAME)
    current_score = get_score()
    POINTS_OF_WINNING = (difficulty * 3) + 5
    new_score = current_score + POINTS_OF_WINNING
    _write_score(score_path, new_score)

    return new_score
