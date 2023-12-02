import random
counta=0
countc=0
a=[random.randint(1,10) ,random.randint(1,10),random.randint(1,10)]
c=[random.randint(1,10) ,random.randint(1,10),random.randint(1,10)]

if a[0]>c[0]:
    print("в первом тайме победила команда A")
    counta=counta+1
else:
    print("в первом тайме победила команда С")
    countc = countc + 1

if a[1] > c[1]:
    print("во втором тайме победила команда A")
    counta = counta + 1
else:
    print("во втором тайме победила команда С")
    countc = countc + 1

if a[2] > c[2]:
    print("в третьем тайме победила команда A")
    counta = counta + 1
else:
    print("в третьем тайме победила команда С")
    countc = countc + 1

if counta>countc:
    print("победила команда А")
else:
    print("победила команда С")
print(a)
print(c)
print("с общим счётом",counta,countc)
a[2]=a[2]+10

print(a)