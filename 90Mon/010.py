n = int(input())
a = [[int(x) for x in input().split()] for _ in range(n)]

q = int(input())
qs = [[int(x) for x in input().split()] for _ in range(q)]
ans = []

sum1 = [0] * (n+1)
sum2 = [0] * (n+1)
for i in range(1, n+1):
    sum1[i] = sum1[i-1]
    sum2[i] = sum2[i-1]
    if a[i-1][0] == 1: sum1[i] += a[i-1][1]
    else: sum2[i] += a[i-1][1]

for k in qs:
    score1 = sum1[k[1]] - sum1[k[0]-1]
    score2 = sum2[k[1]] - sum2[k[0]-1]
    ans.append([score1, score2])

for x in ans:
    print(*x)