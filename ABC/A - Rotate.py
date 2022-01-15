x = input()
a = x[0]
b = x[1]
c = x[2]

ans = int(a+b+c) + int(b+c+a) + int(c+a+b)
print(ans)