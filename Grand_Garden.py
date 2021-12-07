n = int(input())
hn = [int(x) for x in input().split()]

start = False
l = 0
r = len(hn)
cnt = 0
while sum(hn) > 0:
    l = 0
    r = len(hn)
    for i in range(len(hn)):
        if start == False:
            if hn[i] !=0:
                l = i
                start = True
        elif start == True:
            if hn[i] == 0:
                r = i
                break
    cnt += 1
    start = False
    #print('l{}r{}'.format(l,r))
    hn[l:r] = list(map(lambda x: x-1, hn[l:r]))
    #print(hn)
#print(hn)
print(cnt)