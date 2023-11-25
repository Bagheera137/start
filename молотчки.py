import random
import time

import wrap

wrap.world.create_world(400,600)
wrap.world.set_back_color(123,221,100)
crab=wrap.sprite.add("mario-enemies", 350, 600, "crab")



fireball=wrap.sprite.add("mario-3-big", 50, 400, "fireball")
wrap.sprite.set_size(fireball,random.randint(20,40),random.randint(20,150))


b=-7
a=-5
c = time.time()
w=time.time()-c
tx=wrap.sprite.add_text(str(int(w))+" секунд", 200, 300)

while True:
    wrap.sprite.move(fireball, 0, b)

    get = wrap.sprite.get_top(fireball)
    bot = wrap.sprite.get_bottom(fireball)
    if get <= 0:
        b=7
    if bot >= 600:
        b=-7

    w=time.time()-c
    wrap.sprite_text.set_text(tx,str(int(w))+ " секунд")
    print(w ,"секунд")

    if int(w)==5:
        c = time.time()

    wrap.sprite.move(crab, 0, a)

    get1 = wrap.sprite.get_top(crab)
    bot1 = wrap.sprite.get_bottom(crab)
    if get1 <= 0:
        a=7
    if bot1 >= 600:
        a=-7


