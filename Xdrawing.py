N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
ans = []
#l = [['.']* (S-R+1)] * (Q-P+1)
# l = ['.'] *(Q-P+1)
# for i in range(len(l)):
#     l[i] = ['.'] * (S-R+1)
l = ['.'] * (Q-P+1)
for i in range(len(l)):
    l[i] = ['.'] * (S-R+1)
ma = 10 ** 50
mb = 10 ** 50
for k in range(max(1-A,1-B,P-A,R-B), min(N-A, N-B,Q-A,S-B)+1, 1):
    ans.append([A+k, B+k])
    ma = min(ma, A+k)
    mb = min(mb, B+k)

for k in range(max(1-A,B-N,P-A,B-S), min(N-A, B-1,Q-A,B-R)+1, 1):
    ans.append([A+k, B-k])
    ma = min(ma, A+k)
    mb = min(mb, B-k)
for i in range(len(ans)):
    ans[i][0] -= ma
    ans[i][1] -= mb
for n in ans:
    i = n[0]
    j = n[1]
    l[i][j] = '#'

for k in l:
    print(*k,sep='')