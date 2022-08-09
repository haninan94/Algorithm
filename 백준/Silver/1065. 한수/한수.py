def hansu(N):

    count = 0
    for i in range(1, N + 1):
        number = list(map(int, str(i)))
        if i < 100:
            count += 1
        elif number[0] - number[1] == number[1] - number[2]:
            count += 1
    return count


N = int(input())

print(hansu(N))