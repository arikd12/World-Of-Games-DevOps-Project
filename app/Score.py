from .Utils import SCORES_FILE_NAME


def add_score(difficulty):
    if type(difficulty) is not int or not 1 <= difficulty <= 5:
        raise ValueError("difficulty must be a whole number between 1 and 5")

    try:
        with open(SCORES_FILE_NAME, "r", encoding="utf-8") as score_file:
            saved_score = score_file.read().strip()
    except FileNotFoundError:
        current_score = 0
    else:
        if not saved_score.isascii() or not saved_score.isdecimal():
            raise ValueError(
                f"{SCORES_FILE_NAME} must contain one non-negative whole number"
            )
        current_score = int(saved_score)

    POINTS_OF_WINNING = (difficulty * 3) + 5
    new_score = current_score + POINTS_OF_WINNING

    with open(SCORES_FILE_NAME, "w", encoding="utf-8") as score_file:
        score_file.write(f"{new_score}\n")

    return new_score
