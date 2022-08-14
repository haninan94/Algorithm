T = int(input())
for _ in range(T):
    count = 0
    scores = input().split('X')
    for i in range(len(scores)):
        for j in range(len(scores[i])):
            count += j+1
    print(count)