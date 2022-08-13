#advanced rock-scissors-paper game with computer
import random

def rsp_advanced(games):
    cnt = 0
    record = [0, 0, 0]
    rsp_name = ["가위","바위","보"]
    while cnt < games:
        my_rsp = input("\n가위 바위 보 : ")
        if my_rsp in ['0','1','2']:
            my_rsp = int(my_rsp)
        elif my_rsp in rsp_name:
            my_rsp = rsp_name.index(my_rsp)
        else:
            print("정확한 값을 입력하세요!")
            continue
        cnt += 1
        com_rsp = random.randint(0, 2)
        print("나: "+rsp_name[my_rsp])
        print("컴퓨터: "+rsp_name[com_rsp])
        if my_rsp==com_rsp:
            print(cnt,"번째 판 무승부!")
            record[1] = record[1]+1
        elif com_rsp-my_rsp in [-2,1]:
            print(cnt,"번째 판 컴퓨터의 승리!")
            record[2] = record[2]+1
        elif com_rsp-my_rsp in [-1,2]:
            print(cnt,"번째 판 나의 승리!")
            record[0] = record[0]+1
    print("\n나의 전적: {} 승 {} 무 {} 패".format(record[0], record[1], record[2]))
    print("\n컴퓨터의 전적: {} 승 {} 무 {} 패".format(record[2], record[1], record[0]))

#Input
games = int(input("몇 판을 진행하시겠습니까? : "))
#Output
rsp_advanced(games)