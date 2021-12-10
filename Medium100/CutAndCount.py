n = int(input())
s = input()
ans = 0
for i in range(n):
    cnt = 0
    left = set(s[:i])
    right = set(s[i:])
    for key in left:
        if key in right: cnt += 1
    ans = max(ans, cnt)
print(ans)