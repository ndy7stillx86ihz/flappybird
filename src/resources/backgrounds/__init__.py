from pygame.transform import scale

from  commons.assets_loader import AssetsLoader, ASSETS_DIR
from  commons.constants import BG_SIZE

BG_DIR = ASSETS_DIR.joinpath('images').joinpath('backgrounds')

backgrounds = [
    scale(AssetsLoader.load_image(bg), BG_SIZE)
    for bg in list(BG_DIR.iterdir())
]
