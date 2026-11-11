print("--- SCRIPT START ---", flush=True)

import random
import pygame
import particle


class AppMain:
    def __init__(self):
        pygame.init()
        width, height = 600, 400
        self.screen = pygame.display.set_mode((width, height))
        self.world = particle.World(width, height, dt=1.0, gy=0.5)
        self.particle_list = []

    def update(self):
        for p in self.particle_list:
            p.update()
        self.particle_list[:] = [p for p in self.particle_list if p.is_alive]

    def draw(self):
        self.screen.fill(pygame.Color("black"))
        for p in self.particle_list:
            p.draw(self.screen)
        pygame.display.update()

    def add_particle(self, pos, button):
        if button == 1:
            vx = random.uniform(-10, 10)
            vy = random.uniform(-10, 0)
            p = particle.Particle(pos, (vx, vy), self.world, postmove_strategy=particle.bounce_on_boundary)
            self.particle_list.append(p)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            frames_per_second = 60
            clock.tick(frames_per_second)

            sould_quit = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sould_quit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sould_quit = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.add_particle(event.pos, event.button)
            if sould_quit:
                break
            
            self.update()
            self.draw()
            
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    app = AppMain()
    app.run()

