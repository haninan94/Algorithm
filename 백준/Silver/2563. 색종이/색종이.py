board = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            board[i][j] = 1
sums = 0
for i in range(len(board)):
    sums += sum(board[i])
print(sums)