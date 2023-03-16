score_sum = 0
grade_sum = 0

while(True):
    try:
        lecture_name, score, grade = input().split(' ')
        score_sum += float(score)
        if grade == 'A+':
            grade_sum += 4.5 * float(score)
        elif grade == 'A0':
            grade_sum += 4 * float(score)
        elif grade == 'B+':
            grade_sum += 3.5 * float(score)
        elif grade == 'B0':
            grade_sum += 3 * float(score)
        elif grade == 'C+':
            grade_sum += 2.5 * float(score)
        elif grade == 'C0':
            grade_sum += 2 * float(score)
        elif grade == 'D+':
            grade_sum += 1.5 * float(score)
        elif grade == 'D0':
            grade_sum += 1 * float(score)
        elif grade == 'F':
            grade_sum += 0 * float(score)
        elif grade == 'P':
            score_sum -= float(score)
    except:
        break

print(grade_sum/score_sum)