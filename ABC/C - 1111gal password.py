N = int(input())
for i in range(10**(N-1), 10**N):
    s = str(i)
    s = [x for x in s]
    print(s)
