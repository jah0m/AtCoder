from functools import reduce
import math
def gcd(*numbers):
    return reduce(math.gcd, numbers)
n = int(input())
an = list(int(x) for x in input().split())

ans = gcd(*an)
print(ans)