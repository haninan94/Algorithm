make_num = set()
ran = set(range(1, 10001))


for i in range(1, 10001):
    for num in str(i):
        i += int(num)
    make_num.add(i)

self_number = sorted(ran - make_num)
for i in self_number:
    print(i)
