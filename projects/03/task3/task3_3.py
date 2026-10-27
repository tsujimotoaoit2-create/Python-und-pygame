import pygame

def init_screen():
    pygame.init()
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    return screen

def create_text(text, color="green"):
    font_size = 50
    font_file = None
    antialias = True
    font = pygame.font.Font(font_file, font_size)
    text_image = font.render(text, antialias, pygame.Color(color))
    return text_image


def draw(screen, player_image, text_image, mouse_pos):
    screen.fill(pygame.Color("black"))
    screen.blit(player_image, mouse_pos)
    mouse_x, mouse_y = mouse_pos
    text_offset_x = 100
    screen.blit(text_image, (mouse_x + text_offset_x, mouse_y))
    pygame.display.update()


def main():
    screen = init_screen()
    text_image1 = create_text("Hello, World!")
    text_image2 = create_text("Nice to meet you!")

    player_images = create_player()

    while True:
        should_quit = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    should_quit = True
                elif event.key == pygame.K_b:
                    pass
        if should_quit:
            break
        mouse_pos = pygame.mouse.get_pos()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            draw(screen, player_image, text_image2, mouse_pos)
        else:
            draw(screen, player_image, text_image1, mouse_pos)
        
    pygame.quit()

if __name__ == "__main__":
    main()