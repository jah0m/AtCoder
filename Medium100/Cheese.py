n, w = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(n)]

score = 0

a = sorted(a, reverse=True)
for i in a:
    if i[1] < w:
        score += i[0] * i[1]
        w -= i[1]
    else:
        score += i[0] * w
        break
print(score)
