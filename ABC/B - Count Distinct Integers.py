from collections import Counter
N = int(input())
an = [int(x) for x in input().split()]

c = Counter(an)
print(len(c))
