T = int(input())

for test_case in range(1, T+1):

    A, B = input().split()

    A = A.replace(B,'.')
    print(f'#{test_case} {len(A)}')