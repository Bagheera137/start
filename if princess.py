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

# if princess=="прекрасная":
#     print("принцеса вышла погулять")
#     print("по дороге она встретила людоеда и он её съел")
# else:
#     if weather=="солнечная":
#         print("ужасная принцеса решилась выйти прогуляться")
#         if lydaed == "голодный":
#             print("по дороге она встретила людоеда и он её съел")
#         else:
#             print("он подумал и сказал,что не голоден, и не стал её есть ")
#     else:
#         print("принцеса осталась дома,людоед был", lydaed)

if princess=="прекрасная":
    print("принцеса вышла погулять")
    print("по дороге она встретила людоеда и он её съел")
elif weather=="солнечная" and lydaed == "голодный":
    print("ужасная принцеса решилась выйти прогуляться")
    print("по дороге она встретила людоеда и он её съел")
elif weather=="солнечная" and lydaed == "сытый":
    print("ужасная принцеса решилась выйти прогуляться, по дороге она встретила людоеда")
    print("он подумал и сказал,что не голоден, и не стал её есть ")
else:
    print("принцеса осталась дома,людоед был", lydaed)