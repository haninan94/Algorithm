T = 10

for test_case in range(1, T + 1):

    question_number = int(input())

    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    max = 0

    sum_of_oneline = 0

    for i in range(N):
        for j in range(N):
            sum_of_oneline += arr[i][j]
        if sum_of_oneline > max:
            max = sum_of_oneline
        sum_of_oneline = 0

    for j in range(N):
        for i in range(N):
            sum_of_oneline += arr[i][j]
        if sum_of_oneline > max:
            max = sum_of_oneline
        sum_of_oneline = 0

    for i in range(N):
        sum_of_oneline += arr[i][i]
        if sum_of_oneline > max:
            max = sum_of_oneline
        sum_of_oneline = 0

    for i in range(N):
        sum_of_oneline += arr[i][N - 1 - i]
        if sum_of_oneline > max:
            max = sum_of_oneline

    print(f'#{test_case} {max}')
