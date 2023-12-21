import random
import time
import math
import wrap

wrap.world.create_world(400,600)
wrap.world.set_back_color(123,221,100)
crab=wrap.sprite.add("mario-enemies", 350, 600, "crab")



mario=wrap.sprite.add("mario-3-big", 50, 400, "fireball")
wrap.sprite.set_size(mario, random.randint(20, 40), random.randint(20, 150))



fire=time.time()
mush=time.time()
speed=-7
a=-5
c = time.time()
w=time.time()-c
tx=wrap.sprite.add_text(str(int(w))+" секунд", 200, 300)
fireball=None
while True:
    wrap.sprite.move(mario, 0, speed)

    get = wrap.sprite.get_top(mario)
    bot = wrap.sprite.get_bottom(mario)
    mariox=wrap.sprite.get_x(mario)
    marioy=wrap.sprite.get_y(mario)




    if get <= 0:
        speed=7
    if bot >= 600:
        speed=-7

    w=time.time()-c
    wrap.sprite_text.set_text(tx,str(int(w))+ " секунд")
    #print(w ,"секунд")


    wrap.sprite.move(crab, 0, a)

    get1 = wrap.sprite.get_top(crab)
    bot1 = wrap.sprite.get_bottom(crab)
    if get1 <= 0:
        a=7
    if bot1 >= 600:
        a=-7

    rasfire = time.time() - fire
    #print(speed)
    if rasfire >= 3:
        gety=wrap.sprite.get_y(mario)
        fireball=wrap.sprite.add("mario-enemies", 60, gety, "fire_ball")
        fire = time.time()
        crabx = wrap.sprite.get_x(crab)
        craby = wrap.sprite.get_y(crab)

    if fireball !=None:
        wrap.sprite.move_at_angle_point(fireball, crabx, craby, 70)
        col=wrap.sprite.is_collide_sprite(fireball,crab)
        print(col)

        if col:
            break
while True:

    wrap.sprite.move(crab,0,7)
    angle=wrap.sprite.get_angle(crab)
    wrap.sprite.set_angle(crab,angle+10)







    # rasmush = time.time() - mush
    # if rasmush >= 3:
    #     gety1=wrap.sprite.get_y(crab)
    #     wrap.sprite.add("mario-enemies", 340, gety1, "mushroom")
    #     mush = time.time()

