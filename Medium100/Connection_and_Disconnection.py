s = input()
k = int(input())

if len(set(s)) == 1:
    print(len(s) * k // 2)
    exit()
cnt = 0
pre = ''
for i in range(len(s)):
    if s[i] == pre:
        cnt += 1
        pre = ''
    else:
        pre = s[i]
ans = cnt * k
#print(ans)
if s[0] == s[-1]:
    a = 0
    b = 0
    for i in range(len(s)):
        if s[i] == s[0]:
            a += 1
        else: break
    for i in range(len(s)-1,-1,-1):
        if s[i] == s[0]:
            b += 1
        else: break
    
    ans -= (a // 2 + b // 2 - (a+b)//2) * (k-1)

print(ans)