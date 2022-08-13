#방명록 전화번호 검증, txt파일 저장
def wrong_phnno(phn_no):
    if len(phn_no) != 13:
        return True
    elif not phn_no.startswith('010'):
        return True
    elif not phn_no.replace('-','').isdigit():    #숫자가 아닌 문자 입력 체크
        return True
    elif len(phn_no.replace('-','')) != 11:    #"-"의 갯수가 2개인지 체크
        return True
    elif phn_no[3] != '-' or phn_no[8] != '-':
        return True
    else:
        return False

def wrong_guest_book(guest_book):
    save_txt = open('d:\\guest_book.txt','w')    #txt파일 저장할 폴더 및 파일명 지정
    save_txt.write(guest_book)
    save_txt.close()
    list_book = guest_book.split()
    for line in list_book:
        line = line.strip()
        compos = line.find(",")
        name = line[ : compos]
        phone_no = line[compos+1 : ]
        if wrong_phnno(phone_no):
            print("\n잘못 쓴 사람: "+name+"\n잘못 쓴 번호: "+phone_no)
        
gst_bk = input('guest_book = ')
wrong_guest_book(gst_bk)