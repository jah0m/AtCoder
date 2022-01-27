N, W = map(int, input().split())

dp = [[0] *(W+1) for _ in range(N+1)]

for i in range(N):
    dp[i+1] = dp[i].copy()
    w, v = map(int, input().split())
    for j in range(W+1-w):
        dp[i+1][j+w] = max(dp[i][j]+v, dp[i][j+w])
print(dp[-1][-1])