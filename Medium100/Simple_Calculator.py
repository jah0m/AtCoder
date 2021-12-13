x, y = map(int, input().split())
if y > x:
    if x * y >= 0:
        ans = y-x
    else:
        ans = 1 + abs(y+x)
else:
    if x * y > 0:
        ans = 2 + abs(x-y)
    else:
        ans = 1 + abs(x+y)
print(ans)