T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    cards = list(input().split())

    if N % 2 == 0:
        front_of_cards = cards[: N // 2]
        back_of_cards = cards[N // 2 :]
        print(f'#{test_case}', end=' ')
        for i in range(N // 2):
            print(front_of_cards[i], back_of_cards[i], end=' ')
        print()
    else:
        front_of_cards = cards[: (N // 2) + 1]
        back_of_cards = cards[(N // 2) + 1 :]
        print(f'#{test_case}', end=' ')
        for i in range(N // 2):
            print(front_of_cards[i], back_of_cards[i], end=' ')
        print(front_of_cards[-1])