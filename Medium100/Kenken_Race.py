n, a, b, c, d = map(int, input().split())
s = [x for x in input()]

ans = 'No'
while True:
    aMove = False
    bMove = False
    s[a-1] = 'a'
    s[b-1] = 'b'
    #print(*s)
    if d > c:
        if a != c:
            if s[a] == '.':
                aMove = True
                s[a-1] = '.'
                s[a] = 'a'
                a += 1
            elif s[a+1] == '.':
                aMove = True
                s[a-1] = '.'
                s[a+1] = 'a'
                a += 2
    else:
        if a != c:
            if s[a+1] == '.':
                aMove = True
                s[a-1] = '.'
                s[a+1] = 'a'
                a += 2
            elif s[a] == '.':
                aMove = True
                s[a-1] = '.'
                s[a] = 'a'
                a += 1
    if b!= d and aMove is False:
        if s[b] == '.':
            bMove = True
            s[b-1] = '.'
            s[b] = 'b'
            b += 1
        elif s[b+1] == '.':
            bMove = True
            s[b-1] = '.'
            s[b+1] = 'b'
            b += 2
    
    #print(*s)
    if a == c and b == d:
        ans = 'Yes'
        break
    elif a!=c and b!=d:
        if aMove is False and bMove is False:
            ans = 'No'
            break
    elif a == c and aMove is not True and bMove is False:
        ans = 'No'
        break
    elif b == d and aMove is False and bMove is not True:
        ans = 'No'
        break

print(ans)
