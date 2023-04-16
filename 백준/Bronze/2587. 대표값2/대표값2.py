arr = []

for _ in range(5):
    arr.append(int(input()))

arr = sorted(arr)

print(int(sum(arr)/len(arr)))
print(arr[len(arr)//2])