def dfs(v):
    visited[v] = True

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

T = 10
for test_case in range(1, T+1):

    TC, N = map(int, input().split())
    node = list(map(int, input().split()))

    visited = [False] * (100)
    graph = [[] for _ in range(100)]

    # 인접 리스트 만들기 위해 설정
    v1 = node[::2]
    v2 = node[1::2]

    # 인접 리스트 만들기
    for i in range(N):
        graph[v1[i]].append(v2[i])

    dfs(0)

    if visited[99] == True:
        print(f'#{TC} 1')
    else:
        print(f'#{TC} 0')