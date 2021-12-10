n = int(input())
an = [int(x) for x in input().split()]


b = [0] * n
if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            b[(n+i) // 2] = an[i]
        else:
            b[(n-i)// 2] = an[i]
else:
    for i in range(n):
        if i % 2 == 0:
           b[(n-i)// 2] = an[i] 
        else:
            b[(n+i) // 2] = an[i]
print(*b)