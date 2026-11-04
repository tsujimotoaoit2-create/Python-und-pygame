import random
import pygame

class World:
    def __init__(self, width, height, dt, gy):
        self.width = width
        self.height = height
        self.gy = gy
        self.dt = dt

class Particle:
    def __init__(self, pos, vel, World, color = (0, 128, 0), radius = 10.0):
        self.is_alive = True
        self.x, self.y = pos
        self.vx, self.vy = vel
        self.World = World
        self.radius = radius
        self.color = color

    def update(self):
        self.vy += self.World.gy*self.World.dt
        self.x += self.vx*self.World.dt
        self.y += self.vy*self.World.dt
        if self.x < 0 or self.x > self.World.width or self.y > self.World.height:
            self.is_alive = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class AppMain:
    def __init__(self):
        pygame.init()
        width, height = 600, 400
        self.screen = pygame.display.set_mode((width, height))
        self.world = World(width, height, dt=1.0, gy=0.5)
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
            color = tuple(random.randint(0, 255) for _ in range(3))
            radius = random.uniform(1.0, 20.0)
            p = Particle(pos, (vx, vy), self.world, color, radius)
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
