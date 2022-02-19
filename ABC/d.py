import sys

N = int(input())
S = input()
sys.setrecursionlimit(N * 10)

arr = [[-1,-1] for _ in range(N * 2)]
for i in range(1, N+1):
    k = S[i-1]
    if k == 'L':
        arr[i][1] = i-1
        if arr[i-1][0] != -1:
            l = arr[i-1][0]
            arr[l][1] = i
            arr[i-1][0] = i
            arr[i][0] = l
        else:
            arr[i-1][0] = i
    elif k == 'R':
        arr[i][0] = i-1
        if arr[i-1][1] != -1:
            r = arr[i-1][1]
            arr[r][0] = i
            arr[i-1][1] = i
            arr[i][1] = r
        else:
            arr[i-1][1] = i

def getNode(n):
    l = arr[n][0]
    if l == -1:
        return n
    else: 
        return getNode(l)

def printNode(n):
    print(n,end=' ')
    next = arr[n][1]
    if next != -1:
        printNode(next)
#print(arr)
printNode(getNode(N))