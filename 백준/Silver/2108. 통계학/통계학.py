from collections import Counter
import sys

N = int(sys.stdin.readline())

numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
mean = round(sum(numbers) / N)

median = numbers[N // 2]

range_of_numbers = abs(max(numbers) - min(numbers))

# 최빈값

temp = Counter(numbers).most_common(2)

# 최빈값이 1개가 아닐경우(여러개일 경우)
if len(temp) != 1:
    # 개수가 같은 최빈값이 있다면
    if temp[0][1] == temp[1][1]:
        mode = temp[1][0]
    else:
        mode = temp[0][0]
elif len(temp) == 1:
    mode = temp[0][0]

print(mean)
print(median)
print(mode)
print(range_of_numbers)