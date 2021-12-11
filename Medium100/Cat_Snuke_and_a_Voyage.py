n, m = map(int, input().split())
ab = [[int(x) for x in input().split()] for _ in range(m)]

ans = 'IMPOSSIBLE'

l1 = []
l2 = []
for i in ab:
    if i[0] == 1:
        l1.append(i[1])
    if i[1] == n:
        l2.append(i[0])

if set(l1) & set(l2):
    ans = 'POSSIBLE'
print(ans)