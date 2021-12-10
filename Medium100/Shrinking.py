s = input()
ans = 1000
for c in s:
    #c = chr(ord('a')+i)
    cur = []
    pre = [x for x in s]
    cnt = 0
    while pre.count(c) != len(pre):
        #print(pre.count(c))
        #print(len(pre))
        for j in range(len(pre)-1):
            if pre[j] == c:
                cur.append(pre[j])
            else: cur.append(pre[j+1])
        cnt += 1
        pre = cur.copy()
        cur = []
        #print(pre)
    ans = min(ans, cnt)
print(ans)