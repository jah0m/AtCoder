n = int(input())
a = [int(input()) for _ in range(n)]

cnt = 0
i = 0
ans = n

while True:
    i = a[i]-1
    cnt += 1
    if i == 1:
        ans = cnt
        break
    if cnt >= n:
        ans = -1
        break

print(ans)