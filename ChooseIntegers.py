a, b, c = map(int, input().split())

l = set()
n = 1
while True:
    d = n * a % b
    if d == c: 
        ans = 'YES'
        break
    else:
        if d not in l:
            l.add(d)
            n += 1
        else: 
            ans = 'NO'
            break
print(ans)