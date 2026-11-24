import os


SCORES_FILE_NAME = "Scores.txt"
# Valid scores are non-negative, so -1 is an unambiguous failure sentinel.
BAD_RETURN_CODE = -1


def Screen_cleaner():
    os.system("cls" if os.name == "nt" else "clear")
