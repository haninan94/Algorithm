
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


T = int(input())

for test_case in range(1, T + 1):

    N = int(input())  # 섬의 개수

    x_positions = list(map(int, input().split()))

    y_positions = list(map(int, input().split()))

    E = float(input())

    parent = list(range(N + 1))

    edges = []

    for i in range(N):
        for j in range(i + 1, N):
            edges.append(((((x_positions[i] - x_positions[j]) ** 2)+ ((y_positions[i] - y_positions[j]) ** 2))**0.5,
                    i + 1,
                    j + 1,
                )
            )

    edges.sort()
    counts = 0
    cost = 0

    for dist, x, y in edges:
        x_root, y_root = find_set(x), find_set(y)

        if x_root != y_root:
            if x_root < y_root:
                parent[y_root] = x_root
            else:
                parent[x_root] = y_root
            cost += dist**2
            counts += 1

            if counts >= N - 1:
                break

    total_cost = E * cost
    print(f'#{test_case} {round(total_cost)}')
