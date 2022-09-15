T = 10

def preorder(N):
    global answer
    N = int(N)
    if N:
        preorder(ch1[N])
        preorder(ch2[N])
        answer.append(tree[N])


for test_case in range(1, T + 1):
    # N : 정점의 개수
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    tree = [0] * (N + 1)
    answer = []
    for i in range(N):
        info = list(input().split())
        # 정점이 연산자라면
        if not info[1].isdigit():
            ch1[int(info[0])] = info[2]
            ch2[int(info[0])] = info[3]
            tree[int(info[0])] = info[1]
        else:
            tree[int(info[0])] = info[1]
    preorder(1)
    stack = []
    for char in answer:
        if char.isdecimal():
            stack.append(char)
        else:
            y = int(stack.pop())
            x = int(stack.pop())
            if char == '*':
                stack.append(x * y)
            elif char == '/':
                stack.append(x // y)
            elif char == '+':
                stack.append(x + y)
            elif char == '-':
                stack.append(x - y)
    print(f'#{test_case}', *stack)