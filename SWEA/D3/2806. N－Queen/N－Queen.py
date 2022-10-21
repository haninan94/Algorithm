

T = int(input())


def dfs(row):
    global answer
    check = True

    #  열 이동하면서
    for col in range(n):
        if row == n:
            answer += 1
            break
        queen[row] = col
        check = True
        # 행 체크할껀데
        for i in range(row):
            # 0행부터 col의 인덱스까지 행을 체크한다.
            #  같은 열에 있다면
            if queen[i] == queen[row]:
                check = False
                break
            #  대각선에 있다면
            if abs(queen[i] - queen[row]) == abs(i - row):
                check = False
                break
        if check:
            dfs(row + 1)
    return answer


for test_case in range(1, T + 1):

    n = int(input())

    answer = 0

    for i in range(n):
        # 첫번재 행은 반복으로 지정 2행부터 dfs진행
        queen = [9999] * n
        queen[0] = i
        dfs(1)

    print(f'#{test_case} {answer}')
