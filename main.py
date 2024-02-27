import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen.fill((255, 255, 255))
character = pygame.image.load("stick.png")
character_rect = character.get_rect()

# circle_d = 79
# circle_x = 80.25
# circle_direction = 1
# circle_size_direction = 1

x = 30
jump_speed = 0
y = 330
gravity = 1

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    #Jumpting test
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x+=5
    if keys[pygame.K_a]:
        x-=5
    if keys[pygame.K_w] and y == 330:
        jump_speed = -15
    y += jump_speed
    jump_speed += gravity
    if y > 330:
        y = 330
        jump_speed = 0
    # character_rect.move(x, y)
    screen.blit(character, (x, y))
    # pygame.draw.circle(screen, (0, 0, 0), (x, y), 10)

    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     x, y = pygame.mouse.get_pos()
    #     pygame.draw.circle(screen, (255, 0, 0),(x, y), circle_d)
    #     # circle_d = circle_d - 1

    pygame.draw.line(screen, (50, 50, 50), (0, 550), (800, 550), 100)

    # circle stuff
   
    # pygame.draw.circle(screen, (0, 0, 255),(circle_x, 300), circle_d)
    # if circle_d + circle_x >= SCREEN_WIDTH or circle_x - circle_d <= 0:
    #     circle_direction = circle_direction * -1
    # circle_x = circle_x + 0.25 * circle_direction
    # if circle_d >= 80 or circle_d <= 20:
    #     circle_size_direction = circle_size_direction * -1
    # circle_d = circle_d - 0.05 * circle_size_direction





    pygame.display.flip()
    clock.tick(60)