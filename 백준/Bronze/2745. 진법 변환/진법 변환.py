arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sums = 0
count = 0

N, B = input().split(' ')

for i in range(len(N), 0, -1):
    sums += arr.index(N[i-1]) * (int(B)** count)
    count += 1

if sums >= 1000000000:
    print(1000000000)
else:
    print(sums)