N = int(input())
numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
for i in range(len(numbers)):
    print(numbers[i])
