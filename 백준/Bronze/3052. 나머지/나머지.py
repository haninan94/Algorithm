numbers = [int(input()) for _ in range(10)]
remains = []
counts = [0] * 1001
unique_counts = 0

for number in numbers:
    remains.append(number%42)

# remains 를 counts 행렬 만든다
for i in range(10):
    counts[remains[i]] += 1

for j in range(1001):
    if counts[j] >= 1:
        unique_counts += 1
        
print(unique_counts)