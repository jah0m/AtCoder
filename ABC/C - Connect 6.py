N = int(input())
grid = [[x for x in input()] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i - 5 >= 0 and j +6 <= N:
            cnt = 0
            for k in range(6):
                if grid[i-k][j+k] == "#":
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                exit()
                
        if j - 5 >= 0 and i +6 <= N:
            cnt = 0
            for k in range(6):
                if grid[i+k][j-k] == "#":
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                exit()
                        
        if i + 6 < N and j + 6 <= N:
            cnt = 0
            for k in range(6):
                if grid[i+k][j+k] == "#":
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                exit()
        if i - 5 >= 0 and j - 5 >= 0:
            cnt = 0
            for k in range(6):
                if grid[i-k][j-k] == "#":
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                exit()
        
        if j + 6 <= N:
            cnt = 0
            for k in range(6):
                if grid[i][j+k] == "#":
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                exit()
        if i + 6 <= N:
            cnt = 0
            for k in range(6):
                if grid[i+k][j] == "#":
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                exit()
            
print('No')