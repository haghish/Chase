import random
import pygame
from pygame.locals import *
from random import randint
steps = 0 #steps counter

pygame.init()

screen = pygame.display.set_mode((800,600))

#load the player image
sprite = pygame.image.load('smile.png').convert()

# get the screen size
spritew, spriteh = sprite.get_size()
screenw, screenh = screen.get_size()

#initiate the sheep position in the middle.
x0 = screenw/2 - spritew/2
y0 = screenh/2 - spriteh/2
x, y = x0, y0

# Creating Two dimensional array by using lists
times = [0] * screenw
for i in range(0,screenh):
    times[i] = [0] * screenw

# Define moves:
# Tuples to get directions and decide where to go
moves = [(0,1, "up"), (1,0, "right"), (-1,0, "left"), (0,-1, "down")]

N = ( 0, -1)
S = ( 0,  1)
W = (-1,  0)
E = ( 1,  0)
NW = (-1, -1)
NE = (-1,  1)
SE = ( 1,  1)
SW = ( 1, -1)

dx, dy = SW

clock=pygame.time.Clock()

while True:
    #This will not allow the loop to run more than the number of times you
    ## enter per second, and hopefully slow the cube down.
    clock.tick(15)

    # By using randint get a random integer
    dx, dy, position = moves[randint(0, 3)]

    x += dx*5
    y += dy*5
    print("He moved", position)

    #x = x + dx
    #y = y + dy

    #currently it is only drawing when it hits the limits of the screen
    #ranging from 0 to the width size. Change this based on time:
    """
    if x < 0:
        dx, dy = random.choice((E, NE, SE))
    if x > screenw-spritew:
        dx, dy = random.choice((W, NW, SW))
    if y < 0:
        dx, dy = random.choice((S, SW, SE))
    if y > screenh-spriteh:
        dx, dy = random.choice((N, NW, NE))
    """
    #try:
    #    times[x][y] += 1  # And here is, how many times have he stood on each square
    #    steps += 1
    #except IndexError:  # The exit of loop
    #    break

    screen.fill((255,255,255))
    screen.blit(sprite, (x,y))
    pygame.display.update()





