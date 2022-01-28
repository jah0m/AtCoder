a, b, x = map(int, input().split())

x1 = b // x
x2 = a // x

if a % x == 0:
    print(x1-x2+1)
else:
    print(x1-x2)
