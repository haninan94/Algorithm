number = int(input())

answer = 0
for i in range(1, number +1):
    temp = i
    arr = []
    while temp > 0:
        arr.append(temp % 10)
        temp = temp // 10
    if (sum(arr)+i == number):
        answer = i
        break
print(answer)