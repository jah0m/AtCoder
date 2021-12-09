from collections import Counter
s = input()
c = Counter(s)
ca = c['a']
cb = c['b']
cc = c['c']

if max(ca, cb, cc) - min(ca, cb ,cc) > 1:
    ans = 'NO'
else: ans = 'YES'
print(ans)