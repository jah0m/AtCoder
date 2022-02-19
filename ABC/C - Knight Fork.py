x1, y1, x2, y2 = map(int,input().split())

for i in range(x1-5, x1+6):
    for j in range(y1-5, y1+6):
        if (x1-i)**2 + (y1-j)**2 == 5 and (x2-i)**2 + (y2-j)**2 == 5:
            print('Yes')
            exit()
print('No')