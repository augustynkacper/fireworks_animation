
from function import get_roots, get_coefficients, get_velocity
from drawing import draw_parable, draw_start_end
from explosion import Explosion
import random
import math
import pygame


COLORS = [(0, 255, 41),(255, 0, 0),(255, 229, 0),(255, 123, 0),(176, 255, 0),(0, 252, 255),(252, 0, 255),(106, 0, 255),(30,200,255)]



class Firework:
    def __init__(self, size, start, end):
        self.W = size[0]
        self.H = size[1]
        self.start = start
        self.end = end
        self.abc = get_coefficients(self.H, self.start, self.end)
        self.root = get_roots(self.W, self.abc[0], self.abc[1], self.abc[2], self.start, self.end)
        self.x = self.root
        self.y = 0
        self.vel = get_velocity(self.W, self.root, self.end)
        self.color = COLORS[random.randint(0, len(COLORS)-1)]

    def move(self):
        a, b, c = get_coefficients(self.H, self.start, self.end)
        if self.start[0] < self.end[0]:
            self.x += self.vel
        else:
            self.x -= self.vel
        self.y = self.H -(a*self.x**2 + b*self.x + c)

    def draw(self, win):
        if self.start[0]<self.end[0] and self.x < self.end[0]:
            pygame.draw.circle(win, self.color,(self.x, self.y), 4)
        elif self.start[0] > self.end[0] and self.x > self.end[0]:
            pygame.draw.circle(win, self.color,(self.x, self.y), 4)

    def check(self):
        if self.start[0]<self.end[0] and self.x < self.end[0]:
            return True
        if self.start[0] > self.end[0] and self.x > self.end[0]:
            return True
        return False