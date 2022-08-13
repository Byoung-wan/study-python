#5주차 미션 Q2 - 학생들 시험 답지, 답안지 => 채점, 학생들의 점수와 등수 출력
answer_papers = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]
key_sheet = [3,2,4,2,5,2,4,3,1,2]

def grading(in_aw):
    score = 0
    for i in range(len(key_sheet)):
        if str(key_sheet[i]) == str(in_aw[i]):
            score += 10
    return str(score)

def grader(aw_list, key_st):
    result_list = []
    f_grade = 0
    for line in aw_list:
        name, ind_aw = line.split(',')
        ind_scr = grading(ind_aw)
        result_list.append(ind_scr+','+name)
    result_list.sort(reverse=True)
    for f_line in result_list:
        f_grade += 1
        f_score, f_name = f_line.split(',')
        print(f'학생: {f_name} 점수: {f_score}점 {f_grade}등')
    
#main
grader(answer_papers, key_sheet)