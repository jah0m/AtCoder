n = int(input())
s = [int(x) for x in input().split()]
s = sorted(s, reverse=True)
an = 0

for i in range(n):
    if i % 2 == 0:
        an += s[i]
    else:
        an -= s[i]
print(an)