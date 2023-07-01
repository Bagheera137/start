import random
import wrap

wrap.world.create_world(600,400)

dot = wrap.sprite.add("pacman", random.randint(0,600),random.randint(50,200),"dot")
player = wrap.sprite.add("pacman", random.randint(0,600), random.randint(210, 390), "player2")
a = wrap.sprite.get_x(dot)
b = wrap.sprite.get_y(dot)
wrap.actions.set_angle_to_point(player,a,b)
wrap.actions.move_to(player, a, b)
wrap.sprite.hide(dot)
wrap.actions.set_size(player,60,60)
print(a,b)