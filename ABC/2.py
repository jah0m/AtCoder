from collections import Counter
N, M = map(int, input().split())
an = [int(x) for x in input().split()]
bm = [int(x) for x in input().split()]

cnta = Counter(an)
cntb = Counter(bm)

for key in cntb:
    if key not in cnta or cnta[key]<cntb[key]:
        print('No')
        exit()
print('Yes')
