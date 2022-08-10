
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())

    arr = [[0] * N for _ in range(N)]  # 원소가 모두 0인 N * N 2차원 배열
    num = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 우 하 좌 상

    r = 0  # 시작점의 row 번호
    c = 0  # 시작점의 column 번호
    run_num = N - 1  # 처음 이동할 횟수 (이후에 변경됨)
    arr[r][c] = 1  # 첫 시작점 1

    while True:  # 무한루프

        for i in range(4):  # i가 1부터 3까지 반복
            for _ in range(run_num):  # run만큼 반복 해당 반복문 변수 사용하지 않으므로 _ 무관
                r += dx[i]  # i가 x일경우 dx와 dy의 인덱스 x값을 넣어줌으로써 접근하는 인덱스를 변경
                c += dy[i]
                if arr[r][c] != 0:  # 넣어주려는 자리가 0이아니고 다른 숫자가 들어가있으면 반복문 탈출
                    break
                num += 1  # 넣을 숫자 1증가
                arr[r][c] = num  # 증가된 num값을 해당 자리에 저장

        if num == N**2:  # 채워준 넘버가 N**2 즉, 모두 다 채웠다면 무한루프 탈출
            break
        r += 1  # 한바퀴 돌고나면 시작점을 변경해줌
        c += 1
        num += 1
        arr[r][c] = num  # 변경된 시작점에 num값을 저장
        run_num -= 2  # 외곽이 채워졌으니 상하좌우 이동해야할 값을 변경해줌

    print(f'#{test_case}')
    for i in range(N):  # 배열 속의 배열을 반복문으로 접근
        print(*arr[i])  # 언패킹해서 값만 나열