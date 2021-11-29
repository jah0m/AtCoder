n, a, b = map(int, input().split())
sum = 0
for i in range(1, n+1):
    c = 0
    for s in str(i):
        c += int(s)
    if c >= a and c <= b: sum += i
print(sum)
