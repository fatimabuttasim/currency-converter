"""
Streamlit web interface for the currency converter.

Reuses find_rate and convert from converter.py, so only the
interface layer is new.
"""
import requests
import streamlit as st

from converter import find_rate, convert, TIMEOUT_SECONDS

st.title("Currency Converter")
st.caption("Live exchange rates from the Frankfurter API")

col1, col2 = st.columns(2)
with col1:
    base = st.text_input("From (e.g. USD)", value="USD").strip().upper()
with col2:
    target = st.text_input("To (e.g. PKR)", value="PKR").strip().upper()

amount = st.number_input("Amount", min_value=0.0, value=100.0, step=1.0)

if st.button("Convert"):
    if amount <= 0:
        st.error("Please enter a positive number.")
    else:
        try:
            rate = find_rate(base, target, TIMEOUT_SECONDS)
        except KeyError:
            st.error("Please enter a valid currency.")
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
