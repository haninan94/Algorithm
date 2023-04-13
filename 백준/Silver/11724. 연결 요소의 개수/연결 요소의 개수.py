def dfs(v):
    # 방문처리 하고
    visited[v] = True
    global temp
    temp.append(v)

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)
    
    
answer = []

# 정점의 개수 N, 간선의 개수 M
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N+1):
    temp = []
    if not visited[i]:
        dfs(i)
    if temp:
        answer.append(temp)
    temp = []

print(len(answer))
    
    