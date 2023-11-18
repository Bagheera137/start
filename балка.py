import wrap

wrap.world.create_world(500,600)

plat=wrap.sprite.add("mario-items", 250, 300, "moving_platform2")
wrap.sprite.set_angle(plat, 180)
a=-10
while True:
    wrap.sprite.move(plat, 0, a)

    get = wrap.sprite.get_top(plat)
    bot = wrap.sprite.get_bottom(plat)
    if get <= 0:
        a=10
    if bot >= 600:
        a=-10
