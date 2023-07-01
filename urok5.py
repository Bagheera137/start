import wrap
import random
import math
wrap.world.create_world(400,500)
wrap.world.set_back_color(123,71,100)
x1 = random.randint(80,400)
x2 = random.randint(80,400)

spr = wrap.sprite.add("mario-1-big", 50, 50, "climb2")
flower=wrap.sprite.add("mario-items",x1,x2, "flower2",False)
wrap.sprite.add("pacman",50 ,50,"dot")
rass = math.dist([50,50],[x1,x2])

wrap.sprite.add_text("до клада " + str(int(rass)) + "пкс",50,30, text_color= [0,0,0],font_size= 15)
wrap.actions.set_angle_to_point(spr,x1,x2)

a=input("введите координату x")
b=input("введите координату y")
a=int(a)
b=int(b)
wrap.actions.move_to(spr,a,b)

wrap.sprite.add("pacman",a ,b,"dot")
rass=math.dist([a,b],[x1,x2])
wrap.sprite.add_text("до клада " + str(int(rass)) + "пкс",a,b-20, text_color= [0,0,0],font_size= 15)
wrap.actions.set_angle_to_point(spr,x1,x2)
a=input("введите координату x")
b=input("введите координату y")
a=int(a)
b=int(b)
wrap.actions.move_to(spr,a,b)

wrap.sprite.add("pacman",a ,b,"dot")
rass=math.dist([a,b],[x1,x2])
wrap.sprite.add_text("до клада " + str(int(rass)) + "пкс",a,b-20, text_color= [0,0,0],font_size= 15)
wrap.actions.set_angle_to_point(spr,x1,x2)
a=input("введите координату x")
b=input("введите координату y")
a=int(a)
b=int(b)
wrap.actions.move_to(spr,a,b)

wrap.sprite.add("pacman",a ,b,"dot")
rass=math.dist([a,b],[x1,x2])
wrap.sprite.add_text("до клада " + str(int(rass)) + "пкс",a,b-20, text_color= [0,0,0],font_size= 15)
wrap.actions.set_angle_to_point(spr,x1,x2)
wrap.sprite.show(flower)