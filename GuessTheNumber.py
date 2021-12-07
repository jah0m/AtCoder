n, m = map(int, input().split())
s = [[int(x) for x in input().split()] for _ in range(m)]
ans = -1
#print(s)
if n  == 1:
    start = 0
else:
    start = 10 ** (n-1)
for i in range(start, 10 ** n ):
    #print(i)
    cnt = 0
    for k in s:
        #print(k)
        if str(i)[k[0]-1] == str(k[1]):
            cnt += 1
    if cnt == m:
        ans = i
        break
print(ans)
