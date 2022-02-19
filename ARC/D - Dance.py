from itertools import combinations
from itertools import product
from itertools import permutations
n = int(input())

an = [[int(x) for x in input().split()] for _ in range(n*2-1)]
#print(an)
arr = range(1,n*2+1)
ans = 0
groups = [[] for _ in range(2**n - 1)]

# a = list(permutations(arr,2))
# print(a)
for _ in range(2**n - 1):
    for x in permutations(arr, 2):
        print(x)
        flg = False
        i = 0
        while flg != True:
            x0 = x[0]
            x1 = x[1]
            if x1 not in groups[i] and x0 not in groups[i]:
                groups[i].append(x0)
                groups[i].append(x1)
                flg = True
            else:
                if i < n:
                    i += 1
                else:break
            
print(groups)

# for group in groups:
#     cnt = 0
#     for num in range(n*2)[::2]:
#         i = min(group[num],group[num+1])
#         j = max(group[num],group[num+1])
#         cnt += an[i-1][j-i-1]
#     ans = max(ans,cnt)
# print(ans)

# for x in permutations(arr):
#     cnt = 0
#     #print(x)
#     for num in range(n*2)[::2]:
#         i = min(x[num],x[num+1])
#         j = max(x[num],x[num+1])
#         #print(i,j)
#         cnt += an[i-1][j-i-1]
#     ans = max(ans, cnt)
# print(ans)