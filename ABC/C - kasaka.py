S = input()

l = 0
r = len(S)-1 

while l < r:
    if S[l] != S[r]:
        if S[r] == 'a':
            r -= 1
            continue
        else:
            print('No')
            exit()
    l += 1
    r -= 1
print('Yes')