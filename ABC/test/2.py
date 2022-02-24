n, k = map(int, input().split())
s = input()
arr = []
ans = 0
cnt = 0
for key in s:
    if key == 'S':
        if cnt < 3:
            cnt += 1
        else:
            arr.append(cnt)
            cnt = 0
    else:
        arr.append(cnt)
        cnt = 0
        ans += 1
arr.append(cnt)
arr.sort(reverse=True)
for i in range(k):
    ans += arr[i]
print(ans)