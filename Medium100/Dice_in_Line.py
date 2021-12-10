n, k = map(int, input().split())
pn = [int(x) for x in input().split()]

sum_ = sum(pn[:k])
max_ = sum_
for i in range(k,n):
    sum_ += pn[i] - pn[i-k]
    max_ = max(max_, sum_)
ans = (max_ + k) / 2
print(ans)