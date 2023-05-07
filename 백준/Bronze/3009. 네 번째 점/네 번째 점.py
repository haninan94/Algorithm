x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in x:
    if x.count(i) == 1:
        answer_x = i        

for i in y:
    if y.count(i) == 1:
        answer_y = i

print(answer_x)
print(answer_y)
