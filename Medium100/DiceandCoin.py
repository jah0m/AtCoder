N, K = map(int, input().split())
ans = 0
sum = 0
def func(a, b):
    cnt = 0
    while a< b:
        a = a*2
        cnt += 1
    return cnt

for i in range(N):
    t = func(i+1, K)
    p = 1/N * ((1/2) ** t)
    ans += p
print(ans)