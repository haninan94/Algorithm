def delta(x, y):
    global move

    move = 1

    visited[x][y] = True
    while True:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 델타 이동 가능한 곳이면 moves +1 해주고 좌표 변경
            if 0 <= nx < N and 0 <= ny < N and room[nx][ny] - room[x][y] == 1:
                move += 1
                x = nx
                y = ny
                break
        else:
            return move


T = int(input())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_position_x = 0
    max_position_y = 0
    max_moves = 1
    temp = []
    for i in range(N):
        for j in range(N):
            delta_value = delta(i, j)
            if delta_value >= max_moves:
                if delta_value > max_moves:
                    max_moves = delta_value
                    max_position_x = i
                    max_position_y = j
                elif delta_value == max_moves:
                    if room[i][j] < room[max_position_x][max_position_y]:
                        max_position_x = i
                        max_position_y = j
                temp.append(delta_value)
            move = 1
    print(f'#{test_case} {room[max_position_x][max_position_y]} {max(temp)}')

