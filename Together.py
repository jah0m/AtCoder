n = int(input())
a = [int(x) for x in input().split()]
ans = 0

c = []
for x in a:
    c.append(x-1)
    c.append(x)
    c.append(x+1)
l = [0] * (max(c)+2)
for i in c:
    l[i+1] += 1
ans = max(l)
print(l)
print(ans)