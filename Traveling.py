n = int(input())
s = []
oldTime = 0
oldPos = [0, 0]
flg = True
def getDis(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
for i in range(n):
    s.append([int(x) for x in input().split()])
for i in s:
    newTime = i[0]
    newPos = [i[1], i[2]]
    if getDis(oldPos, newPos) > (newTime - oldTime) or getDis(oldPos, newPos) % 2 != (newTime - oldTime) % 2:
        flg = False
        break 
    else:
        oldPos, oldTime = newPos, newTime
if flg: print('Yes') 
else: print('No')
    