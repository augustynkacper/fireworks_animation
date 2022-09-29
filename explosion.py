

import pygame
import math
import random

pygame.init()



W, H = 1000, 800

win = pygame.display.set_mode((W, H))

COLORS = [
(0, 255, 41),
(255, 0, 0),
(255, 229, 0),
(255, 123, 0),
(176, 255, 0),
(0, 252, 255),
(252, 0, 255),
(106, 0, 255),(30,200,255)]

class Explosion:
    def __init__(self, center, radius, segments, vel):
        self.center = center
        self.segments = segments
        self.radius = radius
        self.vel = vel
        self.r = 0
        self.alpha = 255
        self.colors = [COLORS[random.randint(0, len(COLORS)-1)] for _ in range(self.segments+3)]
        self.surf = pygame.Surface((W,H))

    

    def move(self):
        self.r += self.vel
        steps = self.radius//self.vel + 1
        self.alpha -= (self.alpha//steps + 1)

    def draw(self, win):
        
        d = 2*math.pi/self.segments

        
        self.surf.set_colorkey((0,0,0))
        self.surf.set_alpha(max(0, self.alpha) )
        self.surf.fill((0,0,0))
        angle = 0
        i = 0
        while angle < 2*math.pi:
            x,y = self.r*math.cos(angle), self.r*math.sin(angle)
            clr = self.colors[i]
            pygame.draw.circle(self.surf, clr, (x+self.center[0], y+self.center[1]), 3)

            i += 1
            angle += d

        win.blit(self.surf, (0,0))
    
    def check(self):
        if self.alpha > 0:
            return True
        return False


explosions = [Explosion((200,200), 100, 20, 2),Explosion((500,400), 200, 30, 2)]
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    win.fill((0,0,0))
    for expl in explosions:
        expl.move()
        expl.draw(win)
    explosions = [e for e in  explosions if e.check()]
    
    pygame.display.update()
