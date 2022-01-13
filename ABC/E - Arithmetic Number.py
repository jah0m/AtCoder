from collections import *
x = int(input())
dq = deque(range(1,100))

while dq:
    num = dq.popleft()
    if num >= x:
        print(num)
        exit()
    if num >= 10:
        r1 = num % 10
        r2 = (num // 10) % 10
        d = r1 - r2
        n = r1 + d
        if 0 <= n <= 9:
            dq.append(num * 10 + n)

