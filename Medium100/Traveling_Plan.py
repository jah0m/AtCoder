n = int(input())
an = [int(x) for x in input().split()]

sum = 0
pre = 0
for ai in an:
    sum += abs(ai - pre)
    pre = ai
sum += abs(0 - pre)

for i in range(n):
    ans = sum
    if i == 0:
        ans -= abs(an[i]) + abs(an[i+1] - an[i])
        ans += abs(an[i+1])
    elif i == n-1:
        ans -= abs(an[i]) + abs(an[i] - an[i-1])
        ans += abs(an[i-1])
    else:
        ans -= abs(an[i] - an[i-1]) + abs(an[i+1] - an[i])
        ans += abs(an[i+1] - an[i-1])
    print(ans)