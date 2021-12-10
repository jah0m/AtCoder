n = int(input())
xn = [int(x) for x in input().split()]

group = xn.copy()
group.sort()

mid = (group[n//2] + group[n//2-1]) / 2

for xi in xn:
    if xi < mid:
        print(group[n//2])
    else:
        print(group[n//2 -1])
