import sys

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


APPLICATION_URL = "http://127.0.0.1:8777/"
SCORE_ELEMENT_ID = "score"
ELEMENT_WAIT_SECONDS = 10


def test_scores_service(application_url):
    browser = None
    test_passed = False

    try:
        browser = webdriver.Chrome()
        browser.get(application_url)
        score_element = WebDriverWait(browser, ELEMENT_WAIT_SECONDS).until(
            EC.visibility_of_element_located((By.ID, SCORE_ELEMENT_ID))
        )
        score_text = score_element.text.strip()

        if score_text.isascii() and score_text.isdecimal():
            score = int(score_text)
            test_passed = 1 <= score <= 1000

        if not test_passed:
            print(
                f"Invalid score value: {score_text!r}; expected a whole number "
                "from 1 to 1000.",
                file=sys.stderr,
            )
    except WebDriverException as error:
        print(f"Score service browser test failed: {error}", file=sys.stderr)
    finally:
        if browser is not None:
            try:
                browser.quit()
            except WebDriverException as error:
                print(f"Could not close the browser: {error}", file=sys.stderr)
                test_passed = False

    return test_passed


def main_function():
    sys.exit(0 if test_scores_service(APPLICATION_URL) else -1)


if __name__ == "__main__":
    main_function()
