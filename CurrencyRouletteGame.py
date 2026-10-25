import random
import json
from urllib.request import urlopen

def generate_usd_amount():
    return random.randint(1, 100)

def get_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"

    with urlopen(url, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))

    if data.get("result") != "success":
        raise ValueError("Could not retrieve exchange rate.")

    return data["rates"]["ILS"]

def convert_to_ils(usd_amount, exchange_rate):
    return usd_amount * exchange_rate

def get_money_interval(difficulty, t):
    lower = t - (5 - difficulty)
    upper = t + (5 - difficulty)
    return lower, upper

def play(difficulty):
    return False