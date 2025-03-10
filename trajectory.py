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
    if space:
        for i in a:
            wrap.sprite.remove(i["number"])
        a.clear()

@wrap.always(delay=1000)
def add_pacman():
    if space:

        x=wrap.sprite.get_x(point[0])
        y=wrap.sprite.get_y(point[0])

        x1 = wrap.sprite.get_x(point[1])
        y1 = wrap.sprite.get_y(point[1])
        pacman=wrap.sprite.add("pacman",x,y,"player2")
        slovar={"number":pacman,
                "speed":random.randint(5,10),
                "point_x":x1,
                "point_y":y1
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