
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    counts = 0
    max_counts = 0

    for i in range(N - 1):
        if carrots[i] - carrots[i + 1] == -1:
            counts += 1
            if i == N - 2:
                counts += 1
                counts > max_counts
                max_counts = counts
        else:
            if carrots[i-1] - carrots[i] == -1:
                counts += 1
            if counts > max_counts:
                max_counts = counts
            counts = 0
    if max_counts == 0:
        max_counts += 1
    print(f'#{test_case} {max_counts}')