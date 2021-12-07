n = int(input())
an = [int(x) for x in input().split()]
cnt = 0
pre = 0
for i in range(n):
    if i == 0:
        continue
    cur = an[i] - an[i-1]
    if cur * pre >= 0:
        if cur != 0:
            pre = cur
    else:
        cnt += 1
        pre = 0
ans = cnt + 1
print(ans)