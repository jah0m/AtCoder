a, b = map(int, input().split())

if a+1 == b:
    print('Yes')
elif b == 10 and a == 1:
    print('Yes')
else:
    print('No')