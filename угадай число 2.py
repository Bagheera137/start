import random
pop=1
b=random.randint(1,1)
a=0
while a!=b:
    a = input("угадай число " + str(pop) + " попытка")
    isn = a.isnumeric()
    if  isn==False:
        print("нужно вводить число")
        continue
    a = int(a)
    pop = pop + 1
    if a>b:
        print("моё число меньше")
        continue
    if a<b:
        print("моё число больше")
        continue
    print("вы угадали число")
