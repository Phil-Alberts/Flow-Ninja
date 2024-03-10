import pygame
from objects.PhysicsObject import PhysicsObject
from pygame.math import Vector2
from pygame.locals import (
    K_w
)

class Player(pygame.sprite.Sprite):
    physics: PhysicsObject

    def __init__(self, pos: Vector2):
        super(Player, self).__init__()

        # visual
        self.image = pygame.image.load("assets/stick.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        # physics and display
        self.physics = PhysicsObject(pos)
        self.rect = self.image.get_rect()
        self.rect.move_ip(*self.physics.pos)

    def update(self, dt: float, keys, key_events):
        forces: list[Vector2] = []
        forces.append(Vector2(0, 1000))
        pos, vel, acc = self.physics.update(dt, forces)
        print(pos.x, pos.y)
        self.rect.move_ip(pos.x, pos.y)
