from math import gcd
n , m = map(int, input().split())
s = input()
t = input()

lcm = n * m // gcd(n, m)
ans = lcm
for k in range(gcd(n,m)):
    a = k * n//gcd(n,m)
    b = k * m//gcd(n,m)
    if s[a] != t[b]:
        ans = -1
        break
print(ans)