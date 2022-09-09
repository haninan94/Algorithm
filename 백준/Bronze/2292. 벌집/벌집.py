N = int(input())
i = 0
temp = 1
while True:
    temp += 6*i
    i += 1
    if temp >= N:
        break
print(i)