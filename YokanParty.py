n, l = map(int, input().split())
k = int(input())
a = [int(x) for x in input().split()]

def solve(mid):
    cnt = 0
    pre = 0
    global n, l, k, a
    for i in range(n):
        if a[i] - pre >= mid and l-a[i] >= mid:
            cnt += 1
            pre = a[i]
    if cnt >= k: return True
    return False

left = 0
right = l
mid = (left+right) // 2
while True:
    mid = (left+right) // 2
    if  solve(mid): left = mid
    else: right = mid
    if right - left > 1: mid = (left+right) // 2
    else: 
        mid = left
        break

print(mid)