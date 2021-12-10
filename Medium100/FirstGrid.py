s1 = input()
s2 = input()

l1 = [x for x in s1]
l2 = [x for x in s2]

bpos = []
wpos = []
for i in range(2):
    if l1[i] == '#': bpos.append([0, i])
    else: wpos.append([1, i])
    if l2[i] == '.': wpos.append([2, i])
    else: bpos.append([2, i])

def isRight(bpos):
    if len(bpos) >= 3:
        return 'Yes'
    elif bpos[0][1] == bpos[1][1] or bpos[0][0] == bpos[1][0]: return 'Yes'
    return 'No'

print(isRight(bpos))
