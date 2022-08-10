#CodeUp- 6050: [기초-비교연산] 정수 2개 입력받아 비교3
a,b = input().split()
print(int(a) <= int(b))


#CodeUp- 6051: [기초-비교연산] 정수 2개 입력받아 비교4
a,b = input().split()
if int(a) != int(b):
    print('True')
else:    
    print('False')


#CodeUp- 6052: [기초-논리연산] 정수 입력받아 참 거짓 평가
a = int(input())
print(bool(a != 0))


#CodeUp- 6053: [기초-논리연산] 참 거짓 바꾸기
print(not bool(int(input())))


#CodeUp- 6054: [기초-논리연산] 둘 다 참일 경우만 참 출력
a,b = input().split()
print(bool(int(a)) and bool(int(b)))


#CodeUp- 6055: [기초-논리연산] 하나라도 참이면 참 출력
a,b = input().split()
print(bool(int(a)) or bool(int(b)))


#CodeUp- 6056: [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력
a,b = input().split()
print(bool(int(a)) != bool(int(b)))


#CodeUp- 6057: [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력
a,b = input().split()
print(bool(int(a)) == bool(int(b)))


#CodeUp- 6058: [기초-논리연산] 둘 다 거짓일 경우만 참 출력
a,b = input().split()
c = bool(int(a)) or bool(int(b))
print(not c)


#CodeUp- 6059: [기초-비트단위논리연산] 비트단위로 NOT 하여 출력
a = int(input())
print(~a)


#CodeUp- 6060: [기초-비트단위논리연산] 비트단위로 AND 하여 출력
a,b = input().split()
print(int(a)&int(b))


#CodeUp- 6061: [기초-비트단위논리연산] 비트단위로 OR 하여 출력
a,b = input().split()
print(int(a)|int(b))


#CodeUp- 6062: [기초-비트단위논리연산] 비트단위로 XOR 하여 출력
a,b = input().split()
print(int(a)^int(b))


#CodeUp- 6063: [기초-3항연산] 정수 2개 입력받아 큰 값 출력
a,b = input().split()
a = int(a)
b = int(b)
c = a-b
if c>0 :
    print(a)
elif c<0 :
    print(b)
else:
    print(a,"=",b,"입니다")


#CodeUp- 6064: 입력받은 세 정수 중 최소걊 출력
a = input().split()
for i in a:
    i = int(i)   
print(sorted(a)[0])


#CodeUp- 6065: 입력받은 세 정수 중 짝수만 출력
a = input().split()
for i in a:
    if int(i) % 2 == 0:
        print(i)


#CodeUp- 6066: 입력받은 세 정수 짝수, 홀수 확인 출력
a = input().split()
for i in a:
    if int(i) % 2 == 0:
        print('even')
    else:
        print('odd')


#CodeUp- 6067: 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분 출력
a = input()
rst = ['A', 'B', 'C', 'D']

for i in range(4):
    for s in range(2):
        if int(a) % 2 == 0:
            print(rst[i])
        else:
            print('odd')


#CodeUp- 6068: 점수(정수, 0 ~ 100)를 입력받아 평가 출력
a = int(input())
scr_list = [90, 70, 40, 0]
rate_list = ['A', 'B', 'C', 'D']

for i in range(len(scr_list)):
    if a >= scr_list[i]:
        print(rate_list[i])
        break


#CodeUp- 6069: 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력
a = input()
rate_list = ['A', 'B', 'C', 'D']
cont_list = ['best!!!', 'good!!', 'run!', 'slowly~']

if a not in rate_list:
    print('what?')
else:
    for i in range(len(rate_list)):
        if a == rate_list[i]:
            print(cont_list[i])
            break


#CodeUp- 6070: 월(month)이 입력될 때 계절(season) 이름이 출력
a = int(input())
mon_tup = ([12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11])
sean_list = ['winter', 'spring', 'summer', 'fall']

for i in range(len(mon_tup)):
    if a in mon_tup[i]:
        print(sean_list[i])
        break


#Codeup-6071: [기초-반복실행구조] 0 입력될 때까지 무한 출력
while True:
    a= input()
    if a == 0 or a == '0':
        break
    else:
        print(a)


#6072 : [기초-반복실행구조] 정수(0~100) 1개 입력받아 카운트다운 출력
while True:
    num = int(input())
    if num < 0 or num > 100:
        continue
    else:
        for i in range(0, num+1):
            print(i)
        break


#CodeUp-6073: [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력
while True:
    a= int(input())
    if a < 0 or a > 100:
        continue
    else:
        for i in range(a-1, -1, -1):
            print(i)
        break


#CodeUp=6074: 기초-반복실행구조] 문자 1개 입력받아 알파벳 출력
#알파벳 문자 ?의 정수값은 ord('?'), 정수 ?의 알파벳 문자는 chr('?')
while True:
    aipha= input()
    if aipha == '':
        continue
    else:
        for i in range(ord('a'), ord(aipha)+1):
            print(chr(i),end=' ')
        break


#CodeUp-6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력
while True:
    a= int(input())
    if a < 0 or a > 100:
        continue
    else:
        for i in range(a, 0, -1):
            print(i)
        break


#CodeUp-6076: 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력
a = int(input())
for i in range(a+1):
    print(i)


#CodeUp-6077: 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합 출력
a = int(input()) 
b = 0 
for i in range(1,a+1):
    if i % 2 == 0:
        b = b + i 
print(b)


#CodeUp-6078: 영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력
a = None
while a != 'q':
    a = input()
    print(a)


#CodeUp-6079: 1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만 계속 더하는 프로그램
a = int(input())
b = 0
sum = 0
while sum < a:
    b += 1
    sum = sum + b
print(b)


#CodeUp-6080: 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때, 나올 수 있는 모든 경우를 출력
#서로 다른 주사위 2개의 면의 개수 n, m이 공백을 두고 입력, 단, n, m은 10이하의 자연수
a, b = input().split()
a = int(a)
b = int(b)
for i in range(1,a+1):
    for j in range(1,b+1):
        print(i,j)
a, b = input().split()
a = int(a)
b = int(b)
for i in range(1,a+1):
    for j in range(1,b+1):
        print(i,j)


#CodeUp-6081: A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.(단, A ~ F 까지만 입력된다.)
#print('%X'%n)    #n에 저장되어있는 값을 16진수(hexadecimal) 형태로 출력
a = input()
b = int(a,16)    #16진수 정수로 변환
for i in range(1,16):
    print(a+"*"+'%X'%i+"="+'%X'%(b*i))


#CodeUp-6082: 1 부터 n(30 보다 작은 정수 1개)까지 순서대로 공백을 두고 수를 출력하는데, 3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력
a = int(input())
for i in range(1,a+1):
    if i % 10 in [3,6,9]:
        print('X',end=' ')
    else:
        print(str(i),end=' ')


#CodeUp-6083: [기초-종합] 빛 섞어 색 만들기
r, g, b = input().split()
a = 0
for i in range(int(r)):
    for j in range(int(g)):
        for k in range(int(b)):
            print(i, j, k)
            a += 1
print(a)


#COdeUp-6084 : [기초-종합] 소리 파일 저장용량 계산하기
#1초 동안 마이크로 소리강약을 체크하는 횟수 h(헤르쯔), 비트수 b, 채널 개수 c, 녹음할 시간(초) s -  MB 단위로 바꾸어 출력
h, b, c, s = input().split()
save_bit = int(h) * int(b) *  int(c) * int(s)
m_byte = save_bit / 8 / 1024 / 1024    # bit => byte(8) - KB(1024) - MB(1024)
print(round(m_byte,1),'MB')