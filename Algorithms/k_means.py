import math

def k_means(lst):
    
    x = []
    
    for i in lst:
        x.append([i, math.sqrt(i[0] ** 2 + i[1] ** 2)])
    
    sorted_x = sorted(x, key=lambda i:-i[1])
    
    return [i[0] for i in sorted_x]