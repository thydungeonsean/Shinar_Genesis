from random import randint

desert = (220, 210, 50)
plains = (140, 75, 60)
fertile = (10, 180, 90)
river = (0, 210, 240)
farm = (50, 250, 100)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HIGHLIGHT = (200, 200, 0)


def fluctuate_river():

    return randint(0, 100), randint(160, 210), randint(190, 255)
