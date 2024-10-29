import math
from random import choice, randint
import numpy as np 
from settings import *
from target import *
from ball import *
from gun import *
from target2 import *


import pygame

pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont("Times New Roman", 30)

points = 0

while not finished:
    screen.fill(BLACK)

    text_surface = my_font.render(str(points), True, (200,200,200))
    screen.blit(text_surface, (0, 0))

    gun.draw()
    target.draw()
    target2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
            target.live = 1
            target2.live = 1
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    target.move()
    target2.move()
    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            points += 1
            target.live = 0
            target.hit()
            target.new_target()
    for b in balls:
         b.move()
         if b.hittest(target2) and target2.live:
            points += 1
            target2.live = 0
            target2.hit()
            target2.new_target2()
    gun.power_up()
    
    

pygame.quit()