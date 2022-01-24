from collections import deque
n = int(input())
an = [[0]*n*2 for _ in range(n*2-1)]
for i in range(2*n - 1):
    arr = [int(x) for x in input().split()]
    an[i][i+1:] = arr
ans = 0
def dfs(res, xor):
    global ans
    if len(res) == 0:
        ans = max(ans, xor)
        return
    now = res[0]
    for i in range(1,len(res)):
        pair = res[i]
        new_res = [i for i in res if i != now and i!= pair]
        dfs(new_res, xor^an[now][pair])

dfs(range(n*2), 0)
print(ans)