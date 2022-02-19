a,b,c,d = map(int,input().split())
from math import sqrt
def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

for i in range(a, b+1):
    flg = False
    for j in range(c, d+1):
        if is_prime(i+j):
            flg = True
            break
    if flg is False:
        print('Takahashi')
        exit()
print('Aoki')
        