from collections import deque
n, m , k = map(int, input().split())
arr = [[x for x in input()] for _ in range(n)]

boomM = set()
boomN = set()
safe = deque()
boomed = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'B':
            boomM.add(j)
            boomN.add(i)

for i in range(n):
    for j in range(m):
        if arr[i][j] != 'B':
            if i in boomN or j in boomM:
                boomed.append(arr[i][j])
            else:
                safe.append(arr[i][j])

safe = deque(sorted(safe))
boomed = deque(sorted(boomed))

for _ in range(k):
    minSafe = safe.popleft()
    maxBoomed = boomed.pop()
    if minSafe < maxBoomed:
        boomed.appendleft(minSafe)
        safe.append(maxBoomed)
    else:
        boomed.append(maxBoomed)
        safe.appendleft(minSafe)
        break
safe = [int(x) for x in safe]
print(sum(safe))