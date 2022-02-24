from itertools import combinations
from collections import Counter
import math
l, r = map(int, input().split())
m = int(input())
nm = [int(x) for x in input().split()]
#最小公倍数
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

ans = r - l + 1
for n in nm:
    cnt = r // n - (l-1) // n
    ans -= cnt

for a, b in combinations(nm, 2):
    c = my_lcm_base(a,b)
    cnt = r // c - (l-1) // c
    ans += cnt

print(ans)