from random import randint
from pygame.draw import *
from settings import *
import pygame




class Target2:
    
    def __init__(self, screen):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.vx = 1
        self.vy = 4
        self.new_target2()

    def new_target2(self):
        """ Инициализация новой цели. """
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(2, 50)
        color = self.color = MAGENTA
        
    def move(self):
        self.x += self.vx
        self.y -= self.vy 
        if self.x > WIDTH - self.r or self.x < self.r:
            self.vx = -self.vx
        if self.y < self.r or self.y > HEIGHT - self.r:
            self.vy = -self.vy 

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points
        

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )