from collections import Counter
n = int(input())
a = [int(input()) for _ in range(n)]
cnt = Counter(a)
ans = 0
for i in cnt:
    if cnt[i] % 2 == 1:
        ans += 1
print(ans) 
