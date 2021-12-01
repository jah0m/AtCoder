h, w = map(int, input().split())
a = [[x for x in input()] for _ in range(h)]

def get_row_sum(a):
    sum = [0] * len(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == '#': sum[i] += 1
    return sum

def get_col_sum(a):
    sum = [0] * len(a[0])
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == '#': sum[j] += 1
    return sum
# rowSum = get_row_sum(a)
# print(rowSum)
# de =[]
# for r in range(len(rowSum)):
#     if rowSum[r] = 0:
#         de.append(r)
# print(de)

while 0 in (get_row_sum(a) or 0 in get_row_sum(a)) and len(a) > 1:
    rowSum = get_row_sum(a)
    colSum = get_col_sum(a)
    de =[]
    for r in range(len(rowSum)):
        if rowSum[r] == 0:
            de.append(r)
    for i in reversed(de):
        del a[i]
    de = []
    for c in range(len(colSum)):
        if colSum[c] == 0:
            de.append(c)
    for i in reversed(de):
        for l in a:
            del l[i]

for k in a:
    print(*k,sep='')