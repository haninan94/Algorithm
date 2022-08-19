import sys
sys.setrecursionlimit(100000)
def cabbage(x, y):
    global total
    # 방문처리
    visited[x][y] = True
    total += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 1:
            cabbage(nx, ny)


T = int(input())
for test_case in range(1, T+1):
    M, N, K = map(int, input().split())  # N 행    M 열   K 배추 개수
    board = [[0]*M for _ in range(N)]
    result = []


    # 배추밭 만들기
    for i in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    # 방문 처리 리스트
    visited = [[False] * M for _ in range(N)]

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] ==1:
                total = 0
                cabbage(i, j)
                result.append(total)

    print(len(result))