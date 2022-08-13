#gugudan under specific condition
def gugudan(num):
    print(num,"단")
    for i in range (1,10,2):
        result = num * i
        if result <= 50:
            print(num,"X",i,"=", result)

#Input
number = int(input("몇 단? : "))
#Output
gugudan(number)