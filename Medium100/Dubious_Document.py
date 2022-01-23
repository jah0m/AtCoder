from collections import Counter
n = int(input())
sn = [[x for x in input()] for _ in range(n)]

arr = [50] * 26

for ai in sn:
    cnt = Counter(ai)
    for i in range(26):
        arr[i] = min(arr[i], cnt[chr(i+97)])

for i in range(26):
    c = arr[i]
    for j in range(c):
        print(chr(i+97),end='')