s = [x for x in input()]
t = [x for x in input()]

s.sort()
t.sort()
n = min(len(s), len(t))
ans = 'No'
for i in range(n):
    if s[i] < t[-1-i]:
        ans = 'Yes'
        break
    if i == n-1 and len(s) < len(t) and  s[i] == t[-1-i]:
        ans = 'Yes'
print(ans)