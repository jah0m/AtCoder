n = int(input())
an = [int(x) for x in input().split()]

arr = [0] * n

for ai in an:
    arr[ai-1] += 1

print(arr.index(3)+1)