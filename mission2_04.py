#bus fare calculator: Input age and payment method
def bfare_calc(age, pmthd):
    if age < 8 or age >= 75:
        return '무료'
    elif age < 14:
        return '450원'
    elif age < 20:
        if pmthd == '카드':
            return '720원'
        else:
            return '1000원'
    elif age >= 20: 
        if pmthd == '카드':
            return '1200원'
        else:
            return '1300원'
            
while True:
    yage = input("당신의 나이는? ")
    if yage == '' or int(yage) < 0:
        print("정확한 나이를 입력하세요!")
        continue
    else:
        break
while True:
    paymd = input("당신의 지불 유형은(카드 / 현금)? ")
    if paymd in ["카드", "현금"]:
        break
    else:
        print("정확한 지불 유형(카드 / 현금)을 입력하세요!")
        continue
        
busfr = bfare_calc(int(yage), paymd)
print("나이 : ", yage,"세\n지불유형 : ", paymd,"\n버스요금 : ", busfr)