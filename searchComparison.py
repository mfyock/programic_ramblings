import random

def binarySearch(n, lst, c=1):

    if len(lst) > 1:

        midPoint = int(len(lst) / 2)

        if lst[midPoint] == n:
            return c
        
        else:
            
            if lst[midPoint] > n:
                return binarySearch(n, lst[0:midPoint], c+1)

            elif lst[midPoint] < n:
                return binarySearch(n, lst[midPoint:], c+1)

    else:
        return c

def linearSearch(n, lst):
    c = 0
    for i in lst:
        if i != n:
            c += 1
        else:
            return c


x = [i for i in range(1,100001)]
num = random.choice(x)

print('Number: ', num)

print('Linear Search steps: ', linearSearch(num, x))
print('Binary Search steps: ', binarySearch(num, x))]