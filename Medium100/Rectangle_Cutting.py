w, h, x, y = map(int, input().split())

ans1 = w * h / 2
ans2 = 0
if x * 2 == w and y * 2 == h: ans2 = 1
print('{} {}'.format(ans1, ans2))