N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

for i in range(P,Q+1):
    for j in range(R,S+1):
        ok = False
        if i-A == j-B:
            if i-A >= max(1-A,1-B) and i-A <= min(N-A,N-B):
                ok = True
        if i-A == B-j:
            if i-A >= max(1-A,B-N) and i-A <= min(N-A,B-1):
                ok = True
        if ok:
            print('#',end='')
        else:
            print('.',end='')
    print('')