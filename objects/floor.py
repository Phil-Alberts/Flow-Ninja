import pygame
from pygame.math import Vector2
from objects.SpriteWithPhysics import SpriteWithPhysics
from objects.Physics import Physics

class Floor(SpriteWithPhysics):
    physics = Physics(Vector2(0, 0), Vector2(0, 0), Vector2(0, 0), gravity_impact=0)
    collision = True
    def __init__(self, rect: pygame.rect.Rect):
        super(Floor, self).__init__()
        self.image = pygame.Surface((rect.width, rect.height))
        self.image.fill((50, 50, 50))
        self.rect = rect
