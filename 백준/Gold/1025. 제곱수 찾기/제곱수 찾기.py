def is_square_number(number):
    i = 0
    while True:
        # 제곱수라면 해당 숫자 그대로 반환
        if i**2 == number:
            return True
        
        # 제곱수 못찾고 넘어가버리면 제곱수 아니므로 False
        if i**2 > number:
            return False

        i += 1

N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(input())

answer = -1

for i in range(N):
    for j in range(M):
        for degree_difference_row in range(-N, N):
            for degree_difference_col in range(-M, M):
                number = ""
                row = i
                col = j
                if degree_difference_row == 0 and degree_difference_col == 0:
                    continue
                # 등차 더한 행이나 열이 table좌표 내에 있어야 함
                while 0 <= row < N and 0 <= col < M:
                    # 처음은 i, j 좌표값을 넣어주고 이후 부터는 등차 적용된 좌표값 더해줌
                    number += table[row][col]

                    # 더해주면 그게 제곱수인지 검사한다.
                    if is_square_number(int(number)):
                        answer = max(answer, int(number))

                    row += degree_difference_row
                    col += degree_difference_col

print(answer)