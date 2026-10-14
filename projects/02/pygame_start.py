import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
image = pygame.image.load("../../assets/player/p1_walk01.png").convert()

while True:
    pygame.event.clear()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]:
        break

    pygame.draw.circle(screen, pygame.Color('red'), (300, 200), 30)

    screen.fill(pygame.Color('black'))
    screen.blit(image, pygame.mouse.get_pos())
    pygame.display.update()

pygame.quit()

