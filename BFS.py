from collections import *
from itertools import *
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
cn = [[x for x in input()] for _ in range(r)]
sy -= 1
sx -= 1
gy -= 1
gx -= 1

queue = deque()
queue.append([sy, sx])
seen = [[-1 for _ in range(c)] for _ in range(r)]
seen[sy][sx] = 0
moves = [[0,1],[0,-1],[1,0],[-1,0]]
while queue:
    y, x = queue.popleft()
    for move in moves:
        if cn[y+move[0]][x+move[1]] == '.' and seen[y+move[0]][x+move[1]] == -1:
            queue.append([y+move[0], x+move[1]])
            seen[y+move[0]][x+move[1]] = seen[y][x] + 1
print(seen[gy][gx])