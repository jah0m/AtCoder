sa = list(input())
sb = list(input())
sc = list(input())

def dropCard(si, i):
    if len(si) == 0:
        print(i)
    else:
        next = si.pop(0)
        if next == 'a':
            dropCard(sa, 'A')
        elif next == 'b':
            dropCard(sb, 'B')
        else:
            dropCard(sc, 'C')

dropCard(sa, 'A')