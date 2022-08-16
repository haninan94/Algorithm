T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    prices = list(map(int, input().split()))
    income = 0
    while True:
        max_of_price = 0
        max_of_idx = 0
        sum_of_price = 0
        for idx, value in enumerate(prices):
            if value > max_of_price:
                max_of_price = value
                max_of_idx = idx
        for i in range(0, max_of_idx):
            sum_of_price += prices[i]
        income += (max_of_price*max_of_idx) - (sum_of_price)
        if prices[-1] == max_of_price:
            break
        prices = prices[max_of_idx+1:]

    print(f'#{test_case} {income}')
