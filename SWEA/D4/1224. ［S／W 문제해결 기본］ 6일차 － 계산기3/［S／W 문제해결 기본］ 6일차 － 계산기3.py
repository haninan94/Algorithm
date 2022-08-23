T = 10

for test_case in range(1, T + 1):

    N = int(input())
    word = input()

    stack = []
    answer = ''

    for char in word:
        if char.isdecimal():
            answer += char

        # 괄호 곱/나눗셈 합/차 순서
        else:
            if char == '(':
                stack.append(char)

            elif char == ')':
                while stack and stack[-1] != '(':
                    answer += stack.pop()
                stack.pop()

            elif char == '*' or char == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    answer += stack.pop()
                stack.append(char)

            elif char == '+' or char == '-':
                while stack and stack[-1] != '(':
                    answer += stack.pop()
                stack.append(char)

    while stack:
        answer += stack.pop()

    for char in answer:

        if char.isdecimal():
            stack.append(char)

        # 순서 주의 앞에나온 숫자가 아래로 들어갔으니까 뒤로 보내야함
        else:
            x = float(stack.pop())
            y = float(stack.pop())
            if char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)
            elif char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)

    print(f'#{test_case} {int(stack.pop())}')
