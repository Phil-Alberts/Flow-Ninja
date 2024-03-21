import pygame
from objects.Physics import Physics
from objects.SpriteWithPhysics import SpriteWithPhysics
from pygame.math import Vector2
from pygame.locals import (
    K_w
)

class Player(SpriteWithPhysics):
    collision = True

    def __init__(self, pos: Vector2):
        super(Player, self).__init__()

        # visual
        self.image = pygame.image.load("assets/stick.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        # physics and display
        self.physics = Physics(pos)
        self.rect = self.image.get_rect()
        self.rect.move_ip(*self.physics.pos)

    def update(self, events):
        for event in events:
            print(event)
            # if event['type'] == 'collision' and self in event['actors']:
            #     # do collision things
            #     print("we're colliding!")
        self.rect.center = self.physics.pos
