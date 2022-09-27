def backtrack(row, n, now_sum, visited):

    global max_of_percentages

    if now_sum <= max_of_percentages:
        return

    if not (False in visited):
        if now_sum > max_of_percentages:
            max_of_percentages = now_sum

    for col in range(N):
        if not visited[col]:
            visited[col] = True
            backtrack(row + 1, n, now_sum * percentages[row][col], visited)
            visited[col] = False


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    percentages = [
        list(map(lambda x: float(x) / 100, input().split())) for _ in range(N)
    ]
    visited = [False] * N
    max_of_percentages = 0
    backtrack(0, N, 1, visited)

    answer = round(max_of_percentages * 100, 6)
    print(f'#{test_case} {answer:.6f}')
