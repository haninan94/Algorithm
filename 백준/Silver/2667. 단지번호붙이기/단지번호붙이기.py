house = 0

def dfs(x, y):
    global house
    visited[x][y] = True
    house += 1

    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]

        if  0 <= new_x < N and 0 <= new_y < N and graph[new_x][new_y] == '1' and not visited[new_x][new_y]:
            dfs(new_x, new_y)


N = int(input())

graph = []

for i in range(N):
    graph.append(list(input()))


visited = [([False] * (N)) for _ in range(N)]
# print(visited)

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []

for x in range(N):
    for y in range(N):
        if graph[x][y] == '1' and not visited[x][y]:
            dfs(x, y)
            answer.append(house)
            house = 0

print(len(answer), *sorted(answer), sep="\n")