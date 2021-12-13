n = int(input())
an = [int(x) for x in input().split()]

arr = []
sum =0
for ai in an:
    sum += ai
    arr.append(sum)
ans = 10 ** 20
for i in range(n-1):
    ans = min(ans, abs(arr[i] - arr[n-1] + arr[i]))
print(ans)
