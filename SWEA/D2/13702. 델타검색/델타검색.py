T = 10

for test_case in range(1, T+1):

    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    sums = 0

    for i in range(N):
        for j in range(N):

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    sums += abs(board[nx][ny] - board[i][j])
    print(f'#{test_case} {sums}')
