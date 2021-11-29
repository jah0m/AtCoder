h, w = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(h)]
ans = []
row = [0] * h
col = [0] * w
for i in range(h):
    for j in range(w):
        row[i] += a[i][j]
        col[j] += a[i][j]

for i in range(h):
    l = []
    for j in range(w):
        #ans[i][j] = row[i] + col[j] - a[i][j]
        l.append(row[i] + col[j] - a[i][j])
    ans.append(l)
for x in ans:
    print(*x)