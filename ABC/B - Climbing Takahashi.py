n = int(input())
hn = list(map(int, input().split()))

pre = 0
for hi in hn:
    cur = hi
    if cur <= pre:
        print(pre)
        exit()
    pre = cur
print(pre)