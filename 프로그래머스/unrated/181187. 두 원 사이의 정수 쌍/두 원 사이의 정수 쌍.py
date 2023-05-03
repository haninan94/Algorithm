from math import floor, sqrt, ceil

def solution(r1, r2):
    answer = 0
    
    for i in range(1, r2+1):
        max_y = floor(sqrt(r2**2-i**2))
        min_y = 0 if i >= r1 else ceil(sqrt(r1**2 - i**2))
        answer += max_y - min_y + 1
        
    answer *= 4
    return answer