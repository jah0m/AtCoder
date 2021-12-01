s = [x for x in input()]

key = ['k', 'e', 'y', 'e', 'n', 'c', 'e']
n = len(s) - len(key)
ans = 'NO'
for i in range(len(s) - n):
    cur = s.copy()
    del cur[i:i+n]
    if cur == key: ans = 'YES'
print(ans)