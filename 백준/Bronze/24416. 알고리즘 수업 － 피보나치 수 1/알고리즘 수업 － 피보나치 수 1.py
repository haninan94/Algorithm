def fib(n):
    global counts
    if n == 1 or n == 2:
        counts += 1
        return 1  # 코드1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    memory = [0] * 50
    memory[1], memory[2] = 1, 1
    counts2 = 0
    for i in range(3, n+1):
        memory[n] = memory[n - 2] + memory[n - 1]
        counts2 += 1
    return counts2


memory = [0] * 50
counts = 0
counts2 = 0
# fib(5)
# print((counts+1) // 2)
n = int(input())
fib(n)
print(counts, fibonacci(n))