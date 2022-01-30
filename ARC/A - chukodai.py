s = [x for x in input()]
a, b = map(int, input().split())

a -= 1
b -= 1
temp = s[b]
s[b] = s[a]
s[a] = temp

for k in s:
    print(k,end='')