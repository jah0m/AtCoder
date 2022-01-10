x = int(input())

def ok(n):
    n = str(n)
    sa = int(n[1]) - int(n[0])
    for i in range(2,len(n)):
        if int(n[i]) - int(n[i-1]) != sa:
            return False
    return True

if len(str(x)) <= 2:
    print(x)
elif len(str(x)) > 10:
    for i in range(len(str(x))):
        print(9,end='')