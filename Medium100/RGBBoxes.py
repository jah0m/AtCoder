R, G, B, N = map(int, input().split())
cnt = 0
for r in range(N//R+1):
    for g in range((N - r*R) // G + 1):
        b = (N-r*R-g*G) / B
        if b >= 0 and b == int(b):
            cnt += 1
print(cnt)