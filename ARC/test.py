from collections import deque

n = int(input())
pn = [int(x) for x in input().split()]
qn = [int(x) for x in input().split()]

stack = deque()
stack.append([0,0])

reach = [[0 for _ in range(n)] for _ in range(n)]
ans = 0
pre = 0
while stack:
    print(stack)
    pi, qi = stack.popleft()
    cnt = reach[pi][qi]
    if qn[qi] % pn[pi] == 0:
        if pi+1 < n:
            stack.append([pi+1,pre])
            reach[pi][qi] = cnt + 1
            pre = qi
            if qi+1 < n:
                stack.append([pi+1,qi+1])
    else:
        if qi+1 < n:
            stack.append([pi,qi+1])
        elif pi+1 < n:
            stack.append([pi+1,pre])

print(reach)

    
