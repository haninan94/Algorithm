N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(input().lstrip()))

select = []

w_first = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
b_first = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
# 우측 상단이 흰색깔인 체스판
white_board = [
    w_first, b_first, w_first, b_first, w_first, b_first, w_first, b_first
]
black_board = [
    b_first, w_first, b_first, w_first, b_first, w_first, b_first, w_first
]

def check(select):
    white_cnt = 0
    for i in range(8):
        for j in range(8):
           if select[i][j] != white_board[i][j]:
               white_cnt += 1
    black_cnt = 0
    for i in range(8):
        for j in range(8):
            if select[i][j] != black_board[i][j]:
                black_cnt += 1
    
    return min(white_cnt, black_cnt)
# print(black_board)
answer = 64
# start 행에서 시작
for i in range(N-8+1):
    for j in range(M-8+1):
        for k in range(8):
            select.append(board[i+k][j:j+8])
        if(check(select)) < answer:
            answer = check(select)
        select = []
print(answer)