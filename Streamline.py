n, m = map(int, input().split())
xm = [int(x) for x in input().split()]

xm.sort()
#print(xm)
xn = [0] * m
for i in range(1, len(xm)):
    xn[i] = xm[i] - xm[i-1]
xn.sort(reverse=True)
if len(xn) > n:
    print(sum(xn[n-1:]))
else:
    print(0)