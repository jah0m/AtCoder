from typing import Sized


a, b = map(int, input().split())

def intTolist(n):
    l = []
    for x in str(n):
        l.append(int(x))
    return l

l1 = intTolist(a)
l2 = intTolist(b)
l1.reverse()
l2.reverse()
size = min(len(l1), len(l2))

ans = 'Hard'
for i in range(size):
    if l1[i] + l2[i] < 10:
        ans = 'Easy'
    else: 
        ans = 'Hard'
        break

print(ans)
