n = int(input())
an = [int(x) for x in input().split()]

minCost = 10 ** 99

for i in range(min(an), max(an)+1):
    cost = 0
    for ai in an:
        cost += (ai-i) ** 2
    minCost = min(minCost, cost)
print(minCost)
