import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
font = pygame.font.Font(None, 50)
text_image = font.render("hello, pygame", True, pygame.Color("yellow"))
player_image = pygame.image.load("../../assets/player/p1_walk01.png").convert()
    
while True:
    pygame.event.clear()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]:
        break

    pygame.draw.circle(screen, pygame.Color('red'), (300, 200), 30)

    mouse_pos = pygame.mouse.get_pos()

    screen.fill(pygame.Color('black'))

    screen.blit(player_image, mouse_pos)
    mouse_x, mouse_y = mouse_pos
    screen.blit(text_image, (mouse_x + 100, mouse_y))
    
    pygame.display.update()

pygame.quit()

