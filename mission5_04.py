#5주차 미션 Q4 - 날짜를 넣으면 100일 뒤가 몇 월 며칠인지 계산해주는 함수
"""
조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다.
조건2 - 몇 년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.
조건3 - 100일 뒤 요일은 입력요일의 다음 요일로 설정
"""

def after_100(month, date, day):
    date_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_list = ['월', '화', '수', '목', '금', '토', '일']
    mon = month
    cnt = 0
    if day_list.index(day) == 6:
        a_100_day = day_list[0]
    else:
        a_100_day = day_list[day_list.index(day)+1]


    while cnt < 100:
        if mon == month:
            cnt = cnt + (date_list[mon-1] - date + 1)
        else:
            cnt = cnt + date_list[mon-1]
    
        if cnt > 100:
            prt_from = f'{month}월 {date}일 {day}요일'
            prt_to = f'{mon}월 {date_list[mon-1]-(cnt-100)}일 {a_100_day}요일'
            print(f'{prt_from}부터 100일 뒤는 {prt_to}')
            break
    
        if mon == 12:
            mon = 1
        else:
            mon += 1
                
a, b, c = input('월, 일, 요일을 각각 입력하세요: ').split()
after_100(int(a),int(b),c)