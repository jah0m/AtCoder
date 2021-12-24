s = input()

pre = s[0]
cnt = 0
for key in s:
    if key != pre:
        cnt += 1
    pre = key
print(cnt)