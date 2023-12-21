import random

import wrap

wrap.world.create_world(600,600)

for i in range(random.randint(5,10)):
    wrap.sprite.add("mario-enemies", 300, 300, "crab")


a=[]
for b in range(10,590,20):
    print(b)
    fireball = wrap.sprite.add("mario-enemies", b, 10, "fire_ball")
    a.append(fireball)
print(a)


while True:
    for c in range(len(a)):

        if c==5:
            wrap.sprite.move(a[5], 0, 22)
        else:
            wrap.sprite.move(a[c], 0, 10)

