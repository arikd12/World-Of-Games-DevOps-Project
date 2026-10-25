import random
import json
from urllib.request import urlopen
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from urllib.error import URLError, HTTPError

def generate_usd_amount():
    return random.randint(1, 100)

def get_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    try:
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
        if not isinstance(data, dict) or data.get("result") != "success":
            raise ValueError("Invalid response from currency API.")
        rates = data.get("rates")
        if not isinstance(rates, dict) or "ILS" not in rates:
            raise ValueError("ILS exchange rate is missing.")
        exchange_rate = Decimal(str(rates["ILS"]))
        if not exchange_rate.is_finite() or exchange_rate <= 0:
            raise ValueError("Invalid ILS exchange rate.")
        return exchange_rate
    except (
        HTTPError,
        URLError,
        TimeoutError,
        OSError,
        json.JSONDecodeError,
        InvalidOperation,
        TypeError,
        ValueError,
        KeyError,
    ) as error:
        raise RuntimeError(
            "Unable to retrieve the USD-to-ILS exchange rate. "
            "The round has been cancelled."
        ) from error

def convert_to_ils(usd_amount, exchange_rate):
    amount = Decimal(str(usd_amount)) * Decimal(str(exchange_rate))
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def get_money_interval(difficulty, t):
    tolerance = Decimal(5 - difficulty)
    lower = t - tolerance
    upper = t + tolerance
    return lower, upper

def get_guess_from_user(usd_amount):
    while True:
        user_input = input(f"How much is ${usd_amount} in ILS? Enter your estimate: ")
        try:
            guess = Decimal(user_input)
            if guess.is_finite() and guess >= 0:
                return guess
            print("Please enter a valid non-negative amount.")
        except InvalidOperation:
            print("Invalid input. Please enter a decimal number.")

def play(difficulty):
    try:
        usd_amount = generate_usd_amount()
        exchange_rate = get_exchange_rate()
    except RuntimeError as error:
        print(f"Error: {error}")
        return False
    correct_amount = convert_to_ils(usd_amount, exchange_rate)
    lower, upper = get_money_interval(difficulty, correct_amount)
    guess = get_guess_from_user(usd_amount)
    return lower <= guess <= upper