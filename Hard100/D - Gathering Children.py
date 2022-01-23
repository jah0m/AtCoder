s = input()

arr = [0] * len(s)

r = 0
l = 0
pre = 'R'
point = 0
for i in range(len(s)):
    cur = s[i]
    if cur != pre:
        if pre == 'R':
            arr[i-1] += (r+1)//2
            arr[i] += r - (r+1)//2
            point = i
        else:
            arr[point] += (l+1)//2
            arr[point-1] += l - (l+1)//2

        r = 0
        l = 0
    
    
    if cur == 'R':
        r += 1
    else:
        l += 1
    pre = cur
    
if l != 0:
    arr[point-1] += l //2
    arr[point] += l - l//2
print(*arr)