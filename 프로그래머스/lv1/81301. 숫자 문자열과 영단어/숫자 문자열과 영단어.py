def solution(s):
    alphabet_of_number = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    ]
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(10):
        s = s.replace(alphabet_of_number[i], number[i])
    answer = int(s)
    return answer