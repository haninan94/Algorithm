# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

C, R = map(int, input().split()) # C : 세로   R : 가로
target = int(input())
board = [[0] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

# 시작점설정
x = R-1
y = 0

# 첫 시작점에 1 입력
board[x][y] = 1
visited[x][y] = True

# 넣을 숫자
counts = 1

while counts < R*C:
    for i in range(4):
        direction = i
        if i == 0 or i == 2:
            for _ in range(R-1):
                counts += 1
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    visited[nx][ny] = True
                    board[nx][ny] = counts
                    x = nx
                    y = ny
                else:
                    counts -= 1
                    break
        elif i == 1 or i == 3:
            for _ in range(C-1):
                counts += 1
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    visited[nx][ny] = True
                    board[nx][ny] = counts
                    x = nx
                    y = ny
                else:
                    counts -= 1
                    break


for k in range(R):
    for m in range(C):
        if board[k][m] == target:
            print(m+1, R-k)
if target <= 0 or target > R*C:
    print(0)
