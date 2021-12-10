n, c, k = map(int, input().split())
tn = [int(input()) for _ in range(n)]

tn.sort()
cnt = 0
ans = 0
for i in range(n):
    if cnt == 0:
        end = tn[i] + k
    if tn[i] <= end:
        cnt += 1
        if cnt == c:
            ans += 1
            cnt = 0
    else:
        ans += 1
        cnt = 1
        end = tn[i] + k
if cnt != 0:
    ans += 1
print(ans)