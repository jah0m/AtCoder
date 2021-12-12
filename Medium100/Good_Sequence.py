from collections import Counter
n = int(input())
an = [int(x) for x in input().split()]

c = Counter(an)
ans = 0
for k in c:
    if c[k] > k:
        ans += c[k] - k
    elif c[k] < k:
        ans += c[k]
print(ans)