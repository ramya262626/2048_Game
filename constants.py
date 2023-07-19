#module which has all the colors used in the game
#colors are declared with their rgb values

BLACK = (64, 64, 64)
RED = (225, 184, 148)
GREEN = (177, 197, 195 )
PURPLE = (210, 145, 188)
DEEP_PURPLE = (149, 125, 173)
DEEP_ORANGE = (135, 92, 54)
ORANGE = (255,152,0)
BROWN = (121,85,72)
L_GREEN = (139,195,74)
TEAL = (0,150,136)
BLUE  = (33,150,136)
PINK = (234,30,99)


color_dict = {
    0:BLACK,
    2:RED,
    4:GREEN,
    8:PURPLE,
    16:DEEP_PURPLE,
    32:DEEP_ORANGE,
    64:TEAL,
    128:L_GREEN,
    256:PINK,
    512:ORANGE,
    1024:BLACK,
    2048:BROWN
}

def getColor(i):
    return color_dict[i]