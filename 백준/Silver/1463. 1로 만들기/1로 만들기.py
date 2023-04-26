target = int(input())

# 횟수 들어가는 배열
D = [0] * (target+1)

D[1] = 0
for i in range(2, target + 1):
    D[i] = D[i-1] + 1

    # 다음 i 가 3으로 나누어 떨어지면 3으로 나누어 떨어진 수에서 cnt + 1
    if i % 3 == 0:
        D[i] = min(D[i], D[i //3] + 1)

    # 다음 i 가 2으로 나누어 떨어지면 2으로 나누어 떨어진 수에서 cnt + 1
    if i % 2 == 0:
        D[i] = min(D[i], D[i //2] + 1)

print(D[target])
    