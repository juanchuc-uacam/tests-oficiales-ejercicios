import factorial

def test_factorial_0():
    assert factorial.factorial(0) == 1

def test_factorial_1():
    assert factorial.factorial(1) == 1

def test_factorial_5():
    assert factorial.factorial(5) == 120

def test_factorial_7():
    assert factorial.factorial(7) == 5040

def test_factorial_10():
    assert factorial.factorial(10) == 3628800
