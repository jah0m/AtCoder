import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

n, x = map(int, input().split())
xn = [int(x) for x in input().split()]

xn = list(map(lambda i: abs(i-x), xn))
ans = gcd(*xn)
print(ans)
