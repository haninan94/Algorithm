H, M = map(int, input().split())

if M >= 45:
    M -= 45
    print(H, M)
elif M < 45:
    M = (M-45)%60
    if H == 0:
        H = 23
    else:
        H -=1
    print(H, M)