from time import time

from  core.game.settings import DIFFICULTY_LEVELS
from  entities.sprites.abstracts import CommonSprite, CollidableSprite, MovingSprite, SolidSprite
from  resources.spritesheets import pipe_spritesheet


class Pipe(SolidSprite,
           MovingSprite,
           CollidableSprite,
           CommonSprite):
    def __init__(self, x, y, color, upside_down: bool = False, speed=DIFFICULTY_LEVELS['medium']['speed']):
        image = pipe_spritesheet[color]

        MovingSprite.__init__(self, vx=-speed)

        if upside_down:
            CommonSprite.__init__(self, image, x, y, midbottom=(x, y))
        else:
            CommonSprite.__init__(self, image, x, y, midtop=(x, y))

        self.spawn_time = time()
        self.is_mirror = upside_down

    def constraints(self):
        if self.rect.right < 0:
            self.kill()

    def update(self, delta):
        self.move_x(delta)

        self.constraints()
