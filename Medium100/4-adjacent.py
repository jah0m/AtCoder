n = int(input())
an = [int(x) for x in input().split()]

c4 = 0
c2 = 0
c = 0
ans = 'No'
for ai in an:
    if ai % 4 == 0:
        c4 += 1
    elif ai % 2 == 0:
        c2 += 1
    else: c += 1

if c <= c4: ans = 'Yes'
if c + c4 == n and c == c4+1: ans = 'Yes'
print(ans)