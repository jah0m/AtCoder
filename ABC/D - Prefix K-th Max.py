import bisect
from collections import deque
from itertools import *
from typing import Deque
n, k = map(int, input().split())
pn = [int(x) for x in input().split()]

arr = [0] * (n+1)
for i in range(k):
    arr[pn[i]] = 1
ans = min(pn[:k])
print(ans)
for j in range(k,n):
    arr[pn[j]] = 1
    if pn[j] < ans:
        print(ans)
    else:
        for k in range(ans+1, n+1):
            if arr[k] == 1:
                ans = k
                print(ans)
                break