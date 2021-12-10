import math
a, b, c, d = map(int, input().split())
ans = b-a+1

c1 = b // c - (a-1) // c
c2= b // d - (a-1) // d
n = int(c*d/math.gcd(c,d))
#print('n{}'.format(n))
c3 = b // n - (a-1) // n
#print('{} {} {}'.format(c1, c2, c3))
ans -= (c1+c2-c3)
print(ans)