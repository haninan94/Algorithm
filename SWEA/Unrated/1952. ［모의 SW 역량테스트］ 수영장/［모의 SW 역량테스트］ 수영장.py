T = int(input())
for test_case in range(1, T + 1):

    price_list = list(map(int, input().split()))

    month_list = list(map(int, input().split()))

    result_list = [0] * 13

    for i in range(1, 13):
        a = [0, 0, 3000, 3000]

        a[0] = result_list[i - 1] + month_list[i - 1] * price_list[0]

        a[1] = result_list[i - 1] + price_list[1]

        if i >= 3:
            a[2] = result_list[i - 3] + price_list[2]

        if i >= 2:
            a[3] = price_list[3]

        result_list[i] = min(a)

    print(f'#{test_case} {result_list[12]}')