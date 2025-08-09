import factorial
from factorial import factorial

def test_factorial_casos():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720
