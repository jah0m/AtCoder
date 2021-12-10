h, w = map(int, input().split())
a = [[x for x in input()] for _ in range(h)]

ans = [''] * h
dx = [-1, 0, 1]
dy = [-1, 0, 1]
for y in range(h):
    for x in range(w):
        cnt = 0
        if a[y][x] == '#':
            ans[y] += '#'
            continue
        for dx in range(-1,2):
            for dy in range(-1, 2):
                if dx == 0 and dy ==0: continue
                xx = x + dx
                yy = y + dy
                if(0<= xx and xx < w and 0<= yy and yy <h):
                    if a[yy][xx] == '#': cnt += 1
        ans[y] += str(cnt)  
for i in range(h):
    print(ans[i])

