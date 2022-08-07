while True:
    n = input('정수 or 실수 입력:')
    n1=(n.replace('-',''))
    n2=(n.replace('.',''))
    if (not n.isdigit()) and (not n1.isdigit()) and (not n2.isdigit()) :
       print('잘못된 값입니다. 다시 입력해 주세요')
    else :
        #n= float(n)
        break
print(f'{n}을 입력하셨습니다.') 

'''
while True:
    try:
        number = int(input("정수 입력: "))
        break
    except ValueError:
        print ("잘못된 값입니다. 다시 입력해 주세요")
print(f"입력된 값은 {number} 입니다")
'''