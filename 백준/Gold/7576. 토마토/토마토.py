from collections import deque


# M은 열의 개수 N은 행의 개수
# 1은 익은 토마토 0은 익지 않은 토마토 -1은 토마토가 들어있지 않은 칸

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(box, N, M):
    max = 0
    for i in range(N):
        for j in range(M):
            # 0 발생하면 안익은게 있으므로 바로 -1 return
            if box[i][j] == 0:
                return -1
            elif box[i][j] > max:
                max = box[i][j]
    # 최대값이 1이면 익을 필요가 없으므로 0 return
    if max == 1:
        return 0
    else:
        return max-1


def bfs(starts):
    queue = starts
    queue = deque(queue)
    
    while queue:
        (x, y) = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and box[nx][ny] == 0:
                visited[nx][ny] = True
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))


box = []
temp=[]
M, N = map(int, input().split())
for _ in range(N):
    box.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            temp.append([i,j])
bfs(temp)

print(check(box, N, M))