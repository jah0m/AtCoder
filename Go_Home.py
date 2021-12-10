x = int(input())

def get_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

for i in range(1, x+1):
    if get_sum(i) >= x: 
        print(i)
        break
