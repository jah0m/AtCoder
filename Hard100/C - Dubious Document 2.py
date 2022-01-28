S = list(input())
T = list(input())

flg = False
cnt = 0
for i in range(len(S)-len(T)+1)[::-1]:
    if cnt == len(T):
        break
    cnt = 0
    for j in range(i,i+len(T)):
        if S[j] == T[j-i] or S[j] == '?':
            cnt += 1
        else:
            break
        if cnt == len(T):
            flg = True
            n = i
            break
if flg :
    S[n:n+len(T)] = T

    for k in S:
        if k == '?':
            print('a',end='')
        else:
            print(k,end='')
else:
    print('UNRESTORABLE')