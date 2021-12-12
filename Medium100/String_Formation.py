from collections import deque

s = deque([x for x in input()])
q = int(input())
cnt = 0
for _ in range(q):
    qi = input().split()
    if len(qi) == 1:
        cnt += 1
    else:
        if int(qi[1]) % 2 == cnt % 2:
            s.append(qi[2])
        else:
            s.appendleft(qi[2])

if cnt % 2 != 0:
    s.reverse()
print(*s, sep='')