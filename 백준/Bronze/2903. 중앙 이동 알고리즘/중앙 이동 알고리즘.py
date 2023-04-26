n = int(input())

count = 1
i = 2
answer = 0
while count <= n :
    answer = (i + (i-1)) ** 2
    i = i+i-1
    count += 1
print(answer)
