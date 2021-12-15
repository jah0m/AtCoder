n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = [x for x in input()]

ans = 0
arr = [0] * n
for i in range(n):
    if i < k:
        arr[i] = 1
        if t[i] == 'r': 
            ans += p
        elif t[i] == 's': 
            ans += r
        else: 
            ans += s
    else:
        if t[i] == t[i-k]:
            if arr[i-k] != 1:
                arr[i] =1
                if t[i] == 'r': 
                    ans += p
                elif t[i] == 's': 
                    ans += r
                else: 
                    ans += s
        else:
            arr[i] =1
            if t[i] == 'r': 
                ans += p
            elif t[i] == 's': 
                ans += r
            else: 
                ans += s
    #print(ans)
print(ans)
