import os
from pathlib import Path


SCORES_FILE_NAME = "Scores.txt"
SCORES_FILE_PATH = (
    Path("/Scores.txt")
    if os.name != "nt"
    else Path(__file__).resolve().parent.parent / SCORES_FILE_NAME
)
# Valid scores are non-negative, so -1 is an unambiguous failure sentinel.
BAD_RETURN_CODE = -1


def Screen_cleaner():
    os.system("cls" if os.name == "nt" else "clear")
