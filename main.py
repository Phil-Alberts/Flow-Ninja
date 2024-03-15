import pygame
from vector import Vector
from objects import Player, Floor
pygame.init()

FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_INIT_POS = (30, 0)
GROUND_Y = 480

clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen.fill((255, 255, 255))
character = Player(CHARACTER_INIT_POS)
floor = Floor(pygame.rect.Rect((0, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT)))
all_sprites = pygame.sprite.Group()
all_sprites.add(character)
all_sprites.add(floor)

running = True
while running:

    key_events = []
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key_events.append(event)
    screen.fill((255, 255, 255))

    character.update(1/60, pygame.key.get_pressed(), key_events)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)