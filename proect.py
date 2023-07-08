import wrap


width=600
height=500

wrap.world.create_world(width,height)

y=500
x1=100
x2=200

plat1=wrap.sprite.add("mario-items",25,y,"moving_platform1")
wrap.sprite.move_left_to(plat1,0)

plat4=wrap.sprite.add("mario-items",25,y,"moving_platform1")
wrap.sprite.move_right_to(plat4,width)

plat2=wrap.sprite.add("mario-items",x1,y,"moving_platform1")
plat3=wrap.sprite.add("mario-items",x2,y,"moving_platform1")
pac=wrap.sprite.add("pacman", 20,y-23,"enemy_blue_down1")
a=wrap.sprite.get_x(pac)
pol=(x1-a)/2
wrap.actions.move_to(pac,(x1-a)/2+a,y-23-pol)
wrap.actions.move_to(pac,x1,y-23)
pol=(x2-x1)/2
wrap.actions.move_to(pac,(x2-x1)/2+x1,y-23-pol)
wrap.actions.move_to(pac,x2,y-23)
a=wrap.sprite.get_x(plat4)
pol=(a-x2)/2
wrap.actions.move_to(pac,(a-x2)/2+x2,y-23-pol)
wrap.actions.move_to(pac,a,y-23)
