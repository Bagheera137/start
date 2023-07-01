import time

import wrap
wrap.world.create_world(500, 600)
wrap.world.set_back_color(123, 90, 100)
wrap.sprite.add("pacman", 100, 200, "enemy_blue_down1")
wrap.sprite.add("mario-princess", 300, 300, "toad")
time.sleep(3)
wrap.sprite.add_text("привет", 90, 180)
time.sleep(3)
wrap.sprite.add_text("пока", 300, 250)
wrap.actions.move_to(1, 500, 200)