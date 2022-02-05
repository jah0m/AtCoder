H, W = map(int,input().split())
a = [[int(x) for x in input().split()] for _ in range(H)]
b = [[0] * H for _ in range(W)]

for i in range(H):
    for j in range(W):
        b[j][i] = a[i][j]

for l in b:
    print(*l)