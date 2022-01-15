from collections import deque
h, w = map(int, input().split())
c = [[x for x in input()] for _ in range(h)]

sy = 0
sx = 0

queue = deque([[0,0]])
seen = [[-1 for _ in range(w)] for _ in range(h)]
seen[sy][sx] = 1
ans = 1

moves = [[0,1], [1,0]]
while queue:
    y, x = queue.popleft()

    for move in moves:
        if y+move[0] > h-1 or x+move[1]>w-1:
            continue
        if c[y+move[0]][x+move[1]] == '.' and seen[y+move[0]][x+move[1]] == -1:
            cur = seen[y][x] + 1
            ans = max(ans, cur)
            seen[y+move[0]][x+move[1]] = cur
            queue.append([y+move[0], x+move[1]])
print(ans)