s = input()
k = int(input())

n = len(s)
ans = 0
sum = [0]

        
for i in range(n):
    sum.append(sum[i] + (1 if s[i] == '.' else 0))
r = 0
for l in range(n):
    while r < n and sum[r+1]-sum[l] <= k:
        print(r)
        r += 1
    ans = max(ans, r - l)
print(ans)
