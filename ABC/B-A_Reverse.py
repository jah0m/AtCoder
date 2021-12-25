l, r = map(int, input().split())
s = [x for x in input()]
a = s[:l-1]
b = s[l-1:r]
c = s[r:]
b = reversed(b)

print(*a,sep='',end='')
print(*b,sep='',end='')
print(*c,sep='',end='')