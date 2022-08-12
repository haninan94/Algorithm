word = input()  # ljes=njak

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

counts = 0

while len(word) > 0:
    if word[:3] in croatia:
        counts += 1
        word = word[3:]
    elif word[:2] in croatia:
        counts += 1
        word = word[2:]
    elif word[:1] not in croatia:
        counts += 1
        word = word[1:]
print(counts)