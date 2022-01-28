import heapq
from re import T
N, M = map(int, input().split())
an = [int(x) for x in input().split()]
heapq.heapify(an)

arr = []
for _ in range(M):
    b, c = map(int, input().split())
    arr.append([b, c])
arr.sort(key=lambda x : x[1], reverse=True)

for b, c in arr:
    for _ in range(b):
        x = heapq.heappop(an)
        if x < c:
            heapq.heappush(an,c)
        else:
            heapq.heappush(an,x)
            break

print(sum(an))  