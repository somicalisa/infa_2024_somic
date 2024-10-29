from random import choice
from pygame.draw import *
from settings import *
import pygame




class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. Тоесть, обновляет значения
        self.x и self.y сучетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800 х 600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy += -2
        if self.x > WIDTH - self.r:
            self.vx = -self.vx
        if self.y < self.r:
            self.vy = -self.vy
        if self.x < self.r:
            self.y = self. y
            self.vx = 0
            self.vy = 0
        if self.y > HEIGHT - self.r:
            self.x = self.x
            self.vx = 0
            self.vy = 0
        
        


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
    

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (self.x - obj.x)**2 + (self.y - obj.y)**2 < (self.r + obj.r)**2