from functools import reduce
import math
n = int(input())
tn = [int(input()) for _ in range(n)]

def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)

print(my_lcm(*tn))