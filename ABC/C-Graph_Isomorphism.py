import itertools
n, m = map(int, input().split())
ab = [[0]*n for _ in range(n)] 
cd = [[0]*n for _ in range(n)] 
ans = False
for _ in range(m):
    a, b = map(int, input().split())
    ab[a-1][b-1] = 1
    ab[b-1][a-1] = 1
for _ in range(m):
    a, b = map(int, input().split())
    cd[a-1][b-1] = 1
    cd[b-1][a-1] = 1

for p in itertools.permutations(range(n)):
    ok = True
    for i in range(n):
        for j in range(n):
            if ab[i][j] != cd[p[i]][p[j]]:
                ok = False
    if ok:
        ans = True
print('Yes' if ans else 'No')