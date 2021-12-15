import math
n, m = map(int, input().split())

ans = 0
if n == m:
    ans = math.factorial(n)**2 * 2
elif abs(n-m) == 1:
    ans = math.factorial(n) * math.factorial(m)
print(ans % (10 **9 + 7))