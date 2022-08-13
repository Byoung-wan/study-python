#생일 입력, 한국 나이, 미국 나이 구하기 프로그램 (2)
from datetime import date, datetime
birth = input('Enter your birthday!  ex)19991231 : ')
birth = {'year': int(birth[0:4]),
         'month': int(birth[4:6]),
         'day': int(birth[6:8]),}
cyear=datetime.now().year
cmonth=datetime.now().month
cday=datetime.now().day
now = {'year': cyear, 'month': cmonth, 'day': cday,}
diff = date(now['year'], now['month'], now['day']) - date(birth['year'], birth['month'], birth['day'])
year = diff.days // 365
print('Korean age : {}'.format(year+1))
print('US age : {}'.format(year))