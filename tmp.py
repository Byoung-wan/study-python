#40시간을 초과한 시간의 시급을 1.5배하여 급여
hr=input('Enter hours: ')
try:
    hr=float(hr)
except:
    hr=input('Enter hours again in number: ')
    hr=float(hr)
    
rt=input('Enter rate: ')
try:
    rt=float(rt)
except:
    rt=input('Enter rate again in number: ')
    rt=float(rt)

rt=float(rt)
if hr <= 40 :
    py=hr*rt
else :
    py=40*rt+(hr-40)*rt*1.5
print('Pay =',py)