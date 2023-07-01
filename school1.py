a = input("введите число")
b = int(a)
d = 0
while b>0:
    c = b%10
    b = b//10
    print(c)
    d = d + c

if d%5==0:
    print("делится")
else:
    print("не делится")
print(a)