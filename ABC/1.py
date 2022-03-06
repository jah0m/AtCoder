arr = list(map(int, input().split()))
ans = 0
for _ in range(3):
    ans = arr[ans]
print(ans)