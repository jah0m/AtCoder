import sys   
sys.setrecursionlimit(100000) 
n = int(input())
pn = [int(x) for x in input().split()]
qn = [int(x) for x in input().split()]

pos = [0] * (n+1)
for i in range(n):
    pos[qn[i]] = i

z = [10**9]*n
for i in pn:
    ls = []
    for j in range(i,n+1,i)
