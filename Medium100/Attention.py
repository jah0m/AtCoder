n = int(input())
s = input()

arr = []
w = 0
e = 0
ans = n
for k in s:
    if k == 'W':
        w += 1
    else: e += 1
    arr.append([w,e])

for i in range(n):
    if i == 0:
        left = [0,0]
    else:
        left = arr[i-1]
    right = [arr[n-1][0] - arr[i][0], arr[n-1][1] - arr[i][1]]
    ans = min(ans, left[0]+right[1])
print(ans)