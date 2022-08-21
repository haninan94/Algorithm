T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split()) # N은 방바닥 크기 # M은 파리채 크기

    board = [list(map(int, input().split())) for _ in range(N)]

    sums = 0
    max_of_sums = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(i,i+M):
                for l in range(j, j+M):
                     sums += board[k][l]
            if sums > max_of_sums:
                max_of_sums = sums
            sums = 0

    print(f'#{test_case} {max_of_sums}')

