c = [[int(x) for x in input().split()] for _ in range(3)]
ans = 'Yes'
l = []
for i in c:
    l.append([i[0] - i[1], i[0] - i[2]])
l1 = []
for j in range(3):
    l1.append([c[1][j] - c[0][j], c[2][j] - c[1][j]])

if l[0] == l[1] and l[1] == l[2] and l1[0] == l1[1] and l1[1] == l1[0]:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)