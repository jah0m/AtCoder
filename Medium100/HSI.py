n, m = map(int, input().split())

time = 1900 * m + 100 * (n-m)
ans = time * 2**m
print(ans)