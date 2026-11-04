import pygame

def main():
    pygame.init()
    width, height = 600, 400
    screen = pygame.desplay.set_mode((width, height))
    clock = pygame.time.Clock()

    while True:
        frames_per_second = 60
        clocks.tick(frames_per_second)

        sould_quit = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sould_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sould_quit = True
        if sould_quit:
            break

        screen.fill(pygame.Color("black"))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

