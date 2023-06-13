import math
T = int(input())

for _ in range(T):
    start, end = map(int, input().split())
    distance = end-start

    temp = math.sqrt(distance)
    
    # 거리가 제곱수라면
    if(temp == int(temp)):
        print(2*(int(temp)) -1)

    elif(distance <= int(temp) * int(temp) + int(temp)):
        print(2*int(temp))
    
    else:
        print(2*int(temp) + 1)