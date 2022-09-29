def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


N = int(input())  # 도시의 개수
M = int(input())  # 여행 계획에 속한 도시들의 수 M

parent = list(range(N + 1))

for i in range(N):
    arr = input().split()
    for j in range(len(arr)):
        if arr[j] == '1':
            start_root, end_root = find_set(i + 1), find_set(j + 1)

            if start_root != end_root:
                if start_root < end_root:
                    parent[end_root] = start_root
                else:
                    parent[start_root] = end_root

answer = list(map(int, input().split()))

temp = 'YES'

root = find_set(answer[0])
for i in range(1, M):
    if find_set(answer[i]) != root:
        temp = 'NO'
        break
print(f'{temp}')