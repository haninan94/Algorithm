
password = {
    '211': '0',
    '221': '1',
    '122': '2',
    '411': '3',
    '132': '4',
    '231': '5',
    '114': '6',
    '312': '7',
    '213': '8',
    '112': '9',
}


def ratio(code):
    ceta = []
    ans = []
    alpha = []
    beta = []
    str_beta = ''
    code = code.lstrip('0')
    code = code.replace('10', '1,0')
    code = code.replace('01', '0,1')
    temp = code.split(sep=',')
    for i in range(len(temp)):
        ans.append(int(len(temp[i])))
    for i in range(0, len(ans), 4):
        alpha.append(ans[i])
        alpha.append(ans[i + 1])
        alpha.append(ans[i + 2])
        minimum = min(alpha)
        check = 0
        for m in range(3):
            if alpha[m] % minimum == 0:
                check += 1
        if check == 3:
            for j in range(3):
                alpha[j] = alpha[j] // minimum
        for k in range(3):
            str_beta += str(alpha[k])
        beta.append(str_beta)
        if len(beta) == 8:
            ceta.append(beta)
            beta = []
        str_beta = ''
        check = 0
        alpha = []
    return ceta


T = int(input())


for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = sorted(list(set([input().strip() for _ in range(n)])))
    arr.pop(0)
    answer = []
    alpha = []
    for i in range(len(arr)):
        arr[i] = format((int(arr[i], 16)), 'b')
        arr[i] = arr[i].lstrip('0')
    # print(arr)
    for i in range(len(arr)):
        answer.append(ratio(arr[i]))

    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for k in range(len(answer[i][j])):
                if answer[i][j][k] in password.keys():
                    answer[i][j][k] = answer[i][j][k].replace(
                        answer[i][j][k], password.get(answer[i][j][k])
                    )
    # for i in range(len(answer)):
    #     print(answer[i])
    # print(answer[0][0])

    overlaps = []
    final = 0
    val = 0
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for k in range(len(answer[i][j])):
                if k % 2 == 0:
                    val += int(answer[i][j][k]) * 3
                elif k % 2 != 0:
                    val += int(answer[i][j][k])
            # 코드 유효하다면
            if val % 10 == 0:
                overlap = ''
                for l in range(len(answer[i][j])):
                    overlap += answer[i][j][l]
                if not (overlap in overlaps):
                    overlaps.append(overlap)
                    for l in range(len(answer[i][j])):
                        final += int(answer[i][j][l])
                else:
                    continue

            val = 0

    print(f'#{test_case} {final}')
