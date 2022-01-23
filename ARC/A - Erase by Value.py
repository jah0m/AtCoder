n = int(input())
an = [int(x) for x in input().split()]

pre = an[0]
for i in range(n):
    cur = an[i]
    if cur < pre:
        break
    elif cur > pre:
        pre = cur

for n in an:
    if n != pre:
        print(n,end=' ')