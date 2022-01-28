import heapq
N, M = map(int, input().split())
an = [int(x) for x in input().split()]

for i in range(len(an)):
    an[i] *= -1

heapq.heapify(an)
for _ in range(M):
    x = heapq.heappop(an)
    x = -x // 2 * -1
    heapq.heappush(an, x)

print(-sum(an))