from collections import deque, defaultdict
n, k = map(int, input().split())
an = [int(x) for x in input().split()]

ans = 0
cnt_dict = defaultdict(int)
dq = deque([0])
sum = 0

for ai in an:
    sum += ai
    dq.append(sum)
    if sum == k:
        ans += 1
    ans += cnt_dict[sum-k]
    cnt_dict[sum] += 1
    
print(ans)