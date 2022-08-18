computer = int(input())
networks = int(input())
visited = [False] * (computer+1)
graph = [[] for _ in range(computer+1)]

for i in range(networks):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(n):
    visited[n] = True # 방문처리

    for new_visit in graph[n]:
        if visited[new_visit] == False:
            dfs(new_visit)
dfs(1)
sum = 0
for i in range(len(visited)):
    if visited[i] == True:
        sum += 1
print(sum-1)