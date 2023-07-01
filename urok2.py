import wrap
width = 800
height = 600
x1 = 234
y1 = 99
x2 = 356
y2 = 213
x3 = 100
y3 = 362
wrap.world.create_world(width, height)

wrap.sprite.add("pacman", width/2,height/2, "player2")

wrap.sprite.add("pacman", x1, y1, "dot")
wrap.sprite.add_text("точка1", x1, y1- 20, text_color= [234,12,123])

wrap.sprite.add("pacman", x2, y2, "dot")
wrap.sprite.add_text("точка2", x2, y2- 20, text_color= [234,12,123])

wrap.sprite.add("pacman", x3, y3, "dot")
wrap.sprite.add_text("точка3", x3, y3- 20, text_color= [234,12,123])


wrap.sprite.add("pacman", 20,20, "enemy_blue_down1")
wrap.sprite.add("pacman", width - 20,height - 20, "enemy_blue_down1")
wrap.sprite.add("pacman", 20,height - 20, "enemy_blue_down1")
wrap.sprite.add("pacman",width - 20 ,20, "enemy_blue_down1")

wrap.sprite.add("mario-enemies", 30, height/2, "dragon_stand1")
wrap.sprite.add("mario-enemies",width - 30,height/2 , "crab")
wrap.sprite.add("mario-princess", width/2, 30, "toad")
wrap.sprite.add("mario-princess", width/2, height-30, "toad")

wrap.actions.move_to(0, width/2,y1 )
wrap.actions.move_to(0, x1, y1)

wrap.actions.move_to(0, x1, y2)
wrap.actions.move_to(0, x2, y2)

wrap.actions.move_to(0, x2, y3)
wrap.actions.move_to(0, x3, y3)
