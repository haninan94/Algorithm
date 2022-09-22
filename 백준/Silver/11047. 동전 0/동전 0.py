N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
answer = 0
for i in range(len(coins) - 1, -1, -1):
    # 코인의 개수인 answer에 현재 금액을 큰단위의 코인으로 나눈 몫을 덧셈 하고 금액에 나머지금액 저장
    answer += K // coins[i]
    K %= coins[i]

print(answer)