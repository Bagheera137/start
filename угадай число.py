import random
a=input("угадай число")
a=int(a)
b=random.randint(1,10)

while a!=b:
    a = input("угадай число")
    a = int(a)
print("угадал")