def dfs(x, y, char):
    char += str(board[x][y])
    if len(char) == 7:
        temp.add(char)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, char)


T = int(input())

# 상 하 좌 우

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]

    temp = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, '')

    print(f'#{test_case} {len(temp)}')