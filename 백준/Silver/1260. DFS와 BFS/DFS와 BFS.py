def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for next in graph[start]:
        if not visited[next]:
            dfs(next)
queue = []

def bfs(start):
    visited[start] = True
    queue = [start]
    print(start, end=" ")

    while queue:
        v = queue.pop(0)
        for next in graph[v]:
            if not visited[next]:
                visited[next] = True
                print(next, end=" ")
                queue.append(next)
    

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
# print(visited)

# 그래프 만들기
for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(len(graph)):
    if graph[i]:
        graph[i] = sorted(graph[i])
    
dfs(V)
print()

visited = [False] * (N+1)

bfs(V)