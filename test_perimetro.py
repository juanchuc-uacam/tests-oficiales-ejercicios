import pytest
from perimetro import perimetro_rectangulo

def test_perimetro():
    assert perimetro_rectangulo(2, 3) == 10
    assert perimetro_rectangulo(5, 5) == 20
    assert perimetro_rectangulo(0, 0) == 0
