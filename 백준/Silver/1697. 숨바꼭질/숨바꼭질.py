from collections import deque

def bfs(start):
    cnt = 0
    visited[start]=True
    queue = (start, cnt)
    queue = deque([queue])

    while queue:
        v = queue.popleft()
        if v[0] == K:
            print(v[1])
            break
        for i in range(3):
            if i == 0:
                next_v = v[0] + 1
                if 0 <= next_v <= 100002 and not visited[next_v]:
                    queue.append((next_v, v[1] + 1))
                    visited[next_v] = True

            elif i == 1:
                next_v = v[0] -1
                if 0 <= next_v <= 100002 and not visited[next_v]:
                    queue.append((next_v, v[1] +1))
                    visited[next_v] = True

            elif i == 2:
                next_v = v[0] * 2
                if 0 <= next_v <= 100002 and not visited[next_v]:
                    queue.append((next_v, v[1] + 1))
                    visited[next_v] = True

            
N, K = map(int, input().split())

visited = [False] * (200004)

bfs(N)