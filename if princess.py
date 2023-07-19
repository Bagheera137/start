import random
a=["ужасная","прекрасная"]
b=["дождливая","солнечная"]
c=["голодный","сытый"]
princess=random.choice(a)
weather=random.choice(b)
lydaed=random.choice(c)
print("принцеса была",princess)
print("погода была",weather)
print("по лесу бродил",lydaed,"людоед")
if princess=="прекрасная":
    print("принцеса вышла погулять")
else:
    if weather=="солнечная":
        print("ужасная принцеса решилась выйти прогуляться")
    else:
        print("принцеса осталась дома")