T = int(input())

for test_case in range(1, T+1):

    N, M = list(map(int, input().split())) # N:행, M:열
    picture = [list(map(int, input().split())) for _ in range(N)]

    counts = 0
    max_counts = 0

    # 행 우선 순회
    for i in range(N): # 행 반복
        counts = 0
        for j in range(M): # 열 반복
            if picture[i][j] == 1:
                counts += 1
                if j == M-1 :
                    if counts > max_counts and counts >=2:
                        max_counts = counts
                    counts = 0
            else:
                if counts > max_counts and counts >=2:
                    max_counts = counts
                counts = 0

    # 열 우선순회
    for j in range(M): # 열 반복
        counts = 0
        for i in range(N): # 행 반복
            if picture[i][j] == 1:
                counts += 1
                if i == N-1 :
                    if counts > max_counts:
                        max_counts = counts
                    counts = 0
            else:
                if counts > max_counts:
                    max_counts = counts
                counts = 0
    print(f'#{test_case} {max_counts}')

