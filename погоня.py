import time
from wrap import world, sprite, sprite_text, actions


def pobeg(ugol, ras,text):
    addtext(text,victim)
    actions.set_size_percent(victim, 30, 30, 500)
    actions.set_angle(victim, ugol, 500)
    actions.move_at_angle_dir(victim, ras, 600)
    actions.set_size_percent(victim, 100, 100, 500)


def pogonya(ras2, text):
    addtext(text,hunter)
    actions.move_at_angle_point(hunter, sprite.get_x(victim), sprite.get_y(victim), ras2, 500)

def addtext(text2,anim):
    text = sprite.add_text(text2, sprite.get_x(anim), sprite.get_top(anim) - 20)
    time.sleep(0.5)
    sprite.remove(text)



world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

victim = sprite.add("pacman", 300, 100, "player2")
hunter = sprite.add("pacman", 100, 100, "enemy_blue_right1")


pobeg(240, 50,"не догонишь")
# pobeg(150, 150, "не догонишь")
pogonya(56,"стой")
# pogonya(94, "не убежишь")
# pobeg(90, 100, "пока пока")
# pogonya(200, "стой!")
