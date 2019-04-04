import unittest

def fib(a, b, n):
    if n == 0:
        return a
    else:
        n -= 1
        return fib(b, a + b, n)

class FibTest(unittest.TestCase):

    def testFibFunction(self):
        
        self.assertEqual(fib(0,1,10), 55)
        self.assertEqual(fib(0,1,15), 610)
        self.assertEqual(fib(0,1,20), 6765)

FibTest().testFibFunction()