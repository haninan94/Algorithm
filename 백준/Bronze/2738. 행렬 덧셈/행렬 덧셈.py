N, M = map(int, input().split())

# N은 row M은 col

matrix1 = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    numbers = list(map(int, input().split()))
    for j in range(M):
        matrix1[i][j] += numbers[j]
for i in range(N):
    numbers = list(map(int, input().split()))
    for j in range(M):
        matrix1[i][j] += numbers[j]

for i in range(N):
    print(*matrix1[i])
