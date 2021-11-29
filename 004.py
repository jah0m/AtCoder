h, w = map(int, input().split())
a = [[int(x) for x in input().split()] for k in range(h)]
ans = [0] * h
row = [0] * h
col = [0] * w
for i in range(len(ans)):
    ans[i] = [0] * w
for i in range(h):
    for j in range(w):
        row[i] += a[i][j]
        col[j] += a[i][j]

for i in range(h):
    for j in range(w):
        ans[i][j] = row[i] + col[j] - a[i][j]
        
for x in ans:
    print(*x, sep=' ')