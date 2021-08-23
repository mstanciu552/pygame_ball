import pygame
from pygame.constants import KEYDOWN, K_ESCAPE, K_SPACE

from Ball import Ball
from Fruit import Fruit

WIDTH  = 1050
HEIGHT = 920

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode([WIDTH, HEIGHT])

font = pygame.font.SysFont('Iosevka', 30)

ball = Ball(WIDTH / 2, HEIGHT / 2, WHITE, 40)
fruit = Fruit(RED, 20)

score = font.render(f'Score: {ball.score}', True, WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_SPACE:
                print(f'Score: {ball.score}')

    window.fill(BLACK)

    score = font.render(f'Score: {ball.score}', True, WHITE)
    window.blit(score, (40, 40))

    fruit.draw(window)

    ball.draw(window)
    ball.handle_press()
    ball.handle_mouse()

    ball.collision(fruit)

    pygame.display.flip()

pygame.quit()
