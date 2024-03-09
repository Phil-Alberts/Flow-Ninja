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

x, y = CHARACTER_INIT_POS
jump_speed = 0
gravity = 1

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

    #Jumpting test
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x+=5
    if keys[pygame.K_a]:
        x-=5
    if keys[pygame.K_w] and y == GROUND_Y:
        jump_speed = -15
    y += jump_speed
    jump_speed += gravity
    if y > GROUND_Y:
        y = GROUND_Y
        jump_speed = 0

    character.update(pygame.key.get_pressed(), key_events)
    all_sprites.draw(screen)
    # screen.blit(character.surf, (x, y))
    # screen.blit(floor.surf, floor.rect)
    # pygame.draw.rect(screen, (50, 50, 50), (0, GROUND_Y + character.surf.get_height() - 7, SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)