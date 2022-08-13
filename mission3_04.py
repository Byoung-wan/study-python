#count prime numbers between two numbers
def prime_chk(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
    
def prime_cnt(fnum, tnum):
    cnt = 0
    for i in range(fnum+1,tnum):
        if prime_chk(i):
            cnt += 1
    return cnt
                
#Input
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
#Output
print('소수개수 : ',prime_cnt(n, m))