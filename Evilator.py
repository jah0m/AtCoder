sn = [x for x in input()]
ans = 0
for i in range(len(sn)):
    if sn[i] == 'U':
        ans += i*2 + (len(sn) - i - 1) * 1
    else:
        ans += i*1 + (len(sn) - i - 1) * 2
print(ans)