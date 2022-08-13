#5주차 미션 Q3 - 컴퓨터가 임의로 만든 숫자 3개를 맞추기 게임
"""
조건1 - 숫자는 0 ~ 100까지 숫자를 3개 만듭니다(중복 불가).
조건2 - 5회, 10회까지 정답을 못 맞추면 최솟값, 최대값에 대한 힌트를 줍니다.
조건3 - 정답을 맞추면, 맞춘 정답이 최솟값인지, 중간값인지, 최댓값인지 알려줍니다.
"""

import random

com_nums = []
while len(com_nums) < 3:        #숫자는 0 ~ 100까지 3개 (중복 불가)
    number = random.randint(0, 100)
    if number not in com_nums:
        com_nums.append(number)
com_nums.sort()
print(f'컴퓨터 임의 숫자: {com_nums}')  # Test

def suc_num_info(suc_num):
    num_info_list = ['최솟값', '중간값', '최댓값']
    num_info = num_info_list[com_nums.index(suc_num)]
    print(f'숫자를 맞추셨습니다! {suc_num}는 {num_info}입니다.')

def hint_info(t_cnt, m_num):    #5회차 입력값과 최솟값 비교 출력, 10회차 입력값과 최대값 비교 출력
    if t_cnt == 5:
        if com_nums[0] < m_num:
            print(f'최솟값은 {m_num}보다 작습니다')
        else:
            print(f'최솟값은 {m_num}보다 큽니다')
    if t_cnt == 10:
        if com_nums[2] < m_num:
            print(f'최대값은 {m_num}보다 작습니다')
        else:
            print(f'최대값은 {m_num}보다 큽니다')
    
    
def guess_numbers():
    my_num_list = []    #입력값 중복 여부 확인용 리스트
    try_cnt = 1         #시도횟수
    suc_cnt = 0         #성공횟수 
    while suc_cnt < 3:
        print(f'{try_cnt}차 시도')
        my_num = int(input("숫자를 예측해보세요 : "))
        if my_num in my_num_list:
            print(f'{my_num}는 이미 예측에 사용한 숫자입니다')
            if try_cnt in [5, 10] and suc_cnt == 0:
                hint_info(try_cnt, my_num)
            try_cnt += 1
            my_num_list.append(my_num)
            continue
        if my_num not in com_nums:
            print(f'{my_num}는 없습니다')
            if try_cnt in [5, 10] and suc_cnt == 0:
                hint_info(try_cnt, my_num)
            try_cnt += 1
            my_num_list.append(my_num)
            continue
        else:
            suc_num_info(my_num)
            try_cnt += 1
            suc_cnt += 1
            my_num_list.append(my_num)
            continue
    print(f'게임종료\n{try_cnt-1}번 시도만에 예측 성공')
        
#main
guess_numbers()