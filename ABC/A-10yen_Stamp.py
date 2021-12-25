import math
x, y = map(int, input().split())
if x >= y:
    print(0)
else:
    print(math.ceil((y-x) / 10))