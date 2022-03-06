import bisect
Q = int(input())
arr = []
for _ in range(Q):
    query = [int(x) for x in input().split()]
    if len(query) == 2:
        n = query[1]
        bisect.insort(arr, n)
    else:
        if query[0] == 3:
            n = query[1]
            k = query[2]
            index = bisect.bisect_left(arr, n)
            if index + k <= len(arr):
                print(arr[index+k-1])
            else:
                print(-1)
        else:
            n = query[1]
            k = query[2]
            index = bisect.bisect_right(arr, n)
            if index - k >= 0:
                print(arr[index-k])
            else:
                print(-1)
