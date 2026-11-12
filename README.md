# Currency Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A small command-line tool and a web app that convert an amount from one currency to another using live exchange rates from the [Frankfurter API](https://frankfurter.dev). The API is free and needs no API key.

## Features

- Fetches the live exchange rate between two currencies
- Converts any positive amount at that rate
- **Web app** built with Streamlit:
  - Pick currencies from dropdown menus for convenience
  - Side-by-side layout with a burgundy theme
  - Result shown in a clear success box, along with the rate used
- **Terminal version** for quick conversions without a browser
- Handles bad input, unknown currency codes, slow servers, and network problems with clear messages
- Unit tests with pytest, linting with pylint

## Project structure

```
currency-converter/
├── .streamlit/
│   └── config.toml       # web app theme settings
├── app.py                # Streamlit web interface
├── converter.py          # find_rate, convert, find_currency_codes and main guard
├── test_converter.py     # tests for convert
├── requirements.txt      # packages needed to run the program
├── requirements-dev.txt  # packages needed for testing and linting
├── .gitignore            # files to ignore
├── LICENSE               # MIT License text
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

### Web app

```bash
streamlit run app.py
```
On Windows, use `py -m streamlit run app.py` if `streamlit` isn't recognised.

A browser tab opens automatically (usually at `http://localhost:8501`). Choose the **From** and **To** currencies
from the dropdowns, enter an amount, and click **Convert**. Press `Ctrl + C` in the terminal to stop the app.

### Terminal

```bash
python converter.py
```
On Windows, use `py converter.py` if `python` is not recognised.

The program asks for a base currency, a target currency, and an amount. Currency codes are letters (USD, EUR, PKR) and can be typed in any case.

```
Base: usd
Target: eur
Amount: 100
1 USD = 0.893590 EUR
100.00 USD = 89.36 EUR
```

The numbers above are sample values. Real rates change daily.

## Error handling

| Situation | Where | Message |
| --- | --- | --- |
| Amount is not a number, is zero or negative, or is not finite (e.g., abc, 0, -5, nan, or inf) | Terminal | `Please enter a positive number.` |
| Amount is zero (the input box already blocks negatives and non-numbers) | Web app | `Please enter a positive number.` |
| Currency code is not recognised | Terminal | `Please enter a valid currency.` |
| No rate exists for the chosen pair | Web app | `No rate is available for this pair. Please choose another currency.` |
| Currency list can't be loaded when the page opens | Web app | `Could not load the currency list. Please check your internet connection and refresh the page.` |
| Server takes longer than expected time (`TIMEOUT_SECONDS`) | Both | `Server too slow, please try again later.` |
| No internet connection | Both | `Network error. Please check your internet connection.` |
| Other request-related errors (`RequestException`) | Terminal | `An error occurred while fetching exchange rates. Please try again.` |
| Other request-related errors (`RequestException`) | Web app | `An error occurred while fetching exchange rates.` |

## Running the tests

After installing `requirements-dev.txt`:
```bash
python -m pytest
```

The tests cover `convert` with whole numbers, decimals, mixed values, and very small rates. `find_rate` and `find_currency_codes` are not tested yet because they call the live API.

If all tests pass, the last line looks like `===== 4 passed in 0.05s =====` (the count and time will vary).

## Linting

```bash
python -m pylint converter.py test_converter.py app.py
```
A clean run ends with `Your code has been rated at 10.00/10`.

## How it works

- `find_rate(base, target, seconds)` builds the API URL, sends the request with a timeout, and returns the rate.
- `find_currency_codes(seconds)` fetches the list of supported currencies from the API and returns the letter codes.
- `convert(amount, rate)` multiplies the amount by the rate.
- `converter.py`'s main block reads the input, checks it, and prints the result.
- `app.py` is the interface: it reuses `find_rate`, `find_currency_codes` and `convert` from `converter.py` instead of repeating that logic. The currency list is cached with `st.cache_data`, so the API is called once per hour instead of every time the page redraws.

## Author

**Fatima Asim**

- GitHub: https://github.com/fatimabuttasim
- LinkedIn: https://linkedin.com/in/fatima-asim-69291543a

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Exchange rates are provided by the [Frankfurter API](https://frankfurter.dev).
