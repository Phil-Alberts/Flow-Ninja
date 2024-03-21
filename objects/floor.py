import pygame
from pygame.math import Vector2
from objects.SpriteWithPhysics import SpriteWithPhysics
from objects.Physics import Physics
from objects.ExtendedRectangle import ExtendedRectangle

class Floor(SpriteWithPhysics):
    collision = True
    def __init__(self, rect: pygame.rect.Rect):
        super(Floor, self).__init__()
        self.physics = Physics(Vector2(rect.x, rect.y), Vector2(0, 0), Vector2(0, 0), gravity_impact=0)
        self.image = pygame.Surface((rect.width, rect.height))
        self.image.fill((50, 50, 50))
        self.rect = ExtendedRectangle(rect)
