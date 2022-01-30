import math
from decimal import *
from unicodedata import decimal
N, L, W = map(int, input().split())
an = [int(x) for x in input().split()]
 
pre = 0
ans = 0
for ai in an:
    cur =Decimal(ai)
    if cur >= pre:
        ans += math.ceil((cur-pre) / W)
    pre = cur + W
 
if L >= pre:
    ans +=  math.ceil((L-pre) / W)
 
print(ans)