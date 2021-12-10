from collections import Counter
n = int(input())
an = [int(x) for x in input().split()]

c = Counter(an)
l = []
for i in c:
    if c[i] >= 2: l.append(i)
ans = 0
if len(l) >= 2:
    l.sort(reverse=True)
    ans = l[0] * l[1]
for i in c:
    if c[i] >= 4:
        ans = max(ans, i*i)
print(ans)
