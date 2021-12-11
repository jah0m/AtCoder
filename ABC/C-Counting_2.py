import bisect

n, q = map(int, input().split())
an = [int(x) for x in input().split()]
xn = [int(input()) for _ in range(q)]

an.sort()

for xi in xn:
    num = bisect.bisect_left(an, xi)
    print(n-num)