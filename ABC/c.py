S = input()
l = 0
r = len(S) - 1
# flg = True
# cnt = 0
# while True:
#     if S[r] == 'a':
#         cnt += 1
#         r -= 1
#     else:
#         break
# for _ in range(cnt):
#     S = 'a' + S
# l = 0
# r = len(S) - 1
while l < r:
    if S[l] != S[r]:
        if S[r] == 'a':
            r -= 1
            continue
        else:
            print('No')
            exit()
    else:
        l += 1
        r -= 1
print('Yes')
    