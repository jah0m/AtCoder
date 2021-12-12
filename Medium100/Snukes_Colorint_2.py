w, h, n = map(int, input().split())
xyan = [[int(x) for x in input().split()] for _ in range(n)]

x1 = 0
x2 = w
y1 = 0
y2 = h

for xyai in xyan:
    x = xyai[0]
    y = xyai[1]
    a = xyai[2]
    if a == 1:
        x1 = max(x1, x)
    elif a == 2:
        x2 = min(x2, x)
    elif a == 3:
        y1 = max(y1, y)
    elif a == 4:
        y2 = min(y2, y)

if x2 <= x1 or y2 <= y1:
    print(0)
else:
    ans = (x2-x1) * (y2-y1)
    print(int(ans))