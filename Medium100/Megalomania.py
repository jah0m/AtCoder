n = int(input())
ab = [[int(x) for x in input().split()] for _ in range(n)]

# for i in range(n):
#     ab[i][0], ab[i][1] = ab[i][1], ab[i][0]
def takeSecond(elem):
    return elem[1]
ab.sort(key=takeSecond)
t = 0
ans = 'Yes'
for k in ab:
    t += k[0]
    if t > k[1]:
        ans = 'No'
        break
print(ans)