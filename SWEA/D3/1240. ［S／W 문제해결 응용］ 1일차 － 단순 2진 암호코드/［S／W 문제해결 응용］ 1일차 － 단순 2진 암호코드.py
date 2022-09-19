
T = int(input())

password = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N : 세로 , M : 가로 크기
    code = [input() for _ in range(N)]
    for i in range(N):
        if '1' in code[i]:
            first_line = i
            break
    code = code[first_line]
    code = code.strip('0')
    code = '0' * (7 - (len(code) % 7)) + code
    # print(code)
    # print(len(code))
    answer = []
    for i in range(0, len(code), 7):
        answer.append(code[i : i + 7])
    # print(answer)
    for i in range(len(answer)):
        if answer[i] in password.keys():
            answer[i] = password.get(answer[i])
    # print(answer)
    valid = 0
    # print(answer)
    for i in range(len(answer)):
        if i % 2 == 0:
            valid += answer[i] * 3
        else:
            valid += answer[i]

    # print(valid)
    if valid % 10 == 0:
        print(f'#{test_case} {sum(answer)}')
    else:
        print(f'#{test_case} 0')