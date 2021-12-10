from collections import Counter
n = int(input())
dn = [int(x) for x in input().split()]
m = int(input())
tn = [int(x) for x in input().split()]

dc = Counter(dn)
tc = Counter(tn)
ans = 'YES'
for ti in tc:
    if tc[ti] > dc[ti]:
        ans = 'NO'
        break
print(ans)