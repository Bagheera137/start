import random
a=input("угадай число")
a=int(a)
b=random.randint(50,50)
while a!=b:
    while a<b:
       a = input("моё число больше")
       a = int(a)
    while a>b:
        a = input("моё число меньше")
        a = int(a)
    if a==b:
        # a = input("угадай число")
        # a = int(a)
        print("угадал")

