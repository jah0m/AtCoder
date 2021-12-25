import itertools
from typing import Reversible

n, x = map(int, input().split())
ln = [[int(x) for x in input().split()[1:]] for _ in range(n)]

res = list(itertools.product(*ln))

ans = 0
for arr in res:
    sum = 1
    for num in arr:
        sum *= num
    if sum == x:
        ans += 1
print(ans)



