import random

import wrap
wrap.world.create_world(500,500)
a=[]
point=[]

click=False
space=False
@wrap.on_key_down(wrap.K_SPACE)
def move_sprite():
    global space
    space=not space
@wrap.always()
    while space==True:
        pacman=wrap.sprite.add("pacman",100,200,"player2")
        slovar={"number":pacman,
                "speed":random.randint(5,10),
                "point_x":random.randint(100,400),
                "point_y":random.randint(100,400)
                }
    a.append(slovar)

print(a)
@wrap.always()
def move():
    for i in a:
        wrap.sprite.move_at_angle_point(i["number"],i["point_x"],i["point_y"],i["speed"])

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def mouse_move():
    global click
    click=not click
    if click:
        for i in range(len(point)):
            wrap.sprite.remove(point[0])
            del point[0]

@wrap.on_mouse_move()
def make_point(pos_x,pos_y):
    if click:
        dot=wrap.sprite.add("pacman", pos_x, pos_y, "dot")
        point.append(dot)