board = [list(map(int, input().split())) for _ in range(9)]

max_of_value = 0
idx_of_x = 0
idx_of_y = 0
for i in range(9):
    for j in range(9):
        if board[i][j] > max_of_value:
            max_of_value = board[i][j]
            idx_of_x = i
            idx_of_y = j

print(max_of_value)
print(idx_of_x+1, idx_of_y+1)
            