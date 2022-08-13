#입력받은 전체 글에서 특정 글자의 수 세기, txt파일 저장
def count_word(in_text, t_word):
    save_txt = open('d:\\in_text.txt','w')    #txt파일 저장할 폴더 및 파일명 지정
    save_txt.write(in_text)
    save_txt.close()
    list_text = in_text.split()
    cnt = 0
    for word in list_text:
        if word.find(t_word) > 0:
            cnt += 1
    print("\n'"+t_word+"' 의 갯수는 : ",cnt)

a = input('전체 글을 입력하세요 : ')
b = input('특정 글자를 입력하세요 : ')
count_word(a, b)