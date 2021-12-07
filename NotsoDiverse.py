n, k = map(int, input().split())
an = [int(x) for x in input().split()]

l =[0] * n

for ai in an:
    l[ai - 1] += 1
l.sort()
print(sum(l[:n-k]))