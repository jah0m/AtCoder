s = [x for x in input()]
t = [x for x in input()]
ans = 'Yes'
if len(s) !=1 :
    if ord(t[0]) >= ord(s[0]):
        num = ord(t[0]) - ord(s[0])
    else:
        num = ord(t[0]) + 26 - ord(s[0])
    for i in range(len(t)):
        if ord(t[i]) >= ord(s[i]):
            num1 = ord(t[i]) - ord(s[i])
        else:
            num1 = ord(t[i]) + 26 - ord(s[i])
        if num1 != num:
            ans = 'No'
            break
print(ans)
