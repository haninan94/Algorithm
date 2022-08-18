T = 10

for test_case in range(1, T+1):

    n, s = input().split()

    stack = []

    for i in range(int(n)):
        if not stack: # 스택이 비어있다면
            stack.append(s[i])
        else: # 스택이 비어있지 않다면
            if stack[-1] == s[i]: # 넣으려는 item이 stack의 top item과 같다면
                stack.pop()
            else:
                stack.append(s[i])

    stack = ''.join(stack)
    print(f'#{test_case} {stack}')