import math
N, W = map(int, input().split())

L = 10 ** 5
dp = [[math.inf] * (L+1) for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    w, v = map(int,input().split())
    for j in range(L+1):
        if j >= v:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v] + w)
        else:
            dp[i+1][j] = dp[i][j]

for i, d in enumerate(dp[N]):
    if d <= W:
        maxv = i
print(maxv)