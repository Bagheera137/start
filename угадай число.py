import random
pop=1
a=input("угадай число " + str(pop) + " попытка" )
isn=a.isnumeric()
while isn==False:
    a=input("надо вводить число")
    isn=a.isnumeric()
a=int(a)
b=random.randint(1,1)

while a!=b:
    while a<b:
        pop = pop + 1
        a = input("моё число больше "+str(pop)+ " попытка")
        isn=a.isnumeric()
        while isn==False:
            a = input("надо вводить число")
            isn = a.isnumeric()
        a = int(a)

    while a>b:
        pop = pop + 1
        a = input("моё число меньше "+str(pop)+ " попытка")
        a = int(a)
a = int(a)
print("угадал с ", pop ,"попытки")

