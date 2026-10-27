import pygame

def init_screen():
    pygame.init()
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    return screen

def create_text(Phrase, Color):
    font_size = 50
    font_file = None
    antialias = True
    font = pygame.font.Font(font_file, font_size)
    text_image = font.render(Phrase, antialias, pygame.Color(Color))
    return text_image

def create_player():
    file_path = "../../assets/player/p1_walk{:02}.png"
    player_images = []
    for i in range(4,8):
        player_images.append(pygame.image.load(file_path.format(i)).convert())
    return player_images



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
    Phrases = {
        "hello, pygame": "green", 
        "You clicked the mouse button!": "blue", 
        "Let`s make a game!": "white",
        "How are you?": "red"}
    #クリックすると順番に言葉が表示される(辞書型を使って、言葉と色をセットで管理する)
    player_images = create_player()
    clock = pygame.time.Clock()
    frame_index = 0

    clicked_index = 0

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

        buttons_pressed = pygame.mouse.get_pressed()
        if buttons_pressed[0]:
            clicked_index += 1
        text_period = 6
        text_index = (clicked_index//text_period) % len(Phrases)
        text_image_shown = create_text(list(Phrases.keys())[text_index], list(Phrases.values())[text_index])       
        #animationの方と同様にマウスをクリックするごとにclicked_indexが増える、それによって表示する言葉が変わる。text_periodを設定することで、クリックしてから次の言葉に変わるまでの間隔を調整できる。
        frame_index +=1
        animation_period = 6
        animation_index = (frame_index // animation_period) % len(player_images)
        #animation_index = frame_index % len(player_images) clock制限がないバージョンで使う

        draw(screen, player_images[animation_index], text_image_shown, mouse_pos)

if __name__ == "__main__":
    main()