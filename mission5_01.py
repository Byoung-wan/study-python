#5주차 미션 Q1 - 베스킨라빈스31 게임
"""
조건1 - 나의 턴에서는 숫자를 직접 입력하며 한 번 입력 후에 space 한 번으로 구분
        my = input("My turn - 숫자를 입력하세요: ")
조건2 - 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음
조건3 - 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6)
        위 조건이 안맞을 경우 다시 입력
"""

import random 

def input_chk(in_nums, c_num):
    if len(in_nums) == 0 or len(in_nums) > 3:    #입력값 없거나 4개 이상이면 에러 
        return False
    elif int(in_nums[0]) != c_num+1:                  #입력된 처음값이 현재값보다 1크지 않으면 에러 
        return False
    elif len(in_nums) == 2 and int(in_nums[1]) != int(in_nums[0])+1:    #외쳐진 숫자보다 1큰 수만 외칠수 있음 check
        return False
    elif len(in_nums) == 3 and (int(in_nums[1]) != int(in_nums[0])+1 or int(in_nums[2]) != int(in_nums[1])+1):
        return False
    else:
        print(f'현재 숫자 : {in_nums[-1]}')
        return True

def com_turn_nums(c2_num):
    com_nums = list()
    for i in range(random.randint(1,3)):
        c2_num += 1
        print(f'컴퓨터 : {c2_num}')
        com_nums.append(c2_num)
        print(f'현재 숫자 : {com_nums[-1]}')
        if c2_num == 30:              #컴퓨터의 랜덤 값과 무관하게 30에서 종료
            return c2_num
    return c2_num
        
def bs31():
    cur_num = 0
    my_nums = list()
    print('베스킨라빈스 써리원 게임\n------------------')
    
    while cur_num < 31:
        if cur_num == 30:
            print('컴퓨터 승! 나의 패배!')
            break
        my_nums = input('My turn - 숫자를 입력하세요: ').split()
        if input_chk(my_nums, cur_num):             #나의 입력값 확인
            cur_num = int(my_nums[-1])          
            if cur_num == 30:
                print('나의 승! 컴퓨터 패배!')
                break
            else:
                cur_num = com_turn_nums(cur_num)    #컴퓨터의 입력값 확인
        else:
            continue
                
#main
bs31()