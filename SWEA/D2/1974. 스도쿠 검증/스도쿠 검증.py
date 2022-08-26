
T = int(input())

# 가운데부터 시계방향 델타
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

# box 중심 좌표
box_x = [1, 1, 1, 4, 4, 4, 7, 7, 7]
box_y = [1, 4, 7, 1, 4, 7, 1, 4, 7]
# 행 검증
def row(board):
    temp = []
    for i in range(9):
        for j in range(9):
            temp.append(board[i][j])
        if len(set(temp)) != 9:
            return 0
        temp = []
    else:
        return 1


# 열 검증
def col(board):
    temp = []
    for j in range(9):
        for i in range(9):
            temp.append(board[i][j])
        if len(set(temp)) != 9:
            return 0
        temp = []
    else:
        return 1


def box(board):
    temp = []
    # box 반복
    for i in range(9):
        x = box_x[i]
        y = box_y[i]
        # box 내에서 델타이동
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            temp.append(board[nx][ny])
        if len(set(temp)) != 9:
            return 0
        temp = []
    else:
        return 1


for test_case in range(1, T + 1):

    board = [list(map(int, input().split())) for _ in range(9)]

    r = row(board)
    c = col(board)
    b = box(board)

    if r + c + b == 3:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
