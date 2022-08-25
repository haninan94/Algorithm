def bfs(v):
    queue = [v]
    visited[v] = True
    result = 0

    while queue: # queue 가 비어있을 때 까지
        new_v = queue.pop(0)
        for i in graph[new_v]:
            if not visited[i]: # i가 방문처리 안되어있다면
                visited[i] = True
                queue.append(i)
                result += 1

    return result

N = int(input()) # 컴퓨터의 수
network = int(input()) # 네트워크 연결 수
visited = [False] * (N + 1) # 방문처리
graph = [[] for _ in range(N+1)]

for i in range(network):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(1))