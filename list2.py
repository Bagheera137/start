import random
b=random.randint(10,30)
a=[]
v=[]
for i in range(b):
    a.append(random.randint(30,60))
    v.append(random.randint(10,18))
print(a)
print(v)

a1=[]
a2=[]
a3=[]

for b in a:
    if b<40:
        a1.append(b)

    if b>=40 and b<50:
        a2.append(b)

    if b>=50:
        a3.append(b)
print(a1)
print(a2)
print(a3)

m=a[0]
i=0
for c in range(len(a)):
    if a[c]>m:
        m=a[c]
        i=c

print("самый тяжёлый участник " + str(m) + " кг, " + str(v[i]) + " лет")

m=a[0]
i=0
for c in range(len(a)):
    if a[c]<m:
        m=a[c]
        i=c
print("самый лёгкий участник " + str(m) + " кг, " + str(v[i]) + " лет")



