n, t = map(int, input().split())
l = [int(x) for x in input().split()]

ans = n * t
for i in range(n-1):
    if(l[i+1] - l[i]) < t:
        ans -= t - (l[i+1] - l[i])

print(ans)