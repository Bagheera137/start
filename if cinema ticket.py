
print("дайте пожалуйста билет на фильм Астрал")
a=input("Сколько вам лет?")
a=int(a)
if a<=4 and a>=1:
    print("что то не верится..")
    exit()
if a<=8 and a>=5:
    print("где ты взял деньги малыш?")
    exit()
if a<=12 and a>=9:
    print("до 12 лет не пускаем")
    exit()
if a<=16 and a>=12:
    b=input("а родители с тобой пойдут?")
    if "да"==b:
        print("хорошо,проходите")
    else:
        print("без родителей нельзя")
    exit()
print("проходите")