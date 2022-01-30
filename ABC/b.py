H, W = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(H)]

B = [[0] * H for _ in range(W)]

for i in range(H):
    for j in range(W):
        B[j][i] = A[i][j]

for line in B:
    print(*line)