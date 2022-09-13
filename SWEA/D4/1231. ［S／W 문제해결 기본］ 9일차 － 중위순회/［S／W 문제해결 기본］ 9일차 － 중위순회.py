T = 10

def inorder(n):
    global answer
    if n:
        inorder(ch1[n])
        answer += heap[n]
        inorder(ch2[n])

for test_case in range(1, T + 1):
    V = int(input())
    answer = ''
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    heap = [0] * (V + 1)
    for i in range(V):
        information = list(input().split())
        heap[int(information[0])] = information[1]  # 정점 번호에 알파벳 넣기
        if len(information) == 4:  # 좌 우 자식 다 있다면
            ch1[int(information[0])] = int(information[2])
            ch2[int(information[0])] = int(information[3])
        elif len(information) == 3:  # 좌 자식만 있다면
            ch1[int(information[0])] = int(information[2])
        elif len(information) == 2:  # 자식이 없다면
            pass
    inorder(1)
    print(f'#{test_case} {answer}')