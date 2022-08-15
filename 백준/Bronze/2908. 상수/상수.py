numbers = input().split()

numbers[0] = numbers[0][::-1]
numbers[1] = numbers[1][::-1]

if numbers[0]>numbers[1]:
    print(numbers[0])
else:
    print(numbers[1])