T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    sentence = input()
    sentence = sentence.replace(',', '.').replace('?', '.').replace('!', '.')
    sentence = sentence.split('.')
    # print(sentence)
    name = [[] for _ in range(N)]
    # print(name)
    for i in range(N):
        sentence[i] = sentence[i].split()
    # print(sentence)
    for i in range(N):
        for j in range(len(sentence[i])):
            if sentence[i][j].istitle() and sentence[i][j].isalpha():
                name[i].append(sentence[i][j])
    print(f'#{test_case}', end=' ')
    for i in range(len(name)):
        print(len(name[i]), end=' ')
    print()
