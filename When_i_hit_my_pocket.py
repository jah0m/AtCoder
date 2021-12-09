k, a, b = map(int, input().split())

ans1 = 1 + k
ans2 = 0
if k >= a+1:
    ans2 = a
    k -= (a-1)
    ans2 += k % 2 + k // 2 * (b-a)
print(max(ans1, ans2))