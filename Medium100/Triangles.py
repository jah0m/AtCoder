import itertools
n = int(input())
ln = [int(x) for x in input().split()]
cnt = 0
for i in itertools.combinations(ln, 3):
    a = i[0]
    b = i[1]
    c = i[2]

    if a < b+c and b < c+a and c < a+b:
        cnt += 1
print(cnt)