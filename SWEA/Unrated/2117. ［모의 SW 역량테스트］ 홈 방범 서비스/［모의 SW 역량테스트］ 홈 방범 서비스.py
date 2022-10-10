def bfs(i, j):
    global answer

    distance_map[i][j] = 1
    visited[i][j] = True
    queue = [(i, j, 1)]

    while queue:
        x, y, distance = queue.pop(0)
        distance += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                distance_map[nx][ny] = distance
                queue.append((nx, ny, distance))

    for l in range(N):
        for m in range(N):
            if city[l][m] == 1:
                homes.append(distance_map[l][m])

    max_income = M * len(homes)

    alpha = 1
    while True:
        cost = alpha**2 + (alpha - 1) ** 2
        if cost > max_income:
            return
        filtered = [x for x in homes if x <= alpha]
        temp_income = len(filtered) * M
        if temp_income >= cost:
            answer.append(len(filtered))
        alpha += 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    city = [list(map(int, input().split())) for _ in range(N)]

    answer = []
    homes = []
    for i in range(N):
        for j in range(N):
            distance_map = [[0] * N for _ in range(N)]
            visited = [[False] * N for _ in range(N)]
            bfs(i, j)
            homes = []

    print(f'#{test_case} {max(answer)}')
