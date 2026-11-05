"""
This file contains a simple function to get data
from a simple URL of frankfurter.
"""

import requests

RATE_URL = "https://api.frankfurter.dev/v2/rate/usd/pkr"
TIMER = 5
def find_rate(url, seconds):
    """
    Return the exchange rate from one currency to another.
    """
    response = requests.get(url, timeout=seconds)
    currency_dict = response.json()
    return currency_dict["rate"]

if __name__ == "__main__":
    print(find_rate(RATE_URL, TIMER))
