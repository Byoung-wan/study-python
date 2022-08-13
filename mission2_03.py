#Credit converter: Score Input Credit Output
def credit_conv(score):
    if score >= 95:
        return 'A+'
    elif score >= 90:
        return 'A'
    elif score >= 85:
        return 'B+'
    elif score >= 80: 
        return 'B'
    elif score >= 75:
        return 'C+'
    elif score >= 70:
        return 'C'
    elif score >= 65:
        return 'D+'
    elif score >= 60:
        return 'D'
    else :
        return 'F'

while True:
    nm = input("당신의 이름은? ")
    if nm == '':
        print("정확한 이름을 입력하세요!")
        continue
    else:
        break
while True:
    scr = input("당신의 점수는? ")
    if int(scr) > 100 or int(scr) < 0:
        print("정확한 점수를 입력하세요!")
        continue
    else:
        break
        
credit = credit_conv(int(scr))
print("학생이름 : ", nm,"\n점수 : ", scr,"\n학점 : ", credit)