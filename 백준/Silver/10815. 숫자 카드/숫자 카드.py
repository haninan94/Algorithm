

m = int(input())
sangguen_cards = list(map(int, input().split()))
sangguen_cards = set(sangguen_cards)
n = int(input())
my_cards = list(map(int, input().split()))

for idx, card in enumerate(my_cards):
    if card in sangguen_cards:
        my_cards[idx] = 1
    else:
        my_cards[idx] = 0

print(*my_cards)