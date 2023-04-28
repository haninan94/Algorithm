import copy

def dfs(arr):
    if len(arr) == M:
        answer.append(copy.deepcopy(arr))
        return

    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            arr.append(numbers[i])

            dfs(arr)

            visited[i] = False
            arr.pop()

N, M = map(int, input().split())

numbers = list(range(1, N+1))
visited = [False] * (N)
answer = []

dfs([])

for i in range(len(answer)):
    print(*answer[i])