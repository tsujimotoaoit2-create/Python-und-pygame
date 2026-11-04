import pygame

class World:
    def __init__(self, width, height, dt, gy):
        self.width = width
        self.height = height
        self.gy = gy
        self.dt = dt

class Particle:
    def __init__(self, past_pos, now_pos, World):
        self.is_alive = True
        self.past_x, self.past_y = past_pos
        self.now_x, self.now_y = now_pos
        self.x, self.y = now_pos
        self.World = World

    def vel(self):
        self.vx = (self.now_x - self.past_x) / 10
        self.vy = (self.now_y - self.past_y) / 10
    
    def update(self):
        self.vy += self.World.gy * self.World.dt
        self.x += self.vx * self.World.dt
        self.y += self.vy * self.World.dt
        if self.x < 0 or self.x > self.World.width or self.y > self.World.height:
            self.is_alive = False

    def draw(self, screen):
        radius = 10
        pygame.draw.circle(screen, pygame.Color("green"), (self.x, self.y), radius)

class AppMain:
    def __init__(self):
        pygame.init()
        width, height = 600, 400
        self.screen = pygame.display.set_mode((width, height))
        self.world = World(width, height, dt=1.0, gy=0.5)
        self.particle_list = []
        self.mouse_down_pos = None

    def update(self):
        for p in self.particle_list:
            p.update()
        self.particle_list[:] = [p for p in self.particle_list if p.is_alive]

    def draw(self):
        self.screen.fill(pygame.Color("black"))
        for p in self.particle_list:
            p.draw(self.screen)
        pygame.display.update()

    def add_particle(self, past_pos, now_pos):
        p = Particle(past_pos, now_pos, self.world)
        p.vel()
        self.particle_list.append(p)

    def run(self):
        clock = pygame.time.Clock()

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
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_down_pos = event.pos
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and self.mouse_down_pos is not None:
                        mouse_up_pos = event.pos
                        self.add_particle(self.mouse_down_pos, mouse_up_pos)
                        self.mouse_down_pos = None
            if should_quit:
                break
            
            self.update()
            self.draw()

        pygame.quit()

if __name__ == "__main__":
    app = AppMain()
    app.run()
