import pygame
from Fruit import Fruit

class Ball:
    def __init__(self, x, y, color, size):
        self.w, self.h = pygame.display.get_surface().get_size() 
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed_x = 2
        self.speed_y = 2
        self.score = 0

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)

    def move_x(self):
        self.x += self.speed_x
        if self.x + self.size >= self.w or self.x - self.size <= 0:
            self.speed_x = -self.speed_x

    def move_y(self):
        self.y += self.speed_y
        if self.y + self.size >= self.h or self.y - self.size <= 0:
            self.speed_y = -self.speed_y
        
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def handle_press(self):
        pressed = pygame.key.get_pressed()

        BOUND_LEFT  = 0 <= self.x - self.size
        BOUND_RIGHT = self.x + self.size <= self.w
        BOUND_UP    = 0 <= self.y - self.size 
        BOUND_DOWN  = self.y + self.size <= self.h

        if not BOUND_RIGHT:
            self.x -= .1
        if not BOUND_LEFT:
            self.x += .1
        if not BOUND_UP:
            self.y += .1
        if not BOUND_DOWN:
            self.y -= .1

        if pressed[pygame.K_UP] and BOUND_UP:
            self.y -= self.speed_y 
        if pressed[pygame.K_DOWN] and BOUND_DOWN:
            self.y += self.speed_y
        if pressed[pygame.K_LEFT] and BOUND_LEFT:
            self.x -= self.speed_x
        if pressed[pygame.K_RIGHT] and BOUND_RIGHT:
            self.x += self.speed_x

    def handle_mouse(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            MATCH_X = self.x - self.size <= mouse_x and mouse_x <= self.x + self.size
            MATCH_Y = self.y - self.size <= mouse_y and mouse_y <= self.y + self.size
            if MATCH_X and MATCH_Y:
                self.set_x(mouse_x)
                self.set_y(mouse_y)

    def collision(self, fruit: Fruit):
        MATCH_X = self.x - self.size <= fruit.x and fruit.x <= self.x + self.size
        MATCH_Y = self.y - self.size <= fruit.y and fruit.y <= self.y + self.size

        MATCH: bool = MATCH_X and MATCH_Y

        if MATCH:
            fruit.set_rand()
            self.score += 1
