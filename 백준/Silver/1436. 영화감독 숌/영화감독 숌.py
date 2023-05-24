N = int(input())
limit = 1000000000
answer = 0
for i in range(666, limit+1):
    i = str(i)
    if '666' in i:
        answer += 1
        if answer == N:
            print(i)
            break