n = int(input())

sums = 0
i = 0

while sums < n :
    sums += i
    i += 1
line = i - 1
# print(f'sums는 {sums}')
# print('@@@@@@@@@@@@@@@@@@')
# print(f'sums-n은 {sums-n}')
# print(f'{line}번째 줄에 존재합니다.')

if line%2 == 0 :
    first = line
    second = 1
    for j in range(sums-n):
        first -= 1
        second += 1
else:
    first = 1
    second = line
    for j in range(sums-n):
        first += 1
        second -= 1

print(f'{first}/{second}')
    
# 홀수 line은 우상향
# 짝수 Line은 좌하향