import sys
from heapq import heappush, heappop


def prim(start):
    visited = [False] * (n + 1)
    heap = [(0, start)]
    cost = 0

    while heap:

        min_dist, min_node = heappop(heap)
        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += min_dist

        for next_node, dist in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (dist, next_node))

    return cost


n = int(input())  # 행성의 개수

coordinate = [tuple(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n + 1)]


# 행성 넘버 넣어주기
planet = []
for i in range(n):
    temp_coordinate = list(coordinate[i])
    temp_coordinate.append(i + 1)
    temp_coordinate = tuple(temp_coordinate)
    planet.append(temp_coordinate)
coordinate = planet

information = []

for i in range(3):
    temp = sorted(coordinate, key=lambda x: x[i])
    # for k in range(n):
    #     print(temp[k])
    # print()
    for j in range(n - 1):
        graph[temp[j][3]].append((temp[j + 1][3], abs(temp[j][i] - temp[j + 1][i])))
        graph[temp[j + 1][3]].append((temp[j][3], abs(temp[j][i] - temp[j + 1][i])))


print(prim(1))