T = 10

for _ in range(1, T+1):

    test_case = int(input())

    def palindrome(word, M): # 회문 반환 함수
        for i in range(len(word) - (M - 1)): # word의 길이 만큼에서 길이 M인 글자만큼만 돌게 반복
            a = word[i : i + M] # 길이 M인 글자 a에 저장
            b = a[::-1] # a를 거꾸로 뒤집는다.
            if a == b: # 뒤집은게 서로 같으면
                return(len(a)) # 회문의 길이 반환

    words = [list(input()) for _ in range(100)]
    lens = 0
    max_of_lens = 0

    for M in range(100, 0, -1):
        for i in range(100):
            if palindrome(words[i], M) != None:
                lens = palindrome(words[i], M)
        if lens > max_of_lens:
            max_of_lens = lens
        lens = 0

    words_T = [[0] * 100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            words_T[j][i] = words[i][j]

    for M in range(100, 0, -1):
        for i in range(100):
            if palindrome(words_T[i], M) != None:
                lens = palindrome(words_T[i], M)
        if lens > max_of_lens:
            max_of_lens = lens
        lens = 0

    print(f'#{test_case} {max_of_lens}')

