import random
import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800,600))
sprite = pygame.image.load('smile.png').convert()

spritew, spriteh = sprite.get_size()
screenw, screenh = screen.get_size()

x0 = screenw/2 - spritew/2
y0 = screenh/2 - spriteh/2

x, y = x0, y0

# Define moves:

N = ( 0, -1)
S = ( 0,  1)
W = (-1,  0)
E = ( 1,  0)

NW = (-1, -1)
NE = (-1,  1)
SE = ( 1,  1)
SW = ( 1, -1)

dx, dy = SW
while 1:
    x = x + dx
    y = y + dy
    if x < 0:
        dx, dy = random.choice((E, NE, SE))
    if x > screenw-spritew:
        dx, dy = random.choice((W, NW, SW))
    if y < 0:
        dx, dy = random.choice((S, SW, SE))
    if y > screenh-spriteh:
        dx, dy = random.choice((N, NW, NE))    
    screen.fill((255,255,255))
    screen.blit(sprite, (x,y))
    pygame.display.update()





