import pygame
from pygame.draw import *
import random

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

def build_ruchcka(surface,color,x, y, r):
    circle(surface, color, (x, y), r)

def build_window(surface, color, x, y, r):
    circle(surface, color, (x, y ), r, 3)
    line(surface, color, (x, y-r), (x, y+r), 3)
    line(surface, color, (x-r, y), (x+r, y), 3)

def build_door(surface, color, x, y, w, h):
    '''рисуем дверь '''
    rect(surface, color, (x, y-h // 4, w, h))

def build_base(surface, x, y, h, w, color):
    '''порожек'''
    rect(surface, color, (x, y-h, w, h))

def build_wals(surface, color, x, y, w, h):
    '''рисуем стены'''
    rect(surface, color, (x, y-h, w, h))
    
def build_roof(surface,color,x, y, w, h):
    polygon(surface, color, ((x, y), (x+w//2, y-h), (x+w, y)))   
    
def build_truba(surface, color, x, y, h, w):
    rect(surface, color, (x , y - h, w, h))

    
def home_print (surface, color, x, y, h, w):
    '''рисуем дом'''
    build_base(surface, x-3, y+3, 3, w, "brown")
    build_truba(surface, "yellow", x + 2 * w // 3, y- 3 * h // 4, w // 10, h // 15)
    build_wals(surface, color, x, y, w-6, h // 2)
    build_roof(surface, "gray", x-3, y-h//2+3, w, h//2)
    build_door(surface, "black", x + 10, y - h // 4, w // 6, h // 3)
    build_ruchcka(surface,"brown", x + w // 12, y - h // 6, 5)
    build_window(surface, "green", x + 200, y - h//4, h//8)
   
  
  
s = pygame.Surface((300, 300), pygame.SRCALPHA, 32)
s = s.convert_alpha()

home_print(s, "white", 0, 297, 300, 300)

screen.blit(s, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
