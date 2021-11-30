n = int(input())
a = map(int, input().split())

list = [0] * 8
red = 0
ans = [0, 0]
for i in a:
    c = i // 400
    if c > 7: red += 1
    else: list[c] = 1

ans[0] = (max(sum(list), 1))
ans[1] = sum(list) + red
print(*ans)