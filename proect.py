import wrap


width=600
height=500

wrap.world.create_world(width,height)

y=300
x1=300
x2=400

plat=wrap.sprite.add("mario-items",25,y,"moving_platform1")
wrap.sprite.move_left_to(plat,0)

plat=wrap.sprite.add("mario-items",25,y,"moving_platform1")
wrap.sprite.move_right_to(plat,width)

plat=wrap.sprite.add("mario-items",x1,y,"moving_platform1")
plat=wrap.sprite.add("mario-items",x2,y,"moving_platform1")
pac=wrap.sprite.add("pacman", 20,y-23,"enemy_blue_down1")
a=wrap.sprite.get_x(pac)
pol=(x1-a)/2
wrap.actions.move_to(pac,(x1-a)/2+a,y-23-pol)
wrap.actions.move_to(pac,x1,y-23)

wrap.actions.move_to(pac,(x2-x1)/2+x1,y-23-pol)
wrap.actions.move_to(pac,x2,y-23)