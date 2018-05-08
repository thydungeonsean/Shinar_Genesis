

DESERT = 0
PLAINS = 1
FERTILE = 2
RIVER = 3


def moisture_to_tile(m):

    if m >= 5:
        return RIVER
    elif m >= 4:
        return FERTILE
    elif m >= 1:
        return PLAINS
    else:
        return DESERT
