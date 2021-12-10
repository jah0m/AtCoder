n, m = map(int, input().split())
students = [[int(x) for x in input().split()] for _ in range(n)]
points = [[int(x) for x in input().split()] for _ in range(m)]

def getDis(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def getPoint(x1, y1):
    minIndex = 0
    minDis = 10 ** 9
    for i in range(m):
        dis = getDis(x1, y1, points[i][0], points[i][1])
        if dis < minDis:
            minIndex = i
            minDis = dis
    return minIndex + 1

ans = [0] * n

for i in range(n):
    ans[i] = getPoint(students[i][0], students[i][1])
print(*ans,sep='\n')