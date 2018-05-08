from random import randint

desert = (190, 200, 50)
plains = (140, 75, 60)
fertile = (10, 180, 90)
river = (0, 210, 240)


def fluctuate_river():

    return randint(0, 100), randint(160, 210), randint(190, 255)
