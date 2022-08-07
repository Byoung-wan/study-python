while True:
    fname=input('Enter fime name: ')
    try:
        fhand=open(fname)
        break
    except:
        print('Invalid file name...\nEnter valid file name!')
        #print('Invalid file name',fname)
        #quit()
        continue
cnt=0
for line in fhand:
    cnt=cnt+1
    ln=line.rstrip()
    #if not ln.startswith("From:"):
    if not '@uct.ac.za' in ln:
        continue
    print(ln)
print('Line count:', cnt)