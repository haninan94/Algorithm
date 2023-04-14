from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 방문처리

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 방향에서 4가지로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= (N-1) and 0<= ny <= (M-1) and visited[nx][ny] == 0 and maze[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    


N, M = map(int, input().split())

maze = []
visited = [[0] * (M) for _ in range(N)]

for i in range(N):
    maze.append(list(map(int, input())))

visited[0][0] = 1

bfs(0, 0)

print(visited[N-1][M-1])
    