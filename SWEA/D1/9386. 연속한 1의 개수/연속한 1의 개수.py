
T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    arr = input()

    counts = 0
    max_counts = 0
    for i in range(N):
        if arr[i] == '1':
            counts += 1
            if i == N-1:
                if counts > max_counts:
                    max_counts = counts
        elif arr[i] == '0':
            if counts > max_counts:
                max_counts = counts
            counts = 0
    print(f'#{test_case} {int(max_counts)}')
