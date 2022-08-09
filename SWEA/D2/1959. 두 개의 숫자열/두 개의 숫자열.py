T = int(input()) # 테스트 케이스 T 입력

for test_case in range(1, T+1):

    a, b = map(int, input().split())  # bi의 길이
    
    N = input().split()
    M = input().split()
    
    if len(N) == len(M):
        sum = 0
        for i in range (0,len(N)):
            sum += (int(N[i]) * int(M[i]))
        print(sum)

    elif len(N) < len(M):
        diff = len(M) - len(N)
        max = 0
        for i in range(diff+1):
            sum = 0
            for j in range(len(N)):
                sum += int(N[j]) * int(M[j+i])
            if sum > max:
                max = sum

    elif len(M) < len(N):
        diff = len(N) - len(M)
        max = 0
        for i in range(diff+1):
            sum = 0
            for j in range(len(M)):
                sum += int(M[j]) * int(N[i+j])
            if sum > max:
                max = sum
    print('#{0} {1}'.format(test_case, max))