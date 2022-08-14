N = int(input())
scores = list(map(int, input().split()))
max_of_scores = 0
for score in scores:
    if score > max_of_scores:
        max_of_scores = score

for i in range(N):
    scores[i] = scores[i] / max_of_scores * 100
print(sum(scores)/N)