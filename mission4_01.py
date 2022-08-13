#숫자를 입력 받고 3자리마다 ","를 찍어주는 함수 만들기
def make_comma(in_value):
    out_value = str(in_value)
    cnt = len(out_value)
    rep = (cnt-1) // 3       #","를 찍을 횟수
    if cnt < 4:
        print(out_value)
    else:
        for i in range(rep):
            out_value = out_value[ : cnt-(3*(i+1))]+","+out_value[cnt-(3*(i+1)) : ]
    print(out_value)
           
number = input('숫자를 입력하세요 : ')  #입력값 검증 생략
make_comma(number)