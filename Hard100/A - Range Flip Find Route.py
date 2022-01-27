h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

INF = 10 ** 6
dp = [[INF] * w for _ in range(h)]
dp[0][0] = int(grid[0][0] == '#')

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0: continue
        from_left = dp[i][j-1] + (grid[i][j] == '#' and grid[i][j-1] == '.')
        from_top = dp[i-1][j] + (grid[i][j] == '#' and grid[i-1][j] == '.')
        dp[i][j] = min(from_left, from_top)

print(dp[h-1][w-1])