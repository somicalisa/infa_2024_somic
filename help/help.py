import pygame
from pygame.draw import *
from random import randint
from polygon import *
from ball import *
from settings import *

pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont("Times New Roman", 30)


FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

points = 0
count = 0
balls = [new_ball() for _ in range(5)]
poly = [new_polygon() for _ in range(5)]

while not finished:
    clock.tick(FPS)
   # count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points += 1 if screen.get_at(event.pos) == RED else -1
            points += 1 if screen.get_at(event.pos) == BLACK else 0
            for i in range(len(poly)):
                x1, x2, x3, y1, y2, y3, vx, vy, color = poly[i]
                x, y = event.pos
                ab = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
                if ab < 0:
                    x1, x3, y1, y3 = x3, x1, y3, y1
                if ( (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1) > 0 and 
                     (x - x2) * (y3 - y2) - (y - y2) * (x3 - x2) > 0 and 
                     (x - x3) * (y1 - y3) - (y - y3) * (x1 - x3) > 0):
                    # попали в треугольник
                    points +=1
                    poly[i] = new_polygon()
                
            if event.button != 1: break
            for i in range(len(balls)):
                x, y, r, color, vx, vy = balls[i]
                if (x - event.pos[0])**2 + (y - event.pos[1])**2 < r**2 and color == RED:
                    points += 1
                    balls[i] = new_ball()
                elif (x - event.pos[0])**2 + (y - event.pos[1])**2 < r**2 and color != RED:
                    points -= 1
                    balls[i] = new_ball()
        
    #if count == 60:
     #   poly = [new_polygon() for _ in range(5)]
      #  balls = [new_ball() for _ in range(5)]
       # count = 0
    

    for i in range(len(balls)):
        balls[i] = move_ball(balls[i])
        
    for g in range(len(poly)):
        poly[g] = move_poly(poly[g])
    
    screen.fill("black")
    text_surface = my_font.render(str(points), True, (255, 255, 255))
    screen.blit(text_surface, (0, 0))
    for b in balls:
        draw_ball(b, screen)
    for p in poly:
        draw_polygon(p, screen)
        
    pygame.display.update()

pygame.quit()
 