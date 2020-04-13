
player_name = ""
import pygame
from pygame.sprite import Group, Sprite
from pygame.font import Font
from pygame.locals import *
import code
import os                #for getting the path to current directory
import time              #for getting the current time and date
import math              #for doing some computation

#pygame
from pygame.locals import *
from pygame.font import Font
from pygame.mixer import Sound
from pygame.sprite import Sprite, Group

#code
from code.game import Game, Scene
from code.gui import TextButton, ButtonGroup
from code.loader import load_resources

def keyboard(event, name):
    if (event.key == K_a):
        name += "A"
        name_changed = True
    elif (event.key == K_b):
        name += "B"
        name_changed = True
    elif (event.key == K_c):
        name += "C"
        name_changed = True
    elif (event.key == K_d):
        name += "D"
        name_changed = True
    elif (event.key == K_e):
        name += "E"
        name_changed = True
    elif (event.key == K_f):
        name += "F"
        name_changed = True
    elif (event.key == K_g):
        name += "G"
        name_changed = True
    elif (event.key == K_h):
        name += "H"
        name_changed = True
    elif (event.key == K_i):
        name += "I"
        name_changed = True
    elif (event.key == K_j):
        name += "J"
        name_changed = True
    elif (event.key == K_k):
        name += "K"
        name_changed = True
    elif (event.key == K_l):
        name += "L"
        name_changed = True
    elif (event.key == K_m):
        name += "M"
        name_changed = True
    elif (event.key == K_n):
        name += "N"
        name_changed = True
    elif (event.key == K_o):
        name += "O"
        name_changed = True
    elif (event.key == K_p):
        name += "P"
        name_changed = True
    elif (event.key == K_q):
        name += "Q"
        name_changed = True
    elif (event.key == K_r):
        name += "R"
        name_changed = True
    elif (event.key == K_s):
        name += "S"
        name_changed = True
    elif (event.key == K_t):
        name += "T"
        name_changed = True
    elif (event.key == K_u):
        name += "U"
        name_changed = True
    elif (event.key == K_v):
        name += "V"
        name_changed = True
    elif (event.key == K_w):
        name += "W"
        name_changed = True
    elif (event.key == K_x):
        name += "X"
        name_changed = True
    elif (event.key == K_y):
        name += "Y"
        name_changed = True
    elif (event.key == K_z):
        name += "Z"
        name_changed = True
    elif (event.key == K_1):
        name += "1"
        name_changed = True
    elif (event.key == K_2):
        name += "2"
        name_changed = True
    elif (event.key == K_3):
        name += "3"
        name_changed = True
    elif (event.key == K_4):
        name += "4"
        name_changed = True
    elif (event.key == K_5):
        name += "5"
        name_changed = True
    elif (event.key == K_6):
        name += "6"
        name_changed = True
    elif (event.key == K_7):
        name += "7"
        name_changed = True
    elif (event.key == K_8):
        name += "8"
        name_changed = True
    elif (event.key == K_9):
        name += "9"
        name_changed = True
    elif (event.key == K_0):
        name += "0"
        name_changed = True
        # use backspace for correction
    elif (event.key == K_BACKSPACE):
        new_length = len(name) - 1
        name = name[0:new_length]
        name_changed = True

    elif (event.key == K_SPACE):
        name = name + ""
        name_changed = True

    # after entering the user ID, press enter key
    # -------------------------------------------
    elif (event.key == K_RETURN):

        # Save the ID & the wolf letter
        name_changed = False

    # keys which are not allowed
    else:
        name = name + ""
        name_changed = False

    return (name, name_changed)
