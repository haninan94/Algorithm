arr = []
matrix = []

# temp_arr = input()
# for i in range(len(temp_arr)):
#     arr.append(temp_arr[i])

while True:
    try:
        temp_arr = input()
        for i in range(len(temp_arr)):
            arr.append(temp_arr[i])
        matrix.append(arr)
        arr = []
    except:
        break

max = 0
for i in range(len(matrix)):
    if len(matrix[i]) > max:
        max = len(matrix[i])

# print(max)

for i in range(len(matrix)):
    if len(matrix[i]) < max:
        count = max - len(matrix[i])
        for j in range(count):
            matrix[i].append('*')

for j in range(max):
    for i in range(len(matrix)):
        if matrix[i][j] != '*':
            print(matrix[i][j], end="")