import pygame

class Floor(pygame.sprite.Sprite):
    def __init__(self, rect: pygame.rect.Rect):
        super(Floor, self).__init__()
        self.image = pygame.Surface((rect.width, rect.height))
        self.image.fill((50, 50, 50))
        self.rect = rect
