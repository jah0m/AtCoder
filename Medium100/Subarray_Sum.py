n, k , s = map(int, input().split())

if s < 10 ** 9: ans = [s+1] * n
else: ans = [1] * n

for i in range(k):
    ans[i] = s
print(*ans)