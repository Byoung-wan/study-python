#print even number and median between two numbers
#function for median
def median(fn, tn):
    in_list = [i for i in range(fn,tn+1)]
    sr_list = sorted(in_list)   #무작의(random) 수들의 중앙값을 위한 정렬
    len_list = len(in_list)
    half_list = int(len_list/2)
    result = 0
    if len_list < 2:
        return in_list[0]
    elif len_list % 2 == 0:
        result = (sr_list[half_list] + sr_list[half_list-1]) / 2
        return result
    else:
        return sr_list[half_list]

#function for even numbers
def find_even_number(fnum, tnum):
    med = median(fnum, tnum)
    for num in range(fnum,tnum+1):
        if num % 2 == 0: 
            print(num,"짝수") 
            if num == med:
                print(med,"중앙값")
        
#Input
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
#Output
find_even_number(n, m)