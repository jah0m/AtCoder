n, m = map(int, input().split())
ans = 0
ans += min(m // 2, n)
m -= min(m // 2, n) * 2
ans += m // 4

print(ans)