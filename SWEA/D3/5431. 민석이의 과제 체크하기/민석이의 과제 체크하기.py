T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # N은 수강생의 수 K 는 제출한 학생의 수
    submission = list(map(int, input().split()))  # 과제를 제출한 학생들의 번호
    student = range(1, N + 1)
    answer = [x for x in student if x not in submission]
    print(f'#{test_case}', *answer)
