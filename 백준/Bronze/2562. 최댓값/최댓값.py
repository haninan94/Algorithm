numbers = [int(input()) for _ in range(9)]

max_of_numbers = 0
idx_of_max = 0
for idx, number in enumerate(numbers):
    if number > max_of_numbers:
        max_of_numbers = number
        idx_of_max = idx
print(max_of_numbers)
print(idx_of_max+1)