s = input()
if len(s) == 26:
    for i in range(26)[::-1]:
        if s[i-1] < s[i]:
            num = ord(s[i-1])
            s = s[:i-1]
            for l in range(1,26):
                if chr(num+l) not in s:
                    s += chr(num+l)
                    print(s)
                    exit()
    print(-1)
else:
    arr = [False] * 26
    for word in s:
        n = ord(word)
        arr[n-97] = True
    for i in range(27):
        if arr[i] == False:
            ans = s + chr(i+97)
            print(ans)
            exit()