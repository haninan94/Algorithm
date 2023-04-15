import sys
sys.setrecursionlimit(1000000000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = True

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < M and not visited[new_x][new_y] and picture[new_x][new_y] == 1:
            dfs(new_x, new_y)

N, M = map(int, input().split())

picture = []
visited = [[False] * (M) for _ in range(N)]
# print(visited)

for _ in range(N):
    picture.append(list(map(int, input().split())))

answer = []
for i in range(N):
    for j in range(M):
        if picture[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            answer.append(cnt)
if not answer:
    print(0)
    print(0)
else:
    print(len(answer))
    print(max(answer))