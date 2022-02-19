n, m = map(int, input().split())
sn = [x for x in input().split()]
tm = [x for x in input().split()]
d = {}
for si in sn:
    d[si] = 0
for ti in tm:
    d[ti] = 1

for key in d:
    if d[key] == 1:
        print('Yes')
    else:print('No')
