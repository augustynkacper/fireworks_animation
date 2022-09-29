import pygame
from function import get_roots, get_coefficients

pygame.init()


def draw_start_end(win, start, end):
    radius = 2
    pygame.draw.circle(win, (150,150,150), start, radius)
    pygame.draw.circle(win, (150,150,150), end, radius)



def draw_parable(W, H, win, start, end):
    delta = 2
    if start==None or end == None: return
    if start[0]==end[0] or start[1] == end[1]:
        return
     
    # coefficients of a function
    aa, bb, cc = get_coefficients(H, start,end)

    # if end is on the right side of start
    if start[0]<end[0]:
        last = (-1, cc)
        for x in range(0, end[0]+delta, delta):
            y = H - int(aa*x*x + bb*x + cc)
            pygame.draw.line(win, (100,100,100), last, (x,y), 2)
            last = (x,y)
    else:
        x = W+1
        last = (x, H - int(aa*x*x + bb*x + cc))
        for x in range(W+1, end[0]-delta, -delta):
            y = H - int(aa*x*x + bb*x + cc)
            pygame.draw.line(win, (100,100,100), last, (x,y), 2)
            last = (x,y)


