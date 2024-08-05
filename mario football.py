import wrap

def day_pass(name):

    x=wrap.sprite.get_x(name)
    y=wrap.sprite.get_y(name)
    wrap.actions.move_to(ball,x,y, 900)

wrap.world.create_world(400, 600, 900, 50)
wrap.world.set_back_color(234, 100, 200)

ball=wrap.sprite.add("mario-enemies", 200, 300, "beetle_blue_go")
wrap.actions.set_size_percent(ball, 50, 50, 0)

mario1=wrap.sprite.add("mario-1-small", 100, 100, "stand")
mario2=wrap.sprite.add("mario-1-small", 200, 300, "stand")
mario3=wrap.sprite.add("mario-1-small", 300, 100, "stand")
mario4=wrap.sprite.add("mario-1-small", 100, 300, "stand")

day_pass(mario2)
day_pass(mario3)
day_pass(mario1)
day_pass(mario4)





