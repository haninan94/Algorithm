arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(int, input().split())
answer = ''

while N >= B:
    temp = arr[N%B]
    answer = answer + temp
    N = N // B

answer = answer + arr[N]

print(answer[::-1])