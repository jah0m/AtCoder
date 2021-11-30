h, w = map(int, input().split())
a = [[x for x in input().split()] for _ in range(h)]

over = False
while not over:
    cnt = 0
    for i in range(h):
        if sum(a[i]) == 0: del(a[i])
        else: cnt += 1
            
    


