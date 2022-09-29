import sys

def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


N = int(input())  # 컴퓨터의 수
M = int(input())  # 연결할 수 있는 선의 수
sum_of_cost = 0
counts = 0
edges = []
parent = list(range(N + 1))
for i in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, start, end))

edges.sort()  # 비용 기준으로 sort

for cost, start, end in edges:
    start_root, end_root = find_set(start), find_set(end)

    # 서로소 라면
    if start_root != end_root:
        if start_root < end_root:
            parent[end_root] = start_root
        else:
            parent[start_root] = end_root

        sum_of_cost += cost
        counts += 1

        if counts >= N - 1:
            break
print(sum_of_cost)
