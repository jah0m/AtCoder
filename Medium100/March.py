from collections import Counter
from math import factorial
n = int(input())
sn = [input() for _ in range(n)]

d = {'M': 0,  'A': 1, 'R':2, 'C':3, 'H':4}
cnt = [0] * 5
for si in sn:
    if si[0] in d:
        cnt[d[si[0]]] += 1
ans = 0
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            ans += cnt[i] * cnt[j] * cnt[k]
print(ans)