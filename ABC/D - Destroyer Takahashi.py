N, D = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x : x[1])
#print(arr)
ans = 0
pre = 0
for i in arr:
    if i[0] > pre:
        ans += 1
        pre = i[1] + D - 1

print(ans)

    