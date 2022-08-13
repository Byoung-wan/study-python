#rock-scissors-paper game with computer
import random

def rep(choice):
    if choice == '가위' or choice == '0':
        return 0
    elif choice == '바위' or choice == '1':
        return 1
    elif choice == '보' or choice == '2':
        return 2
   
while True:
    my = input("당신의 선택은? 가위=0, 바위=1, 보=2 :")
    if my in ["가위", "바위", "보", "0", "1", "2"]:
        break
    else:
        print("정확한 값을 입력하세요!")
        continue
        
mychoice = rep(my)
computer = random.randint(0,2)

if mychoice == 0 :
    if computer == 0:
        print("나: 가위\n컴퓨터: 가위\n비김!")
    elif computer == 1:
        print("나: 가위\n컴퓨터: 바위\n컴퓨터 승리!")
    elif computer == 2:
        print("나: 가위\n컴퓨터: 보\n나 승리!")        
elif mychoice == 1 :
    if computer == 0:
        print("나: 바위\n컴퓨터: 가위\n나 승리!")
    elif computer == 1:
        print("나: 바위\n컴퓨터: 바위\n비김!")
    elif computer == 2:
        print("나: 바위\n컴퓨터: 보\n컴퓨터 승리!")
elif mychoice == 2 :
    if computer == 0:
        print("나: 보\n컴퓨터: 가위\n컴퓨터 승리!")
    elif computer == 1:
        print("나: 보\n컴퓨터: 바위\n나 승리!")
    elif computer == 2:
        print("나: 보\n컴퓨터: 보\n비김!")