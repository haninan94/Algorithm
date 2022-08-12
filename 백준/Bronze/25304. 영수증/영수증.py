total_price = int(input())
N = int(input())
prices = []
for i in range(N):
    price, n = map(int, input().split())
    prices.append(price*n)
if total_price == sum(prices):
    print('Yes')
else :
    print('No')
    