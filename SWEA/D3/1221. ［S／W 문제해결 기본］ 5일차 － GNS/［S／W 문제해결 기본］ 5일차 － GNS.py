T = int(input())

for test_case in range(1, T + 1):

    test_case_num, N = input().split()
    N = int(N)
    string = input()
    num_dict = {"ZRO":"0", "ONE":"1", "TWO":"2", "THR":"3", "FOR":"4", "FIV":"5", "SIX":"6", 'SVN':"7", "EGT":"8", "NIN":"9"}

    for key, value in num_dict.items():
        string = string.replace(key, value)

    string = string.split()
    string.sort()
    string = ' '.join(s for s in string)

    for key, value in num_dict.items():
        string = string.replace(value, key)
    print(f'#{test_case}', string)
