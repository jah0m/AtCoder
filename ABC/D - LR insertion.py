from collections import deque
N = int(input())
S = input()

dq = deque([N])

for i in range(0, N)[::-1]:
    if S[i] == 'L':
        dq.append(i)
    else:
        dq.appendleft(i)
print(*dq)