n = int(input())
s = input()
t = input()
cnt = 0
for i in range(1,n):
    if s[-i:] == t[:i]:
        cnt = i
if cnt == 0:
    text = s + t
else :
    text = s[:-cnt] + t
if s == t:
    text = s
print(len(text))