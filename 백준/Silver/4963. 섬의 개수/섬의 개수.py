import sys
sys.setrecursionlimit(10000)
# 상 하 좌 우 10시 1시 5시 7시
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y):
    global total
    # 방문처리
    visited[x][y] = True
    total += 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and island[nx][ny] == 1:
            dfs(nx, ny)

while True:

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    island = []
    visited = [[False] * w for _ in range(h)]
    result = []

    # 지도 만들기
    for i in range(h):
        temp = list(map(int, input().split()))
        island.append(temp)

    for j in range(h):
        for i in range(w):
            if not visited[j][i] and island[j][i] == 1:
                total = 0
                dfs(j, i)
                result.append(total)

    print(len(result))