T = int(input())

for test_case in range(1, T + 1):
    # N : 점원의 수, B : 탑의 높이
    N, B = map(int, input().split())

    # 점원들 키 정보
    info = list(map(int, input().split()))

    # S : 점원들 키의 합
    S = sum(info)

    min_height = S

    result = []
    for i in range(1 << len(info)):
        subset = []
        for j in range(len(info)):
            if i & (1 << j):
                subset.append(info[j])
        if sum(subset) >= B:
            if sum(subset) < min_height:
                min_height = sum(subset)
        # result.append(subset)
    # print(min_height)
    answer = min_height - B
    print(f'#{test_case} {answer}')