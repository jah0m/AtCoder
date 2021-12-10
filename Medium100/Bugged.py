n = int(input())
s = [int(input()) for _ in range(n)]

s.sort()
ans = sum(s)
for i in s:
    if ans % 10 != 0: break
    else:
        if i % 10 != 0: ans -= i
if ans % 10 == 0:
    ans = 0
print(ans)