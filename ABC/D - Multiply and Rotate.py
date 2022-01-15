from collections import *
a, n = map(int, input().split())
m = 1
while m <= n:
    m *= 10

def list_to_int(dq):
    word = ''
    for i in dq:
        word += i
    return int(word)
def rotate(n):
    dq = deque([x for x in str(n)])
    dq.appendleft(dq.pop())
    return list_to_int(dq)

queue = deque([1])
seen =[-1] * m
seen[1] = 0

while queue:
    num = queue.popleft()
    cnt = seen[num]

    cur = num * a
    if cur < m and seen[cur] == -1:
        queue.append(cur)
        seen[cur] = cnt + 1
    
    if num >= 10 and num % 10 != 0:
        cur = rotate(num)
        if cur < m and seen[cur] == -1:
            queue.append(cur)
            seen[cur] = seen[num] + 1
print(seen[n])