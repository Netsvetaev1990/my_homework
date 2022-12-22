import pygame
pygame.init()

pygame.display.set_caption("Hello Pygame")
window = pygame.display.set_mode((600, 500))
FPS = 60 # число кадров в секунду
clock = pygame.time.Clock()
x = 600 // 2
y = 500 // 2
speed = 2
# flLeft = flRight = False
# pygame.draw.rect(window, (255, 0, 255), (20, 10, 100, 100), 5)
# pygame.draw.circle(window, (255, 0, 0), (200, 200), 100)
# pygame.draw.line(window, (0, 255, 0), (300, 250), (500, 450))
# pygame.display.update()
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
        if x <= 0:
           x = 0
    elif keys[pygame.K_RIGHT]:
        x += speed
        if x >= 550:
            x = 550
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    #     elif event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_LEFT:
    #             flLeft = True
    #         elif event.key == pygame.K_RIGHT:
    #             flRight = True
    #     elif event.type == pygame.KEYUP:
    #         if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
    #             flLeft = flRight = False
    # if flLeft:
    #     x -= speed
    # elif flRight:
    #     x += speed

    window.fill((0, 0, 255))
    pygame.draw.rect(window, (0, 255, 0), (x, y, 50, 60))
    pygame.display.update()

    clock.tick(FPS)