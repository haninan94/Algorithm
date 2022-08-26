T = int(input())

# 숫자가 단조이면 그대로 반환 아니면 -1 반환
def is_increasing(number):
    number = str(number)
    if len(number) == 1:
        return -1
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            return -1
    return number


for test_case in range(1, T + 1):

    N = int(input())
    numbers = list(map(int, input().split()))
    answer = []
    temp = []
    for i in range(N):
        for j in range(i + 1, N):
            temp.append(numbers[i] * numbers[j])

    for number in temp:
        if int(is_increasing(number)) == number:
            answer.append(number)
    if not answer:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {max(answer)}')