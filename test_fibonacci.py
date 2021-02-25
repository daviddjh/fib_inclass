import unittest
import fib
import math

class TestFib(unittest.TestCase):
    def testFib(self):
        self.assertEqual(fib.fib_getNext(1, 1), 2)
        self.assertEqual(fib.fib_getNext(1, 2), 4)
        self.assertEqual(fib.fib_getNext(1, 3), 8)
        self.assertEqual(fib.fib_getNext(1, 4), 16)

    def testFact(self):
        self.assertEqual(fib.Dfactorial(1), math.factorial(1))
        self.assertEqual(fib.Dfactorial(2), math.factorial(2))
        self.assertEqual(fib.Dfactorial(3), math.factorial(3))
        self.assertEqual(fib.Dfactorial(4), math.factorial(4))

if __name__ == "__main__":
    unittest.main()
