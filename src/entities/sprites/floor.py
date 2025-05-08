from random import choice

from  commons.constants import FLOOR_Y
from  core.game.settings import DIFFICULTY_LEVELS
from  entities.sprites.abstracts import MovingSprite
from  entities.sprites.abstracts import SolidSprite, CollidableSprite, CommonSprite
from  resources.spritesheets import floor_spritesheet


class Floor(SolidSprite,
            MovingSprite,
            CollidableSprite,
            CommonSprite):
    def __init__(self, x=0, y=FLOOR_Y, speed=DIFFICULTY_LEVELS['medium']['speed']):
        image = floor_spritesheet[choice(list(floor_spritesheet.keys()))]

        MovingSprite.__init__(self, vx=-speed)
        CommonSprite.__init__(self, image, x, y, topleft=(x, y))

    def constraints(self):
        if self.rect.right < 0:
            self.kill()

    def update(self, delta):
        self.move_x(delta)

        self.constraints()
