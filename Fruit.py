import pygame
from random import randint

class Fruit:
    def __init__(self, color, size):
        self.w, self.h = pygame.display.get_surface().get_size()
        self.x = randint(0, self.w)
        self.y = randint(0, self.h)
        self.color = color
        self.size = size
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)   

    def set_rand(self):
        self.x = randint(self.size, self.w - self.size)
        self.y = randint(self.size, self.h - self.size)

    
