import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
font = pygame.font.Font(None, 50)
text_image = font.render("hello, pygame", True, pygame.Color("green"))
player_image = pygame.image.load("../../assets/player/p1_walk01.png").convert()
    
while True:
    pygame.event.clear()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]:
        break

    pygame.draw.circle(screen, pygame.Color('red'), (300, 200), 30)

    mouse_pos = pygame.mouse.get_pos()

    screen.fill(pygame.Color('black'))
    
    mouse_x, mouse_y = mouse_pos
    width, height = player_image.get_width(), player_image.get_height()

    mouse_x1 = mouse_x - width // 2
    mouse_y1 = mouse_y - height // 2

    screen.blit(player_image, (mouse_x1, mouse_y1))
    screen.blit(text_image, (mouse_x1 + 100, mouse_y1))

    pygame.display.update()

pygame.quit()