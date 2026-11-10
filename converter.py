"""
Currency converter using the Frankfurter API.

Provides functions to fetch the exchange rate between two
currencies and convert an amount from one to the other.
"""
import math
import requests

FIXED_URL = "https://api.frankfurter.dev/v2/rate/"
TIMEOUT_SECONDS = 5


def find_rate(base, target, seconds):
    """
    Return the exchange rate from base currency to target currency.
    """
    url = FIXED_URL + base + "/" + target
    response = requests.get(url, timeout=seconds)
    currency_dict = response.json()
    return currency_dict["rate"]


def convert(amount, rate):
    """
    Return the amount converted into the target currency using the rate.
    """
    return amount * rate


if __name__ == "__main__":
    base_currency = input("Base: ").strip().upper()
    target_currency = input("Target: ").strip().upper()
    try:
        value = float(input("Amount: "))
        if value <= 0 or not math.isfinite(value):
            raise ValueError("Amount must be positive and finite.")
    except ValueError:
        print("Please enter a positive number.")
    else:
        try:
            exchange_rate = find_rate(base_currency, target_currency, TIMEOUT_SECONDS)
        except KeyError:
            print("Please enter a valid currency.")
        except requests.exceptions.Timeout:
            print("Server too slow, please try again later.")
        except requests.exceptions.ConnectionError:
            print("Network error. Please check your internet connection.")
        except requests.exceptions.RequestException:
            print("An error occurred while fetching exchange rates."
            " Please try again.")
        else:
            result = convert(value, exchange_rate)
            print(f"1 {base_currency} = {exchange_rate:.6f} "
                  f"{target_currency}")
            print(f"{value:.2f} {base_currency} = "
                  f"{result:.2f} {target_currency}")
