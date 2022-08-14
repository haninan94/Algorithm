N = int(input())
numbers = list(map(int , input().split()))
max_of_numbers = -1000000
min_of_numbers = 1000000
for num in numbers:
    if num > max_of_numbers:
        max_of_numbers = num
    if num < min_of_numbers:
        min_of_numbers = num
print(f'{min_of_numbers} {max_of_numbers}')