import statistics
n = int(input())
an = [int(x) for x in input().split()]
groups = []
maxAvg = 0
maxMed = 0
if (n % 2 == 0):
    for i in range(2 ** (n//2)):
        group = []
        for j in range(n//2):
            if (i >> j) & 1 == 1:
                group.append(an[2*j])
            else:
                group.append(an[2*j+1])
        #groups.append(group)
        maxAvg = max(maxAvg,sum(group)/len(group))
        maxMed = max(maxMed,statistics.median(group))
#print(groups)
print(maxAvg)
print(maxMed)



        