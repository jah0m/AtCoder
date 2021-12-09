n, p = map(int, input().split())
an = [int(x) for x in input().split()]

if sum([ai % 2 for ai in an]) == 0:
    if p == 0:
        print(2 ** n)
    else: print(0)
else:
    print(2 ** (n-1))

