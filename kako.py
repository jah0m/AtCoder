s = input()
list = [0] * (len(s)+1)

for i in range(len(s)):
    if s[i] == '<':
        list[i+1] = list[i] + 1
for i in range(len(s)-1, -1, -1):
    if s[i] == '>':
        list[i] = max(list[i+1] +1, list[i])
print(sum(list))