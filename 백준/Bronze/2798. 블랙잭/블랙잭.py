from itertools import combinations


N, M = map(int, input().split())
cards = list(map(int, input().split()))

temp = combinations(cards, 3)

max = 0
for card in temp:
    sums = 0
    for j in range(3):
        sums += card[j]
    if sums > max and  sums <= M:
        max = sums
print(max)