import random

import wrap
wrap.world.create_world(500,500)
a=[]
y=50
click=False
for i in range(random.randint(3,8)):
    pacman=wrap.sprite.add("pacman",50,y,"player2")
    slovar={"number":pacman,
            "speed":random.randint(5,10),
            "point_x":random.randint(100,400),
            "point_y":random.randint(100,400)
            }
    a.append(slovar)
    y = y + 70
print(a)
@wrap.always()
def move():
    for i in a:
        wrap.sprite.move_at_angle_point(i["number"],i["point_x"],i["point_y"],i["speed"])

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def mouse_move():
    global click
    click=not click

@wrap.on_mouse_move()
def make_point(pos_x,pos_y):
    if click:
        wrap.sprite.add("pacman", pos_x, pos_y, "dot")