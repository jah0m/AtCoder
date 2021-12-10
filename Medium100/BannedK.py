from collections import Counter
n = int(input())
a = [int(x) for x in input().split()]
ans = []

def get(n):
    return (n * (n-1)) // 2

cnt = Counter(a)
sum = 0
for c in cnt:
    sum += get(cnt[c])

for i in a:
    ans = sum
    ans -= get(cnt[i])
    ans += get(cnt[i] - 1)
    print(ans)