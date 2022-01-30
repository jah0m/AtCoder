from collections import defaultdict
from collections import deque
from string import ascii_lowercase as alp #a~z
N = int(input())
S = input()

pos = defaultdict(deque)

for i, s in enumerate(S):
    pos[s].append(i)


ans = list(S)
last = N
for s in S:
    if not pos[s]:
        break
    i = pos[s].popleft()

    swap = False
    for a in alp: #a~z
        if a == s:
            swap = True
            break
        while pos[a] and pos[a][-1] >= last:
            pos[a].pop()
        if not pos[a]:
            continue

        swap = True
        j = pos[a].pop()
        ans[i], ans[j] = ans[j], ans[i]
        last = j
        break
    if not swap:
        break
print(''.join(ans))
