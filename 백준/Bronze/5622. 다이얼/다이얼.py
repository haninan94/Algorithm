number = input()
n = len(number)
time = 0

for i in range(n):
    if 65 <= ord(number[i]) <= 67:
        time += 2
    elif 68 <= ord(number[i]) <= 70:
        time += 3
    elif 71 <= ord(number[i]) <= 73:
        time += 4
    elif 74 <= ord(number[i]) <= 76:
        time += 5
    elif 77 <= ord(number[i]) <= 79:
        time += 6
    elif 80 <= ord(number[i]) <= 83:
        time += 7
    elif 84 <= ord(number[i]) <= 86:
        time += 8
    elif 87 <= ord(number[i]) <= 90:
        time += 9

print(time + n)