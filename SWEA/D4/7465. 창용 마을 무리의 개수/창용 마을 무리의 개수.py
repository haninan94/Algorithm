
def dfs(v):
    global total
    visited[v] = True
    total += 1

    for next_v in social[v]:
        if not visited[next_v]:
            dfs(next_v)

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    social = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    result = []

    for i in range(M):
        v1, v2 = map(int, input().split())
        social[v1].append(v2)
        social[v2].append(v1)
    for i in range(1, N+1):
        if not visited[i] or len(social[i]) == 0:
            total = 0
            dfs(i)
            result.append(total)

    print(f'#{test_case} {len(result)}')