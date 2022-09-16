import math
import decimal


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    answer = N ** decimal.Decimal(
        '0.33333333333333333333333333333333333333333333333333333333333333333333333333333333'
    )
    answer = float(answer)
    if answer.is_integer():
        print(f'#{test_case} {int(answer)}')
    else:
        print(f'#{test_case} -1')
