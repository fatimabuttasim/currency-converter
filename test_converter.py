"""
Tests for the convert function in converter.py.
"""
import pytest
from converter import convert


def test_convert_whole_numbers():
    """
    Check that convert works with simple whole numbers.
    """
    assert convert(10, 3) == 30


def test_convert_decimal_numbers():
    """
    Check that convert works with decimal numbers.
    """
    assert convert(9.6, 4.0) == pytest.approx(38.4)


def test_convert_mixed_numbers():
    """
    Check that convert works with simple whole numbers and
    decimal numbers combined.
    """
    assert convert(0.1, 3) == pytest.approx(0.3)


def test_convert_smaller_fractions():
    """
    Check that convert works with smaller actual rates.
    """
    assert convert(4, 0.00036) == pytest.approx(0.00144)
