import pygame
from pygame.locals import (
    K_w
)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Player, self).__init__()
        self.image = pygame.image.load("assets/stick.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)
        self.v_x = 0

    def update(self, keys, key_events):
        for event in key_events:
            if event.key == K_w:
                self.v_x -= 60
        self.v_x += 1
        move_x = 0
        move_y = self.v_x
        if keys[pygame.K_d]:
            move_x += 5
        if keys[pygame.K_a]:
            move_x -= 5
        if self.rect.bottom > 487:
            self.v_x = 0
            self.rect.bottom = 487
        self.rect.move_ip((move_x, move_y))
