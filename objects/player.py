import pygame
from objects.Physics import Physics
from objects.SpriteWithPhysics import SpriteWithPhysics
from objects.ExtendedRectangle import ExtendedRectangle
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
        self.rect = ExtendedRectangle(self.image.get_rect())
        self.rect.move_ip(*self.physics.pos)

    def update(self, events):
        for event in events:
            if event['type'] == 'collision' and self in event['actors']:
                # do collision things
                # self.physics.set_to_previous()
                # identify the object we collided with
                [other] = [actor for actor in event['actors'] if actor is not self]



                # assume the object is a rectangle, calculate next vel
                print("we're colliding!", other)

        self.rect.center = self.physics.pos
