import random

import wrap
wrap.world.create_world(700,700)

crab1=wrap.sprite.add("mario-enemies", 350, 400, "crab")
mario1=wrap.sprite.add("mario-3-big", 350, 400, "fireball")
mario2=wrap.sprite.add("mario-3-big", 350, 400, "fireball")
crab2=wrap.sprite.add("mario-enemies", 350, 400, "crab")
crab3=wrap.sprite.add("mario-enemies", 350, 400, "crab")

a=[crab1, mario1,mario2,crab2,crab3]
print(a)

for b in a:
    wid=wrap.sprite.get_width(b)
    hei=wrap.sprite.get_height(b)

    wrap.sprite.move_to(b, random.randint(100, 450), random.randint(100, 450))

    wrap.sprite.set_size(b, random.randint(wid * 1, wid * 3), random.randint(hei * 1, hei * 3))

    right= wrap.sprite.get_right(b)
    y = wrap.sprite.get_y(b)

    fire= wrap.sprite.add("mario-enemies",right ,y, "fire_ball")
    wrap.sprite.move_left_to(fire,right)
    firey=wrap.sprite.get_y(fire)
    wrap.sprite.move_to(fire,700,firey)
    print(b)

