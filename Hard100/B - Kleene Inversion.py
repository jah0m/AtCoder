n, k = map(int, input().split())
an = [int(x) for x in input().split()]
mod = 10**9 + 7
cnt1 = 0
for i in range(n):
    for j in range(i+1,n):
        if an[i] > an[j]:
            cnt1 += 1

cnt2 = 0
for i in range(n):
    for j in range(n):
        if an[i] > an[j]:
            cnt2 += 1

ans = cnt1 * k + cnt2 * (k*(k-1))//2
print(ans % (mod))