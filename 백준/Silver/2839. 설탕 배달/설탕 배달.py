a = 5
b = 3

sugar = int(input())

answer_list = []

# sugar = 18일때 for i in range(3)
for i in range(sugar//a, -1, -1):
    for j in range(sugar//b, -1, -1):
        if a*i + b*j == sugar:
            answer_list.append(i+j)

if answer_list:
    print(min(answer_list))
else:
    print(-1)