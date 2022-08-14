C = int(input())
for test_case in range(C):
    N_scores = list(map(int, input().split()))
    N = N_scores[0]
    scores = N_scores[1:]
    sum_of_scores = 0
    smart_student = 0
    for score in scores:
        sum_of_scores += score
    mean_of_scores = sum_of_scores/N
    for i in range(N):
        if scores[i] > mean_of_scores:
            smart_student += 1
    ratio_smart_student = (smart_student/N)*100
    print('{:.3f}%'.format(ratio_smart_student))