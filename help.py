import pygame
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont("Times New Roman", 30)


FPS = 30
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_polygon():
    '''рисуем треугольник'''
    x1 = randint(100, 1000)
    x2 = x1 + randint(-100, 100)
    x3 = x2 + randint(-100, 100)
    y1 = randint(100, 900)
    y2 = y1 + randint(-100,100)
    y3 = y2 + randint(-100, 100)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)] 
    return x1, x2, x3, y1, y2, y3, vx, vy, color


def draw_polygon(p):
    x1, x2, x3, y1, y2, y3, vx, vy, color = p
    polygon(screen, color, ((x1,y1), (x2,y2), (x3, y3)))

def new_ball():
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]
    return x, y, r, color, vx, vy

def draw_ball(b):
    x, y, r, color, vx, vy = b
    circle(screen, color, (x, y), r)

def move_ball(b):
    x, y, r, color, vx, vy = b
    return x + vx, y + vy, r, color, vx, vy

def move_poly(p):
    x1, x2, x3, y1, y2, y3, vx, vy, color = p
    return x1 + vx, x2 + vx, x3 + vx, y1 + vy, y2 + vy, y3 + vy, vx, vy, color 

pygame.display.update()
clock = pygame.time.Clock()
finished = False

points = 0
count = 0
balls = [new_ball() for _ in range(5)]
poly = [new_polygon() for _ in range(5)]

while not finished:
    clock.tick(FPS)
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button != 1: break
            points += 1 if screen.get_at(event.pos) == RED else -1
            points += 1 if screen.get_at(event.pos) == BLACK else 0
            # for b in balls:
            #     x, y, r, color, vx, vy = b
            #     if (x - event.pos[0])**2 + (y - event.pos[1])**2 < r**2 and color == RED:
            #         points += 1
            #     elif (x - event.pos[0])**2 + (y - event.pos[1])**2 < r**2 and color != RED:
            #         points -= 1
        
    if count == 60:
        poly = [new_polygon() for _ in range(5)]
        balls = [new_ball() for _ in range(5)]
        count = 0
    
    for i in range(len(balls)):
        balls[i] = move_ball(balls[i])
        
    for g in range(len(poly)):
        poly[g] = move_poly(poly[g])
    
    screen.fill("black")
    text_surface = my_font.render(str(points), True, (255, 255, 255))
    screen.blit(text_surface, (0, 0))
    for b in balls:
        draw_ball(b)
    for p in poly:
        draw_polygon(p)
        
    pygame.display.update()

pygame.quit()
 