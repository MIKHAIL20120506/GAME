import random


def take_damage(x):
    x+= 1
    x+= 15
    x -= 5
    if random.randint( 1, 2) == 1:
           x *=2
    print(x)


take_damage(9)
take_damage(15)
take_damage(7)
take_damage(7)