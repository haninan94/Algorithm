while True:
    a, b, c = map(int, input().split())

    arr = []
    arr.append(a)
    arr.append(b)
    arr.append(c)

    arr = sorted(arr)
    if a == 0 and b == 0 and c == 0:
        break

    if (arr[2] >= arr[0] + arr[1]):
        print('Invalid')

    elif a == b == c:
        print('Equilateral')

    elif (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
        print('Isosceles')


    elif (a != b and a != c and b != c):
        print('Scalene')

    else:
        print('Invalid')