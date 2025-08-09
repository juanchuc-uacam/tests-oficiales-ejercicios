import pytest
from conversion import celsius_a_fahrenheit

def test_conversion():
    assert celsius_a_fahrenheit(0) == 32
    assert celsius_a_fahrenheit(100) == 212
    assert round(celsius_a_fahrenheit(37), 2) == 98.6
