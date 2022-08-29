T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 버스 노선의 수

    stop = [0] * 1001

    for _ in range(N):
        bus, A, B = map(int, input().split())

        stop[A] += 1
        stop[B] += 1

        if bus == 1:
            for i in range(A + 1, B):
                stop[i] += 1
        elif bus == 2:
            if A % 2 == 0:
                for i in range(A + 1, B):
                    if i % 2 == 0:
                        stop[i] += 1
            else:
                for i in range(A + 1, B):
                    if i % 2 != 0:
                        stop[i] += 1
        elif bus == 3:
            if A % 2 == 0:
                for k in range(A + 1, B):
                    if k % 4 == 0:
                        stop[k] += 1
            else:
                for z in range(A+1, B):
                    if z % 3 == 0 and z % 10 != 0:
                        stop[z] += 1

    print(f'#{test_case} {max(stop)}')