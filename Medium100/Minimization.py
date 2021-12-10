import math
n, k = map(int, input().split())
an = [int(x) for x in input().split()]

ans = 1 + (n-k)/(k-1)
ans = math.ceil(ans)
print(ans)