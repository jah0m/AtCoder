s = input()
l = [x for x in s]

cnt = 0
ans = 0
for i in range(len(s)-1, -1, -1):
    if l[i] == 'B':
        ans += len(s) - 1 - i - cnt
        cnt += 1
print(ans)