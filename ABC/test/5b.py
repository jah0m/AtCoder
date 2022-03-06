from collections import deque
n, m = map(int, input().split())
arr = [[x for x in input()] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            sy = i
            sx = j
        if arr[i][j] == 'G':
            gy = i
            gx = j
INF = 10 ** 6
dp = [[INF, 0] * m for _ in range(n)]
dp[sy][sx] = [0, 0]

for i in range(n):
    for j in range(m):
        if i == sy and j == sx: continue
        from_left = dp[i][j-1][0] + 1 + ()
        from_top = dp[i-1][j]