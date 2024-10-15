from random import randint
from pygame.draw import *
from settings import *

def new_polygon():
    '''рисуем треугольник'''
    x1 = randint(50, 1000)
    x2 = x1 + randint(20, 50)
    x3 = x2 + randint(50, 100)
    y1 = randint(100, 900)
    y2 = y1 + randint(0, 100)
    y3 = y2 + randint(-100, 0)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)] 
    return x1, x2, x3, y1, y2, y3, vx, vy, color


def draw_polygon(p, screen):
    x1, x2, x3, y1, y2, y3, vx, vy, color = p
    polygon(screen, color, ((x1,y1), (x2,y2), (x3, y3)))



def move_poly(p):
    x1, x2, x3, y1, y2, y3, vx, vy, color = p
    if (x1 < 0 or x1 > 1400) or (x2 < 0 or x2 > 1400) or (x3 < 0 or x3 >1400):
        vx = -vx
    if (y1 < 0 or y1 > 900) or (y2 < 0 or y2 > 900) or (y3 < 0 or y3 > 900):
        vy = -vy
    return x1 + vx, x2 + vx, x3 + vx, y1 + vy, y2 + vy, y3 + vy, vx, vy, color 