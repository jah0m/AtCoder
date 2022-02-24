from collections import deque
n, m = map(int, input().split())
arr = [[x for x in input()] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            sy = i
            sx = j
        if arr[i][j] == 'G':
            gy = i
            gx = j

queue = deque()
queue.append([sy, sx, 0])
reach = [[10**9 for _ in range(m)] for _ in range(n)]
reach[sy][sx] = 0
cnt = [[0 for _ in range(m)] for _ in range(n)]
moves = [[0,1],[1,0],[-1,0],[0,-1]]

while queue:
    y, x, z = queue.popleft()
    for move in moves:
        if y+move[0] > n-1 or x+move[1] > m-1 or y+move[0] < 0 or x+move[1] < 0:
            continue
        if cnt[y+move[0]][x+move[1]] >= 4:
            continue
        else:
            cnt[y+move[0]][x+move[1]] += 1

        if (arr[y+move[0]][x+move[1]] == '.' or arr[y+move[0]][x+move[1]] == 'G'):
            if reach[y][x] + 1 < reach[y+move[0]][x+move[1]]:
                queue.append([y+move[0], x+move[1], z])
                reach[y+move[0]][x+move[1]] = reach[y][x] + 1
            

        elif arr[y+move[0]][x+move[1]] == '#':
            if reach[y][x] + 1 + z < reach[y+move[0]][x+move[1]]:
                queue.append([y+move[0], x+move[1], z+1])
                reach[y+move[0]][x+move[1]] = reach[y][x] + 1 + z
    
            
print(reach[gy][gx])