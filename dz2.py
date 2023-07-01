import random
import wrap
a = random.randint(0,10)
b = wrap.world.create_world(700,500)
wrap.sprite.add("mario-enemies", random.randint(100,400),random.randint(100,400),"dragon_stand1")
wrap.sprite.add("mario-princess", random.randint(100,400),random.randint(100,400),"toad")
wrap.sprite.add("mario-enemies", random.randint(100,400),random.randint(100,400),"crab")