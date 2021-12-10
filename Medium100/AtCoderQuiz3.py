n = int(input())

if n >= 42:
    n += 1

if len(str(n)) == 1:
    ans = 'AGC' + '00' + str(n)
elif len(str(n)) == 2:
    ans = 'AGC' + '0' + str(n)
else:
    ans = 'AGC' + str(n)

print(ans)
