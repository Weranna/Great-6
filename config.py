WIN_WIDTH = 1280
WIN_HEIGHT = 720
TILESIZE = 32
FPS = 60

PLAYER_SPEED = 3
ENEMY_SPEED = 2

PLAYER_LAYER = 5
ENEMY_LAYER = 4
TERRAIN_LAYER = 3
GRASS_LAYER = 2
GROUND_LAYER = 1

RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B.....S............B',
    'B.....S...E.....E..B',
    'B.....S............B',
    'B.....S............B',
    'B..............SSSSB',
    'B..................B',
    'B........P.........B',
    'B..............SSSSB',
    'B..................B',
    'BSSSSSSSSSS........B',
    'B...S..............B',
    'B.........E........B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB',
]

DEFAULT_IMAGE_SIZE = (TILESIZE, TILESIZE)