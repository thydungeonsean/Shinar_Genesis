from random import randint

desert = (248, 206, 120)
plains = (201, 111, 10)
fertile = (117, 134, 23)
river = (0, 240, 210)
farm = (50, 250, 100)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HIGHLIGHT = (200, 200, 0)


def fluctuate_river():

    return randint(0, 100), randint(160, 220), randint(170, 200)
