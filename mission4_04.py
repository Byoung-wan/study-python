#주민등록번호로 출생 년월 및 성별 구분하기
def wrong_idno(id_num):
    if len(id_num) != 14:
        return True
    elif not id_num.replace('-','').isdigit():    #숫자가 아닌 문자 입력 체크
        return True
    elif len(id_num.replace('-','')) != 13:    #"-"의 갯수가 1개인지 체크
        return True
    elif id_num[6] != '-':
        return True
    elif id_num[7] not in ['1','2','3','4']:
        return True
    else:
        return False

def check_input_id():
    while True:
        id = input("당신의 주민등록번호는? ")
        if wrong_idno(id):
            print("잘못된 번호입니다.\n올바른 번호를 넣어주세요.\n")
            continue
        if id[:2] > '21':
            return id
            break
        else:
            chk = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
            if chk == 'o' and id[7] in ['3','4']:
                return id
                break
            elif chk == 'x' and id[7] in ['1','2']:
                return id
                break
            else:
                print("잘못된 번호입니다.\n올바른 번호를 넣어주세요,\n")
                continue

def prt_result(id_no):
    if id_no[7] in ['1','3']:
        gender = '남자'
    elif id_no[7] in ['2','4']:
        gender = '여자'
    if id_no[7] in ['1','2']:
        print("19"+id_no[:2]+"년"+id_no[2:4]+"월 "+gender)
    elif id_no[7] in ['3','4']:
        print("20"+id_no[:2]+"년"+id_no[2:4]+"월 "+gender)
        
in_idno = check_input_id()    #주민등록번호 입력 및 체크
prt_result(in_idno)    #결과값 출력