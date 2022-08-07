#40시간을 초과한 시간의 시급을 1.5배하여 급여
def computepay(hours, rate):
    hr=float(hours)
    rt=float(rate)
    if hr <= 40 :
        py=hr*rt
    else :
        py=40*rt+(hr-40)*rt*1.5
    return py

#40시간을 초과한 시간의 시급을 1.5배하여 급여
hr=input('Enter hours: ')
rt=input('Enter rate: ')

print("pay =", computepay(hr, rt))