from collections import Counter

n = int(input())
sn = [sorted(input()) for _ in range(n)]
def listToStr(arr):
    newArr =[]
    for i in arr:
        char = ''
        for k in i:
            char += k
        newArr.append(char)
    return newArr
sn = listToStr(sn)
        
c = Counter(sn)
#print(c)
ans = 0 
for i in c.keys():
    if c[i] >= 2: 
        ans += (c[i] * (c[i] -1)) // 2
print(ans)