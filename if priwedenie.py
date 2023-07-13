import random

import wrap
wrap.world.create_world(500,500)
pac=wrap.sprite.add("pacman", 250,250,"enemy_blue_down1")
a=random.randint(30,470)
b=random.randint(30,470)
wrap.sprite.add("pacman",a,b,"dot")

if b > 250:
    wrap.sprite.set_costume(pac, "enemy_blue_down1")
else:
    wrap.sprite.set_costume(pac, "enemy_blue_up1")

wrap.actions.move_to(pac,250,b)
if a <= 250:
    wrap.sprite.set_costume(pac, "enemy_blue_left1")
else:

    wrap.sprite.set_costume(pac, "enemy_blue_right1")

wrap.actions.move_to(pac,a,b)

