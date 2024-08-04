import wrap

def car(x1,y1,x2,y2,x3,y3):

    mario1=wrap.sprite.add("mario-1-small", x1, y1, "stand")
    mario2=wrap.sprite.add("mario-1-small", x2, y2, "stand")
    mario3=wrap.sprite.add("mario-1-small", x3, y3, "stand")

    ball=wrap.sprite.add("mario-enemies", x2, y2, "beetle_blue_go")
    wrap.actions.set_size_percent(ball, 50, 50, 0)
    wrap.actions.move_to(ball, x1, y1, 900)
    wrap.actions.move_to(ball, x3, y3, 900)
    wrap.actions.move_to(ball, x1, y1, 900)
    wrap.actions.move_to(ball, x2, y2, 900)
    wrap.actions.move_to(ball, x3, y3, 900)


wrap.world.create_world(400, 600, 900, 50)
wrap.world.set_back_color(234, 100, 200)

car(100,100,200,300,300,100)



