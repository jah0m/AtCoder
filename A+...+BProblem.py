n, a, b = map(int, input().split())
min_ = (n-1) * a + b
max_ = (n-1) * b + a
print(max((max_ - min_ + 1), 0))