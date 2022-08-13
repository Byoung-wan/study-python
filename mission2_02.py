#Calculate monthly payment as yearly payment
def yearly_payment(monpay):
    yearpay = monpay*12
    if yearpay <= 12000000:
        return yearpay, int(yearpay - yearpay*6/100)
    elif yearpay <= 46000000:
        return yearpay, int(yearpay - yearpay*15/100)
    elif yearpay <= 88000000:
        return yearpay, int(yearpay - yearpay*24/100)
    elif yearpay <= 150000000: 
        return yearpay, int(yearpay - yearpay*35/100)
    elif yearpay <= 300000000:
        return yearpay, int(yearpay - yearpay*38/100)
    elif yearpay <= 500000000:
        return yearpay, int(yearpay - yearpay*40/100)
    else :
        return yearpay, int(yearpay - yearpay*42/100)
   
while True:
    monp = input("당신의 월급은 (단위:만원)? ")
    try:
        monp=int(monp)*10000
        break
    except:
        print("정확한 값을 입력하세요!")
        continue
        
btaxyp, ataxyp = yearly_payment(monp)
print("세전 연봉: ", int(btaxyp/10000),"만원\n세후 연봉: ", int(ataxyp/10000),"만원")