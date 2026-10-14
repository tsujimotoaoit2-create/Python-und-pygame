import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

while True:
    pygame.event.clear()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]:
        break
    pygame.draw.circle(screen, pygame.Color('red'), (300, 200), 30)
    pygame.display.update()

pygame.quit()

