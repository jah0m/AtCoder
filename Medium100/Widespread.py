import math
n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]

def check(list, x):
    global n, a, b
    cnt = 0
    cur = list.copy()
    for i in range(n):
        cur[i] -= x * b
        cur[i] = max(0, cur[i])
        if cur[i] > 0:
            cnt += math.ceil(cur[i] / (a-b))
    if cnt <= x: return True
    else: return False

l = 0
r = max(h)
mid = (r + l) // 2
while r-l > 1:
    mid = (r+l) // 2
    if check(h, mid): 
        r = mid
    else: 
        l = mid
if(check(h, mid)): print(mid)
else: print(mid+1)