import random
import unittest

def find_duplicate(arr):
    # Finds the duplicate number in an integer array
    for i in range(len(arr)):
        if arr.count(arr[i]) == 2:
            return arr[i]

class DuplicateTest(unittest.TestCase):

    def find_duplicate_test(self):

        x = [i for i in range(100)]
        y = random.choice(x)
        x.append(y)

        z = find_duplicate(x)

        self.assertEqual(z,y)

for i in range(100):
    print(DuplicateTest().find_duplicate_test())