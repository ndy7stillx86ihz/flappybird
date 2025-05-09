import pygame as pg

from  core.game.settings import SCREEN_HEIGHT, BASE_DIR

DEFAULT_SPRITE_SIZE: tuple[int, int] = (SCREEN_HEIGHT // 15, SCREEN_HEIGHT // 15)

FONTS_DIR = BASE_DIR.parent.joinpath('assets', 'fonts')  # ../assets/fonts

pg.font.init()

GRAVITY_FORCE = SCREEN_HEIGHT * 0.98
JUMP_FORCE = SCREEN_HEIGHT * 0.3

FONT_FILENAME = 'FlappyBirdRegular-9Pq0.ttf'
DEFAULT_FONT_SIZE = 20
DEFAULT_FONT_STYLE = pg.font.Font(FONTS_DIR.joinpath(FONT_FILENAME), DEFAULT_FONT_SIZE)

COLORS = {
    "blue": (32, 41, 135),
    "sky_blue": (64, 188, 216),
    "black": (18, 22, 25),
    "less_black": (24, 25, 29),
    "jasmine": (244, 213, 141),
    "green": (0, 128, 0),
    "pink": (147, 47, 109),
    "gray": (154, 160, 168),
    "red": (135, 27, 27),
    "white": (255, 255, 255),
    "honeydew": (225, 239, 230),
    "gold": (255, 215, 0),
}

BASE_COLOR = COLORS['black']

DEFAULT_TITLE_FONT_SIZE = 150
DEFAULT_TITLE_FONT_COLOR = 'white'
DEFAULT_OPTION_FONT_SIZE = 80
DEFAULT_OPTION_FONT_COLOR = 'honeydew'
DEFAULT_HOVER_OPTION_FONT_SIZE = DEFAULT_OPTION_FONT_SIZE + DEFAULT_OPTION_FONT_SIZE // 10
DEFAULT_HOVER_OPTION_FONT_COLOR = 'white'
DEFAULT_OPTIONS_OFFSET = 60
DEFAULT_OUTLINE_WIDTH = 2
DEFAULT_SHADOW_WIDTH = 3
DEFAULT_OUTLINE_COLOR = (0, 0, 0)

BG_SPEED = -50
DEFAULT_BG_ALPHA = 220
DEFAULT_BG_LAYER = 0

BG_SIZE = (SCREEN_HEIGHT * 1.2, SCREEN_HEIGHT)
BIRD_SIZE = (SCREEN_HEIGHT // 14, SCREEN_HEIGHT // 14)
PIPES_SIZE = (SCREEN_HEIGHT // 6, SCREEN_HEIGHT * 2.5)
FLOOR_SIZE = (SCREEN_HEIGHT // 4, SCREEN_HEIGHT // 14)

FLOOR_WIDTH, FLOOR_HEIGHT = FLOOR_SIZE
FLOOR_Y = SCREEN_HEIGHT - FLOOR_HEIGHT

INGAME_DEADZONE = (SCREEN_HEIGHT // 5,
                   FLOOR_Y - SCREEN_HEIGHT // 5)
MONITOR_SIZE = pg.display.get_desktop_sizes()[0]
