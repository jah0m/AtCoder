n = int(input())
pn = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    if pn[i] == i+1:
        if i < n-1:
            pn[i], pn[i+1] = pn[i+1], pn[i]
        else:
            pn[i-1], pn[i] =  pn[i], pn[i-1]
        ans += 1

print(ans)
