l, r = map(int, input().split())
ans = 99999999999
for i in range(l, r+1):
    if ans == 0: break
    a = i % 2019
    if a == 0:
        ans = 0
        break
    for j in range(i+1, r+1):
        b = j % 2019
        if b == 0:
            ans = 0
            break
        ans = min(ans, a*b%2019)
print(ans) 