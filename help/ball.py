from random import randint
from pygame.draw import *
from settings import *

def new_ball():
    '''рисует новый шарик '''
    x = randint(100, WIDTH - 100)
    y = randint(100, HEIGHT - 100)
    r = randint(10, 100)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]
    return x, y, r, color, vx, vy

def draw_ball(b, screen):
    x, y, r, color, vx, vy = b
    circle(screen, color, (x, y), r)

def move_ball(b):
    x, y, r, color, vx, vy = b
    if x < r or x > 1400 - r:
        vx = -vx
    if y < r or y > 900 - r:
        vy = -vy
    return x + vx, y + vy, r, color, vx, vy
