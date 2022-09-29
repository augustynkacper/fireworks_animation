from function import get_roots, get_coefficients, get_velocity
from drawing import draw_parable, draw_start_end
from explosion import Explosion
import random
import math
import pygame
from firework import Firework



W, H = 1000, 800
pygame.init()
win = pygame.display.set_mode((W, H))

  

def draw(W, H, win, start, end, fireworks, explosions):
    win.fill((0,0,0))

    if start!=None and end!= None: 
        draw_parable(W, H, win, start, end)
        draw_start_end(win, start, end)

    for frwrk in fireworks:
        frwrk.draw(win)

    for expl in explosions:
        expl.draw(win)
    
    pygame.display.update()



def fireworks():
    clock = pygame.time.Clock()
    run = True

    mouse_pressed = False
    start,end = None, None

    fireworks_list = []
    explosions = []

    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        # GETTING START AND END POINT

        if pygame.mouse.get_pressed()[0]:
            if not mouse_pressed:
                start = pygame.mouse.get_pos()
                mouse_pressed = True
            else:
                pos = pygame.mouse.get_pos()

                if pos[1] >= start[1]:
                    end = (pos[0], start[1]-1)
                elif pos[0]!=start[0]:
                    end = pygame.mouse.get_pos()
        else:
            mouse_pressed = False
            if start!=None and end!=None:
                fireworks_list.append(Firework((W,H),start, end))
            start, end =  None, None


        for frwrk in fireworks_list:
            frwrk.move()

            if not frwrk.check():
                explosions.append(Explosion(frwrk.end, random.randint(50,400), random.randint(10,35), 2))


        for expl in explosions:
            expl.move()

        fireworks_list = [f for f in fireworks_list if f.check()]

        draw(W, H, win, start, end, fireworks_list, explosions)

        clock.tick(60)



fireworks()

        
    