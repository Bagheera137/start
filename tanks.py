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

    if b==90:
        x = wrap.sprite.get_x(name)
        y = wrap.sprite.get_y(name)
        bul=wrap.sprite.add("battle_city_items", ar, y, "bullet")
        wrap.sprite.set_angle(bul,90)
        wrap.actions.move_at_angle_point(bul,600,y,skolko_letit,1000)
        wrap.sprite.hide(bul)

    if b==-90:
        x = wrap.sprite.get_x(name)
        y = wrap.sprite.get_y(name)
        bul=wrap.sprite.add("battle_city_items", al, y, "bullet")
        wrap.sprite.set_angle(bul, -90)
        wrap.actions.move_at_angle_point(bul, 0, y, skolko_letit, 500)
        wrap.sprite.hide(bul)

    if b==0:
        x = wrap.sprite.get_x(name)
        y = wrap.sprite.get_y(name)
        bul=wrap.sprite.add("battle_city_items", x, at, "bullet")
        wrap.sprite.set_angle(bul, 0)
        wrap.actions.move_at_angle_point(bul, x, 0, skolko_letit, 500)
        wrap.sprite.hide(bul)


    if b==180:
        x=wrap.sprite.get_x(name)
        y = wrap.sprite.get_y(name)
        bul=wrap.sprite.add("battle_city_items", x, ab, "bullet")
        wrap.sprite.set_angle(bul, 180)
        wrap.actions.move_at_angle_point(bul, x, 600, skolko_letit, 500)
        wrap.sprite.hide(bul)



def vzriv(kill):
    wrap.sprite.hide(kill)
    w=wrap.sprite.get_width(kill)
    h= wrap.sprite.get_height(kill)
    xt = wrap.sprite.get_x(kill)
    yt = wrap.sprite.get_y(kill)
    a=wrap.sprite.add("battle_city_items", xt, yt, "effect_explosion2")
    wrap.sprite.set_size(a,w+20,h+20)
    time.sleep(0.2)
    wrap.sprite.set_size(a, w + 20, h + 20)
    time.sleep(0.2)
    wrap.sprite.set_size(a, w + 20, h + 20)
    time.sleep(0.1)
    wrap.sprite.hide(a)



appear(tank2)
appear(tank1)
move_down(tank1,80)
vistrel(tank1,100)
move_right(tank1,100)
vistrel(tank1,100)
move_down(tank1,40)
vistrel(tank1,170)
move_right(tank1,50)
vistrel(tank1,50)
vzriv(tank1)
move_up(tank2,30)
move_left(tank2,50)
vistrel(tank2,50)
move_down(tank2,40)
vistrel(tank2,50)
vzriv(tank2)