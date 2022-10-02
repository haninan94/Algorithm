import sys

# find(경로 압축)
def find_set(node):
    if parent[node] != node:
        parent[node] = find_set(parent[node])
    return parent[node]

# N : 도시의 개수, M : 간선의 개수
N, M = map(int, sys.stdin.readline().split())

# 간선 정보 입력받고 가중치를 기준으로 sort
information = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
information.sort(key=lambda x: x[2])


parent = list(range(N + 1))
cost = 0
counts = 0

for x, y, weight in information:
    x_root, y_root = find_set(x), find_set(y)

    if x_root != y_root:
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root
        cost += weight
        counts += 1

        if counts >= N - 2:
            break

print(cost)

