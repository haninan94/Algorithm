T = 10

for test_case in range(1, T + 1):

    N = int(input())
    passwords = list(map(int, input().split()))

    while passwords[-1] != 0:
        for i in range(1, 6):
            temp = passwords[0] - i
            if temp <= 0:
                passwords.append(0)
                passwords.pop(0)
                break
            else:
                passwords.append(passwords.pop(0) - i)
    print(f'#{test_case}', *passwords)