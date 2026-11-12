"""
Streamlit web interface for the currency converter.
 
Reuses find_rate, convert and find_currency_codes from converter.py,
so only the interface layer is new.
"""
import requests
import streamlit as st

from converter import find_rate, convert, find_currency_codes, TIMEOUT_SECONDS


@st.cache_data(ttl=3600)
def load_codes():
    """
    Return the currency codes, fetched at most once per hour.
    """
    return find_currency_codes(TIMEOUT_SECONDS)

def start_index(codes, code):
    """
    Return the position of code in codes, or 0 if it is missing.
    """
    if code in codes:
        return codes.index(code)
    return 0


st.title("Currency Converter")
st.caption("Live exchange rates from the Frankfurter API")

try:
    currency_codes = load_codes()
except requests.exceptions.RequestException:
    st.error("Could not load the currency list. "
             "Please check your internet connection and refresh the page.")
    st.stop()

col1, col2 = st.columns(2)
with col1:
    base = st.selectbox("From", currency_codes,
                        index=start_index(currency_codes, "USD"))
with col2:
    target = st.selectbox("To", currency_codes,
                          index=start_index(currency_codes, "PKR"))

amount = st.number_input("Amount", min_value=0.0, value=100.0, step=1.0)

if st.button("Convert"):
    if amount <= 0:
        st.error("Please enter a positive number.")
    else:
        try:
            rate = find_rate(base, target, TIMEOUT_SECONDS)
        except KeyError:
            st.error("No rate is available for this pair. "
                     "Please choose another currency.")
        except requests.exceptions.Timeout:
            st.error("Server too slow, please try again later.")
        except requests.exceptions.ConnectionError:
            st.error("Network error. Please check your internet connection.")
        except requests.exceptions.RequestException:
            st.error("An error occurred while fetching exchange rates.")
        else:
            result = convert(amount, rate)
            st.success(f"{amount:,.2f} {base} = {result:,.2f} {target}")
            st.write(f"1 {base} = {rate:.6f} {target}")
