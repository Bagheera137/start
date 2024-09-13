import time

import wrap

wrap.world.create_world(400, 600, 900, 50)
wrap.world.set_back_color(100, 200, 200)
tank1 = wrap.sprite.add("battle_city_tanks", 200, 100, "tank_enemy_size1_green1",False)
tank2 = wrap.sprite.add("battle_city_tanks", 100, 400, "tank_enemy_size1_white1",False)
def appear(name):
    xt=wrap.sprite.get_x(name)
    yt=wrap.sprite.get_y(name)

    star=wrap.sprite.add("battle_city_items",xt,yt,"effect_appearance1")
    time.sleep(0.2)
    wrap.sprite.set_costume(star,"effect_appearance2")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance3")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance4")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance3")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance2")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance1")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance2")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance3")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance4")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance3")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance2")
    time.sleep(0.2)
    wrap.sprite.set_costume(star, "effect_appearance1")

    wrap.sprite.remove(star)
    wrap.sprite.show(name)


def move_left(name,dis):
    wrap.sprite.set_angle(name,270)
    wrap.actions.move_at_angle_dir(name,dis,1000)

def move_down(name,dis):
    wrap.sprite.set_angle(name,180)
    wrap.actions.move_at_angle_dir(name,dis,1000)

def move_right(name,dis):
    wrap.sprite.set_angle(name,90)
    wrap.actions.move_at_angle_dir(name,dis,1000)

def move_up(name,dis):
    wrap.sprite.set_angle(name,0)
    wrap.actions.move_at_angle_dir(name,dis,1000)

def vistrel(name,skolko_letit):
    at=wrap.sprite.get_top(name)
    ab = wrap.sprite.get_bottom(name)
    ar = wrap.sprite.get_right(name)
    al = wrap.sprite.get_left(name)
    b=wrap.sprite.get_angle(name)
    y=wrap.sprite.get_y(name)
    if b==90:
        bul=wrap.sprite.add("battle_city_items", ar, y, "bullet")
        wrap.actions.move_at_angle_point(bul,600,y,skolko_letit,1000)

    if b==-90:
        bul=wrap.sprite.add("battle_city_items", al, y, "bullet")
        wrap.actions.move_at_angle_point(bul, 0, y, skolko_letit, 500)

    if b==0:
        bul=wrap.sprite.add("battle_city_items", at, y, "bullet")
        wrap.actions.move_at_angle_point(bul, at, 0, skolko_letit, 500)

    if b==-180:
        bul=wrap.sprite.add("battle_city_items", ab, y, "bullet")
        wrap.actions.move_at_angle_point(bul, ab, 0, skolko_letit, 500)

appear(tank2)
appear(tank1)
move_down(tank1,80)
move_left(tank1,100)
vistrel(tank1,100)
move_up(tank2,30)
move_right(tank2,50)
vistrel(tank2,50)