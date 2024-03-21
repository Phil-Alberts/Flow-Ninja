import pygame
import util.args as args
from objects import Player, Floor
from objects.PhysicsEngine import PhysicsEngine

pygame.init()

FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_INIT_POS = pygame.math.Vector2(50, 400)
GROUND_Y = 800

clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen.fill((255, 255, 255))
engine = PhysicsEngine()
character = Player(CHARACTER_INIT_POS)
floor = Floor(pygame.rect.Rect((SCREEN_WIDTH / 2, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT)))
all_sprites = pygame.sprite.Group()
all_sprites.add(character)
all_sprites.add(floor)

engine.register_object(character)
engine.register_object(floor)

running = True
frame_advance = False
while running:

    key_events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key_events.append(event)
            if args.debug and event.key == pygame.K_n:  # Check for 'n' key in debug mode
                frame_advance = True
                
    if not args.debug or frame_advance:  # Only update if not in debug mode or if 'n' is pressed
        screen.fill((255, 255, 255))
        engine.update_entities(1/60, pygame.key.get_pressed(), key_events)
        all_sprites.draw(screen)
        pygame.display.flip()
        frame_advance = False

    clock.tick(FPS)