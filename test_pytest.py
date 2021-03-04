import fib
import math

def test_fib():
    assert fib.fib_getNext(1, 1) == 2
    assert fib.fib_getNext(1, 2) == 4
    assert fib.fib_getNext(1, 3) == 8
    assert fib.fib_getNext(1, 4) == 16

def test_fact():
    assert fib.Dfactorial(1) == math.factorial(1)
    assert fib.Dfactorial(2) == math.factorial(2)
    assert fib.Dfactorial(3) == math.factorial(3)
    assert fib.Dfactorial(4) == math.factorial(4)
    assert fib.Dfactorial(5) == math.factorial(5)

