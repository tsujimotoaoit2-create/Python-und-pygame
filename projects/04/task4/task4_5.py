import pygame
import math

def init_screen():
    pygame.init()
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    return screen

def create_text():
    font_size = 50
    font_file = None
    antialias = True
    font = pygame.font.Font(font_file, font_size)
    text_image = font.render("hello, pygame", antialias, pygame.Color("green"))
    return text_image

def create_player():
    file_path = "../../assets/player/p1_walk{:02}.png"
    player_images = []
    for i in range(4,8):
        player_images.append(pygame.image.load(file_path.format(i)).convert())
    return player_images

def distance(coordination_change):
    x_change, y_change = coordination_change
    return math.sqrt(x_change**2 + y_change**2)

def draw(screen, player_image, text_image, mouse_pos):
    screen.fill(pygame.Color("black"))
    screen.blit(player_image, mouse_pos)
    if text_image is not None:
        mouse_x, mouse_y = mouse_pos
        text_offset_x = 100
        screen.blit(text_image, (mouse_x + text_offset_x, mouse_y))
    pygame.display.update()

def main():
    screen = init_screen()
    text_image = create_text()
    player_images = create_player()
    clock = pygame.time.Clock()
    total_distance = 0

    while True:
        frames_per_second = 60
        clock.tick(frames_per_second)

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

        mouse_rel = pygame.mouse.get_rel()

        buttons_pressed = pygame.mouse.get_pressed()
        if buttons_pressed[0]:
            text_image_shown = text_image
        else:
            text_image_shown = None
        
        if mouse_rel == (0, 0):
            animation_index = 0
        else:
            total_distance += distance(mouse_rel)
            animation_index = int(total_distance / 20) % len(player_images)

        draw(screen, player_images[animation_index], text_image_shown, mouse_pos)

if __name__ == "__main__":
    main()