h, w = map(int, input().split())
an = [[x for x in input()] for _ in range(h)]
cnt = 0
ans = 'Possible'
for ai in an:
    if ai.count('#') > w-cnt:
        ans = 'Impossible'
        break
    
    cnt += ai.count('#') - 1
print(ans)