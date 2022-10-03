def test(x, y, color):
    move = 1
    for i in range(8):
        move = 1
        nx = x + dx[i]
        ny = y + dy[i]

        # 이동하고나서 새로 이동한 곳이 board위에 있고 이동한곳의 돌이 놓은돌과 다른 색깔일때 반복
        while (
            0 <= nx < N
            and 0 <= ny < N
            and board[nx][ny] != board[x][y]
            and board[nx][ny] != 0
        ):
            # move + 1 해주고 move의 거리만큼 계속 이동
            move += 1
            nx = x + dx[i] * move
            ny = y + dy[i] * move
        # 같은 색깔의 돌을 만나면 위 while문이 멈추고 다른돌을 발견하면 변경 / 0 만나면 알아서 다음 방향으로 진행
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == board[x][y]:
            for j in range(1, move):
                board[x + dx[i] * j][y + dy[i] * j] = color


# 델타 12 시부터 시계방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * (N) for _ in range(N)]

    # 시작할때 board 초기화
    for i in range(N // 2, N // 2 + 2):
        for j in range(N // 2, N // 2 + 2):

            if i == j:
                board[i - 1][j - 1] = 2
            else:
                board[i - 1][j - 1] = 1

    # 돌 놓는 정보 입력받기
    for i in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        board[x][y] = color
        test(x, y, color)

    black = 0
    white = 0
    for i in range(N):
        black += board[i].count(1)
        white += board[i].count(2)

    print(f'#{test_case} {black} {white}')