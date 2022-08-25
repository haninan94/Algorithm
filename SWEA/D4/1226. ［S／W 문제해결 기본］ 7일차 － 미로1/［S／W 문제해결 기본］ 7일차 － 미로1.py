# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True

    while queue:
        out = 0
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and (maze[nx][ny] == 0 or maze[nx][ny] == 3):
                visited[nx][ny] = True
                queue.append((nx, ny))

    if not visited[target_i][target_j]:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')

T = 10

for test_case in range(1, T+1):
    N = 16
    T = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    # print(maze)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i = i
                start_j = j
                break

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                target_i = i
                target_j = j
                break
    bfs(start_i, start_j)
