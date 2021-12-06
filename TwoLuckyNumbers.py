a = int(input())
b = int(input())
ans = 0
a2 = 2*a
# print('a2:{}'.format(a2))
bSize = len(str(b))
flg = False
if str(b) in str(a2):
    ans = a
else:
    for i in range(bSize):
        # print(i)
        # print(str(b)[:i+1])
        # print(str(a2)[-i-1:])
        if str(b)[-i-1:] == str(a2)[:i+1]:
            # print(str(b)[-i-1:])
            # print(str(a2)[:i+1])
            temp = str(int(str(b)[:i+1])) + str(a2)
            if int(temp) / 2 < 10 ** 18:
                ans = int(temp)//2
                break
        if str(b)[:i+1] == str(a2)[-i-1:]:
            temp = str(a2) + str(int(str(b)[i+1:]))
            if int(temp) / 2 < 10 ** 18:
                ans = int(temp)//2
                break
    temp = str(b) + str(a2)
    if int(temp) / 2 < 10 ** 183:
        if str(a) in str(int(temp)//2):
            ans = int(temp)//2
            flg = True
    if flg == False:
        temp = str(a2) + str(b)
        if int(temp) / 2 < 10 ** 18:
            while int(temp) %2 != 0:
                temp += '0'
            ans = int(temp)//2
        
print(ans)