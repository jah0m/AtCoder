import bisect'
from collections import Counter
Q = int(input())
arr = []
for _ in range(Q):
    query = [int(x) for x in input().split()]
    if len(query) == 2:
        n = query[1]
        arr.append(n)
    else:
        if query[0] == 3:
            n = query[1]
            k = query[2]
            cnt = Counter(arr)
            arr1 = []
            for key in cnt:
                arr1.append(key, cnt[key])
                
                

        else:
            n = query[1]
            k = query[2]
            arr.sort()
            index = bisect.bisect_right(arr, n)
            if index - k >= 0:
                print(arr[index-k])
            else:
                print(-1)
