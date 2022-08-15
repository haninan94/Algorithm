T = int(input()) # test case 입력
counts = T # test case에서 그룹 단어가 아닌것들을 뺄 예정

for test_case in range(T):
    word = input() # 단어 입력받기
    temp= [] # 조건에 맞는 단어들을 넣기 위해 임시 할당
    
    
    for i in range(len(word)-1):
        
        # 만약 i번째 문자와 i+1번째 문자가 같다면 continue (연속되므로)
        if word[i] == word[i+1]:
            if word[i] in temp:
                counts -= 1
                break
            
        # i번째 문자와 i+1번째 문자가 같지않을경우에    
        else:
            
            # i가 만약 문자열 끝의 2개를 비교했을때라면
            if i == len(word)-2:
                
                # 끝에서 2번째 문자가 이미 temp에있는가 ?
                if word[i] in temp:
                    # 있다면 counts 에서 1개 빼고 그룹문자 아니므로 더이상 진행X
                    counts -= 1
                    break
                # 끝에서 1번째 문자가 이미 temp에있는가?
                if word[i+1] in temp:
                    #있다면 counts 에서 1개 빼고 그룹문자 아니므로 더이상 진행X
                    counts -= 1
                    break
                    
            # i와 i+1 의 문자가 같지 않을 경우중에서 i가 len(word)-2가 아닐경우
            else:
                
                # 해당 문자가 temp에 있는가 ?
                if word[i] in temp:
                    # 있다면 counts 에서 1개 빼고 그룹문자 아니므로 더이상 진행X
                    counts -= 1
                    break
                # 해당 문자가 temp에 없다면
                else:
                    # temp에 해당 문자 저장
                    temp.append(word[i])
print(counts)