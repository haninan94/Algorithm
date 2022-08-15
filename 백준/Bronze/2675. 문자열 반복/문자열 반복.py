T = int(input())
for test_case in range(1, T+1):
    N, word = list(input().split())
    N = int(N)
    for i in range(len(word)):
        print(word[i]*N,end='')
    print()