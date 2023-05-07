M = int(input())
N = int(input())

def Is_Primary(number):

    for i in range(2, number):
        if number % i == 0:
            return False

    else:
        return True

arr = []

for i in range(M, N+1):
    
    if Is_Primary(i):
        arr.append(i)

if 1 in arr:
    idx = arr.index(1)
    del arr[idx]


if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))