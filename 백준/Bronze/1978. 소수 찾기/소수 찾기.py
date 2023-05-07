T = int(input())

arr = list(map(int, input().split()))

def Is_Primary(number):

    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True

count = 0

for number in arr:

    if number == 1:
        continue
    if Is_Primary(number):
        count += 1

print(count)