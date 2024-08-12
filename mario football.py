import random
import time
import math
import wrap

def day_pass(who, storona,comy ):
    """
    def передаёт пасс если мячик стоит рядом с марио
    :param who:
    :param storona:
    :return:
    """
    x=wrap.sprite.get_x(who)
    namey=wrap.sprite.get_y(who)
    y=wrap.sprite.get_bottom(comy)
    z=wrap.sprite.get_right(comy)
    l=wrap.sprite.get_left(comy)
    ballx=wrap.sprite.get_x(ball)
    bally=wrap.sprite.get_y(ball)
    ras=math.dist([x,namey],[ballx,bally])




    if ras<40:
        if storona=="right":
            wrap.actions.move_to(ball, z+15, y-10, 900)
        else:
            wrap.actions.move_to(ball, l-15, y-10, 900)



def mimo(x,y):
    wrap.actions.move_to(ball, x, y, 900)

def shvati_ball(name,storona):
    br = wrap.sprite.get_right(ball)
    bl = wrap.sprite.get_left(ball)
    y=wrap.sprite.get_bottom(ball)
    wid=wrap.sprite.get_width(name)/2
    heig=wrap.sprite.get_height(name)/2

    if storona == "right":
        wrap.actions.move_to(name, br+5+wid, y-heig, 900)
    else:
        wrap.actions.move_to(name, bl-5-wid, y-heig, 900)


wrap.world.create_world(400, 600, 900, 50)
wrap.world.set_back_color(234, 100, 200)



mario1=wrap.sprite.add("mario-1-small", 100, 100, "stand")
mario2=wrap.sprite.add("mario-1-small", 200, 300, "stand")
mario3=wrap.sprite.add("mario-1-small", 300, 100, "stand")
mario4=wrap.sprite.add("mario-enemies", 100, 300, "dragon_throw2")
ball=wrap.sprite.add("mario-enemies", 200, 300, "beetle_blue_go")
wrap.actions.set_size_percent(ball, 50, 50, 0)

# day_pass(mario2,"right",mario2)
# day_pass(mario2,"left",mario2)
# day_pass(mario2,"left",mario1)
# day_pass(mario1,"left",mario4)
mimo(100,230)
shvati_ball(mario2,"right")
shvati_ball(mario4,"left")







