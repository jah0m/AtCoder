from math import *
n = int(input())
xyn = [[int(x) for x in input().split()] for _ in range(n)]

def getDis(p1, p2):
    return (p1[0]-p2[0]) ** 2 + (p1[1]-p2[1])**2
ans = 0
for i in range(n):
    for j in range(i+1,n):
        ans = max(ans, getDis(xyn[i], xyn[j]))

print(sqrt(ans))