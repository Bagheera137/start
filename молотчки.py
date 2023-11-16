import random

import wrap

wrap.world.create_world(400,600)

crab=wrap.sprite.add("mario-enemies", 350, 600, "crab")



fireball=wrap.sprite.add("mario-3-big", 50, 400, "fireball")
wrap.sprite.set_size(fireball,random.randint(20,40),random.randint(20,150))


b=-7
a=-5
while True:
    wrap.sprite.move(fireball, 0, b)

    get = wrap.sprite.get_top(fireball)
    bot = wrap.sprite.get_bottom(fireball)
    if get <= 0:
        b=7
    if bot >= 600:
        b=-7

    wrap.sprite.move(crab, 0, a)

    get1 = wrap.sprite.get_top(crab)
    bot1 = wrap.sprite.get_bottom(crab)
    if get1 <= 0:
        a=7
    if bot1 >= 600:
        a=-7


