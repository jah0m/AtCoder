from collections import deque
N = int(input())
an = [int(x) for x in input().split()]
dq = deque()

cur = 0
cnt = 0
for ai in an:
    if ai != cur:
        cur = ai
        cnt = 1
        dq.append(ai)
    else:
        cnt += 1
        dq.append(ai)
        if cnt == cur:
            for _ in range(cnt):
                dq.pop()
            if dq:
                cur = dq[-1]
            else:
                cur = 0
            cnt = 0
            for i in range(len(dq))[::-1]:
                if dq[i] == cur:
                    cnt += 1
                else:
                    break
            #print(cur, cnt)
    print(len(dq))