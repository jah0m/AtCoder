from collections import Counter
n = int(input())
s = [x for x in input()]
ans = 1

cnt = Counter(s)

for k,v in cnt.items():
    ans *= v+1
    
print((ans-1) % (10**9+7))