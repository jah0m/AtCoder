n = int(input())
bn = [int(x) for x in input().split()]

ans = []
while True:
    flg = False
    for i in range(len(bn))[::-1]:
        if bn[i] == i+1:
            ans.append(bn.pop(i))
            flg = True
            break
    if flg is False:
        break
ans.reverse()
if len(bn) > 0:
    print(-1)
else:
    print(*ans,sep='\n')