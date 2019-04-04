import random
import unittest

def find_missing_num(arr):
    for i,n in enumerate(arr, 1):
        if i != n:
            return i
    
    return len(arr) + 1

class MissingNumTest(unittest.TestCase):
    
    def missing_num_test(self):
        x = [i for i in range(1,101)]
        y = random.choice(x)
        x.remove(y)
        z = find_missing_num(x)

        self.assertEqual(z, y)

        return 'Pass'

for i in range(100):
    print(MissingNumTest().missing_num_test())