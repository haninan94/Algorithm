def bfs(v):
    visited[v] = True
    queue = [(v, 1)]
    # print(v, end=' ')
    # 큐가 빌 때까지 반복
    while queue:
        v, depth = queue.pop(0)
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                depth_map[next_v] = depth
                queue.append((next_v, depth + 1))
                # print(next_v, end=' ')
        # depth += 1
    return depth - 1


T = 10

for test_case in range(1, T + 1):
    length, start = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    visited = [False] * (101)
    depth_map = [0 for _ in range(101)]
    for i in range(0, len(edges), 2):
        v1, v2 = edges[i], edges[i + 1]
        graph[v1].append(v2)
    step = bfs(start)
    max_idx = 0
    for i in range(len(depth_map)):
        if depth_map[i] == step:
            if i >= max_idx:
                max_idx = i
    print(f'#{test_case} {max_idx}')
