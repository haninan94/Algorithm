dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def dfs(x, y, path, direction):
    global counts, i, j

    # 방향은 0에서 시작하므로 무조건 사각형 만들어질려면 방향 3으로 끝나야함
    # 그리고 사각형 만들어 져야 하므로 최소한 경로가 4개 이상이어야함
    if direction == 3 and x == i and y == j and len(path) >= 4:
        counts = max(counts, len(path))
        return 
        

    # 이동한 곳이 경로 리스트에없 유효한 좌표라면
    if 0 <= x < N and 0 <= y < N and cafe[x][y] not in path:
        # 새로운 경로에 해당 경로 추가
        new_path = path + [cafe[x][y]]

        nx = x + dx[direction]
        ny = y + dy[direction]
        dfs(nx, ny, new_path, direction)

        if direction < 3:
            nx = x + dx[direction+1]
            ny = y + dy[direction+1]
            dfs(nx, ny, new_path, direction+1)
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    cafe = [list(map(int, input().split())) for _ in range(N)]

    counts = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, [], 0)

    print(f'#{test_case} {counts}')