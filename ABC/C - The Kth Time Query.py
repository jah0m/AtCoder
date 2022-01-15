n, q = map(int, input().split())
an = [int(x) for x in input().split()]
xkq = [[int(x) for x in input().split()] for _ in range(q)]

arr = {}

for i in range(n):
    if an[i] not in arr:
        arr[an[i]] = [i]
    else:
        arr[an[i]].append(i)

for xki in xkq:
    x = xki[0]
    y = xki[1]
    if x in arr:
        if len(arr[x]) >= y:
            print(arr[x][y-1] + 1)
        else:
            print(-1)
    else:
        print(-1)