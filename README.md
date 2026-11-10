# Currency Converter

A small command-line tool that converts an amount from one currency to another using live exchange rates from the [Frankfurter API](https://frankfurter.dev). The API is free and needs no API key.

## Features

- Fetches the live exchange rate between two currencies
- Converts any positive amount at that rate
- Handles bad input, unknown currency codes, slow servers, and network problems with clear messages
- Unit tests with pytest, linting with pylint

## Project structure

```
currency-converter/
├── converter.py          # find_rate, convert, and main guard
├── test_converter.py     # tests for convert
├── requirements.txt      # packages needed to run the program
├── requirements-dev.txt  # packages needed for testing and linting
├── .gitignore            # files to ignore
└── README.md             # project description
```

## Requirements

- Python 3 (tested on 3.14.6)
- An internet connection (rates are fetched live)

## Installation

```bash
git clone https://github.com/fatimabuttasim/currency-converter
cd currency-converter
pip install -r requirements.txt
```
For development, also install `requirements-dev.txt`:
```bash
pip install -r requirements-dev.txt
```
On Windows, use `py -m pip` if `pip` isn’t recognised.

## Usage

```bash
python converter.py
```
On Windows, use `py converter.py` if `python` is not recognised.

The program asks for a base currency, a target currency, and an amount. Currency codes are three letters (USD, EUR, PKR) and can be typed in any case.

```
Base: usd
Target: eur
Amount: 100
1 USD = 0.893590 EUR
100.00 USD = 89.36 EUR
```

The numbers above are sample values. Real rates change daily.

## Error handling

| Situation | Message |
| --- | --- |
| Amount is not a number, is zero or negative, or is not finite (e.g., abc, 0, -5, nan, or inf) | `Please enter a positive number.` |
| Currency code is not recognised | `Please enter a valid currency.` |
| Server takes longer than expected time (`TIMEOUT_SECONDS`) | `Server too slow, please try again later.` |
| No internet connection | `Network error. Please check your internet connection.` |
| Other request-related errors (`RequestException`) | `An error occurred while fetching exchange rates. Please try again.`|

## Running the tests

After installing `requirements-dev.txt`:
```bash
python -m pytest
```

The tests cover `convert` with whole numbers, decimals, mixed values, and very small rates. `find_rate` is not tested yet because it calls the live API.

If all tests pass, the last line looks like `===== 4 passed in 0.05s =====` (the count and time will vary).

## Linting

```bash
python -m pylint converter.py test_converter.py
```
A clean run ends with `Your code has been rated at 10.00/10`.

## How it works

- `find_rate(base, target, seconds)` builds the API URL, sends the request with a timeout, and returns the rate.
- `convert(amount, rate)` multiplies the amount by the rate.
- The main block reads the input, checks it, and prints the result.

## Author

**Fatima Asim**

- GitHub: https://github.com/fatimabuttasim
- LinkedIn: https://linkedin.com/in/fatima-asim-69291543a

## Acknowledgements

Exchange rates are provided by the [Frankfurter API](https://frankfurter.dev).