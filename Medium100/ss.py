s = input()

for i in range(len(s)-2, 0, -2):
    cur = s[:i]
    mid = i // 2
    if cur[:mid] == cur[mid:]:
        ans = len(cur)
        break
print(ans)