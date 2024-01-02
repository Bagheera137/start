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
    b=0
    for c in range(len(a)):
        b=b+1
        if b==3:
            wrap.sprite.move(a[c], 0, 22)
            b=0
        else:
            wrap.sprite.move(a[c], 0, 10)

