h, w = map(int, input().split())
a = [[x for x in input()] for _ in range(h)]

ans = 'Yes'
for i in range(h):
    for j in range(w):
        cnt = 0
        if a[i][j] == '#':
            if i != 0:
                cnt += (1 if a[i-1][j] == '#' else 0)
            if i != h-1:
                cnt += (1 if a[i+1][j] == '#' else 0)
            if j != 0:
                cnt += (1 if a[i][j-1] == '#' else 0)
            if j != w-1:
                cnt += (1 if a[i][j+1] == '#' else 0)
            if cnt == 0:
                ans = 'No'
                break
print(ans)