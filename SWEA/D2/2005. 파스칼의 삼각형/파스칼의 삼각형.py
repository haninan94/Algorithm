def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def combination(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    print(f'#{test_case}')
    print(1)
    for n in range(1, N):
        for r in range(0, n+1):
            print(int(combination(n, r)), end=' ')
        print()