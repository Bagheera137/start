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

def udar(name,cuda):

    cr1 = wrap.sprite.get_right(cub1)
    cl2 = wrap.sprite.get_left(cub2)
    cr3 = wrap.sprite.get_right(cub3)
    cl4 = wrap.sprite.get_left(cub4)
    wid = wrap.sprite.get_width(ball) / 2
    if cuda=="raz":
        wrap.actions.move_to(ball,random.randint(cr1+2+wid,cl2-2-wid),40)
    else:
        wrap.actions.move_to(ball, random.randint(cr3+2+wid, cl4-2-wid),460)

wrap.world.create_world(400, 600, 900, 50)
wrap.world.set_back_color(234, 100, 200)

cub1=wrap.sprite.add("battle_city_items", 125, 50, "block_brick")
cub2=wrap.sprite.add("battle_city_items", 275, 50, "block_brick")
cub3=wrap.sprite.add("battle_city_items", 125, 450, "block_brick")
cub4=wrap.sprite.add("battle_city_items", 275, 450, "block_brick")


mario1=wrap.sprite.add("mario-1-small", 100, 100, "stand")
mario2=wrap.sprite.add("mario-1-small", 200, 300, "stand")
mario3=wrap.sprite.add("mario-1-small", 300, 100, "stand")
mario4=wrap.sprite.add("mario-enemies", 100, 300, "dragon_throw2")
ball=wrap.sprite.add("mario-enemies", 200, 300, "beetle_blue_go")
wrap.actions.set_size_percent(ball, 50, 50, 0)

day_pass(mario2,"right",mario2)
day_pass(mario2,"left",mario2)
day_pass(mario2,"left",mario1)
day_pass(mario1,"left",mario4)
mimo(100,230)
shvati_ball(mario4,"left")
udar(mario4,"raz2")








