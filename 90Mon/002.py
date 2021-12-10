from itertools import product
n = int(input())

def isRight(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] =='(': cnt += 1
        if s[i] == ')': cnt -= 1
        if cnt < 0: return False
    return cnt == 0

s = ''
for s in product(['(', ')'],repeat=n):
    if isRight(s):
        print(*s, sep='')