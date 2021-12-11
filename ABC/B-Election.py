from collections import Counter
n = int(input())
sn = [input() for _ in range(n)]
 
c = Counter(sn)
print(c.most_common(1)[0][0])