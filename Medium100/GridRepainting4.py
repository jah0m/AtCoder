h, w = map(int, input().split())
c = [[x for x in input()] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if c[i][j] != '.': continue
        for n in range(1,6,1):
            n = str(n)
            if i != 0 :
                if c[i-1][j] == n: continue
            if i != h-1:
                if c[i+1][j] == n: continue
            if j != 0:
                if c[i][j-1] == n: continue
            if j != w-1:
                #print('{}{}'.format(i,j+1))
                if c[i][j+1] == n: continue
            c[i][j] = n
            break
for i in c:
    print(*i,sep='')