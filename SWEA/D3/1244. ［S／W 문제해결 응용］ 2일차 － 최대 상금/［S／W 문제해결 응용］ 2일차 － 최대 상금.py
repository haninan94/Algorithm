def dfs(N):
    global reward
    if N == 0:
        temp = int(''.join(numbers))

        if temp > reward:
            reward = temp
        return

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            if not ((''.join(numbers), N) in alpha):
                alpha.add((''.join(numbers), N))
                dfs(N - 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())

for test_case in range(1, T + 1):
    numbers, N = list(input().split())
    numbers = list(numbers)
    N = int(N)
    alpha = set()
    reward = 0
    dfs(N)

    print(f'#{test_case} {reward}')
