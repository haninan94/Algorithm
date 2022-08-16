T = int(input())

for test_case in range(1, T+1):

    lens = []
    new_words = [['*']*15 for _ in range(5)]
    words = [list(input()) for _ in range(5)]
    for i in range(5):
        lens.append(len(words[i]))
    for i in range(5):
            for j in range(lens[i]):
                new_words[i][j] = words[i][j]
    ans = ''
    for j in range(15):
        for i in range(5):
            if new_words[i][j] != '*':
                ans += new_words[i][j]
    print(f'#{test_case} {ans}')