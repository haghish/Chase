
# The code procedure:
    # 1) Loading the modules
    # 2) Game default settings


# ====================================================================
# ====================================================================
#                           M O D U L E S
# ====================================================================
# ====================================================================
import random, requests, pygame, code

import os                #for getting the path to current directory
import time              #for getting the current time and date
import math              #for doing some computation
import webbrowser        #for reading the description
import numpy
from numpy import array  #for creating vectors and holding trial information

#pygame
from pygame.locals import *
from pygame.font import Font
from pygame.mixer import Sound
from pygame.sprite import Sprite, Group

#code
from code.game import Game, Scene
from code.gui import TextButton, ButtonGroup
#from code.loader import load_resources
#from code.players import Enemy, Player

from code.keyboard import keyboard
from code.clock import Clock
#from code.scenes import MenuScene
#from code.load_settings import load_settings

#import threading
from datetime import datetime

from code.timer import *
from code.fixSpeed import *

# ====================================================================
# ====================================================================
#                           D E F A U L T
# ====================================================================
# ====================================================================
#These settings can be overruled by "settings.cfg"

screen_width = 800
screen_height = 600
fullscreen = False
x = screen_width
y = screen_height
dx = 0 #used for randomPlayer player
dy = 0 #used for randomPlayer player

backgroundColor = None
fontColor = None
player_sheet = None
title_image = None                  #NOT USED
#end_image = None
next_trial_image = None
players_sheet = None
gameover_sound = None
player_score = 0
is_game_over = False
playerSpeed = 1
wolfSpeed = 1
sheepNumber = 1
sheepNumberTracker = 0
wolfNumberTracker = 0
killZone = 32
Radius = 1
showTimer = True
randomPlayer = False
mouseCursor = False
ID = ""                           # Save the ID in a global
wolf = ""                         # Save wolf name in a global
player_name = ""
trialNumber = 0
trialType = 0
chaseAngle = 0
scapeAngle = 0
chaseRate = 0
duration = 30
trialsTotal = 1
Second = None
SecondPlayer = None               # Time frame for randomPlayer
name_changed=False
game = None
# optimization for enemy spawning
sheep_recycle_bin = []
turnRate = 1
startTime = 0
test = 0
shit = 0
seed = 1
seat = 0   #place of the image

# ====================================================================
# This is a function that parces the seetings.cfg file and reads the
# software's settings.
#
# WARNING: moving this function to a separate file will loose its
# position to the global variables!
# ====================================================================

def load_settings():
    global screen_width
    global screen_height
    global fullscreen
    # global high_score_server_enabled
    global high_score_server_ip
    global playerSpeed
    global wolfSpeed
    global showTimer
    global randomPlayer
    global gameover_sound
    global trialType
    global duration
    global trialsTotal
    global mouseCursor
    global backgroundColor
    global fontColor
    global sheepNumber
    global killZone
    global Radius
    global turnRate
    global chaseAngle
    global scapeAngle
    global chaseRate

    # Loading game configuration
    # ---------------------------------------------------------------
    print("\nLoading game configuration file")
    print("===============================\n")

    try:
        settings = open("settings.cfg", "r")
        for line in settings:
            line = line.rstrip("\n")
            print("Parsing: {}".format(line))
            sline = line.split("=")
            setting = sline[0]
            value = sline[1]
            if setting == "screen_width":
                if value != "": screen_width = int(value)
                print("Set screen width to {}".format(value))
            elif setting == "screen_height":
                if value != "": screen_height = int(value)
                print("Set screen height to {}".format(value))
            elif setting == "playerSpeed":
                if value != "": playerSpeed = int(value)
                print("Set player Speed to {}".format(value))
            elif setting == "wolfSpeed":
                if value != "": wolfSpeed = float(value)
                print("Set wolf Speed to {}".format(value))
            elif setting == "killZone":
                if value != "": killZone = int(value)
                print("Set killZone to {}".format(value))
            elif setting == "turnRate":
                if value != "": turnRate = int(value)
                print("Set turnRate to {}".format(value))
            elif setting == "Radius":
                if value != "": Radius = float(value)
                print("Set Radius to {}".format(value))
            elif setting == "FullScreen":
                if value == "True":
                    fullscreen = True
                elif value == "False":
                    fullscreen = False
                print("Set FullScreen to {}".format(fullscreen))
            elif setting == "showTimer":
                if value == "True":
                    showTimer = True
                elif value == "False":
                    showTimer = False
                print("Set showTimer to {}".format(showTimer))
            elif setting == "randomPlayer":
                if value == "True":
                    randomPlayer = True
                elif value == "False":
                    randomPlayer = False
                print("Set randomPlayer to {}".format(randomPlayer))
            elif setting == "mouseCursor":
                if value == "True":
                    mouseCursor = True
                elif value == "False":
                    mouseCursor = False
                print("Set mouseCursor to {}".format(mouseCursor))
            elif setting == "gameover_sound":
                if value == "True":
                    gameover_sound = True
                elif value == "False":
                    gameover_sound = False
                print("Set gameover_sound to {}".format(gameover_sound))
            elif setting == "trialType":
                if value != "":
                    # trialType = array([[value]])
                    # trialType = array([value])
                    value = value.split(',')
                    trialType = map(int, value)
                    trialsTotal = len(trialType)
                    print("Set trial types to {}".format(value))
                    print("Set total trials to {}".format(trialsTotal))
            elif setting == "chaseAngle":
                if value != "":
                    value = value.split(',')
                    chaseAngle = map(int, value)
                    print("Set chaseAngle to {}".format(value))
            elif setting == "scapeAngle":
                if value != "":
                    value = value.split(',')
                    scapeAngle = map(int, value)
                    print("Set scapeAngle to {}".format(value))
            elif setting == "chaseRate":
                if value != "":
                    value = value.split(',')
                    chaseRate = map(int, value)
                    print("Set chaseAngle to {}".format(value))
            elif setting == "duration":
                if value != "":
                    # trialType = array([[value]])
                    # trialType = array([value])
                    value = value.split(',')
                    duration = map(int, value)
                    print("Set trial duration to {}".format(duration))
            elif setting == "backgroundColor":
                if value != "":
                    value = value.split(',')
                    # and make sure the numbers are integers
                    backgroundColor = map(int, value)
                    print("Set background color to {}".format(backgroundColor))
                    print("background color type: {}".format(type(backgroundColor)))
            elif setting == "fontColor":
                if value != "":
                    fontColor = value
                    print("Set font color to {}".format(fontColor))
            elif setting == "sheepNumber":
                if value != "": sheepNumber = int(value)
                print("Set number of sheeps to {}".format(value))
            # elif setting == "HighScoreServerIp":
            #    high_score_server_enabled = True
            #    high_score_server_ip = value
            #    print("High score server enabled")

            print("\n\n")
        settings.close()

    except:
        print("Error loading game settings")


def load_resources():

    # Title image is used for the main manu
    # global title_image
    # title_image = engine.loader.load("title.jpg")

    # global end_image
    # end_image = engine.loader.load("title.jpg")


    # global next_trial_image
    # next_trial_image = engine.loader.load("high-score.jpg")

    # loads the image file that has the background and players
    global players_sheet
    players_sheet = code.loader.load("players.png")

    # loads the sound for ending the trial (if lost)
    global gameover_sound

    if (gameover_sound == True):
        gameover_sound = code.loader.load("end.ogg")


# ====================================================================
# ====================================================================
#                           C L A S S E S
# ====================================================================
# ====================================================================



# Player
# ===================================================================
class Player(Sprite):

    global screen_width
    global screen_height
    global killZone

    # Initialize the player
    # ---------------------
    def __init__(self):
        Sprite.__init__(self)
        screen = pygame.display.set_mode((screen_width, screen_height))
        self.rect = pygame.draw.circle(screen, (0,0,255), (0,0), 32, 1)

        # image size
        self.image = players_sheet.subsurface(Rect(0, 0, 32, 32))

        #self.rect = Rect(0, 0, 64, 64) #left, top, width, height
        #self.rect = Rect(64, 0, 128, 128)


    # Get the mouse coordinates
    # -------------------------
    def update(self, *args):

        global x
        global y
        global dx
        global dy
        global randomPlayer
        global playerSpeed

        # for randomPlayer
        global SecondPlayer
        global turnRate
        global test
        global sheepNumber
        global screen_width
        global screen_height
        global shit
        global seed
        global playerSpeed
        global scapeAngle


        # Start the game in the center of the screen
        self.rect.centerx = x
        self.rect.centery = y

        # Defining two modes for the sheep's movement
        # -------------------------------------------
        if randomPlayer == False:

            # get the position of the mouse pointer
            # -------------------------------------
            (mouse_x, mouse_y) = pygame.mouse.get_pos()

            #ALTERNATIVELY YOU COULD
            # mouse_x = args[0]
            # mouse_y = args[1]
            # print("mouse X {}".format(mouse_x))

            # Calculate the distance between the two points
            xdiff = mouse_x - x
            ydiff = mouse_y - y

            # Get the fix speed movement in terms of x and y
            dx, dy = fixSpeed(playerSpeed, xdiff, ydiff)

            # update the points, considering the minimum movement
            if (abs(xdiff) >= playerSpeed):
                self.rect.centerx += dx
            else:
                self.rect.centerx = mouse_x

            if (abs(ydiff) >= playerSpeed):
                self.rect.centery += dy
            else:
                self.rect.centery = mouse_y

            # Update the location of the globals
            x = self.rect.centerx
            y = self.rect.centery

            # Stay within the game screen
            # -----------------------------------------------------------
            if self.rect.left < 0:               self.rect.left = 0
            if self.rect.top < 0:                self.rect.top = 0
            if self.rect.right > (screen_width):   self.rect.right = screen_width
            if self.rect.bottom > (screen_height): self.rect.bottom = screen_height


        # RANDOM WALK
        # -------------------------------
        elif randomPlayer:
            now = datetime.now().second

            angleTarget = numpy.rad2deg(numpy.arctan2(dy, dx))
            angleNoise = scapeAngle[trialNumber]                            # 4) get a random noise angle



            angleLow = int(angleTarget - angleNoise)                        # 5) adjust the angle to the target by adding the random noise
            angleUp = int(angleTarget + angleNoise)
            angle = random.randrange(angleLow, angleUp, 1)                  # 6) get an angle in the range
            radius = 100
            # 7) get a random point within the angle
            randomPointx = math.cos(math.radians(angle)) * radius;
            randomPointy = math.sin(math.radians(angle)) * radius;
            #print angle

            if (SecondPlayer == None):
                SecondPlayer = now
                #randomPointx = random.gauss(0, .2)
                #randomPointy = random.gauss(0, .2)
                randomPointx = math.cos(math.radians(angle)) * radius;
                randomPointy = math.sin(math.radians(angle)) * radius;
                dx, dy = fixSpeed(playerSpeed, randomPointx, randomPointy)

            if (now < 1 and SecondPlayer != 0):
                SecondPlayer = 0
                #randomPointx = random.gauss(0, .2)
                #randomPointy = random.gauss(0, .2)
                randomPointx = math.cos(math.radians(angle)) * radius;
                randomPointy = math.sin(math.radians(angle)) * radius;
                dx, dy = fixSpeed(playerSpeed, randomPointx, randomPointy)

            elif ((SecondPlayer + turnRate) == now):
                SecondPlayer += turnRate
                test = 0
                #randomPointx = random.gauss(0, .2)
                #randomPointy = random.gauss(0, .2)
                randomPointx = math.cos(math.radians(angle)) * radius;
                randomPointy = math.sin(math.radians(angle)) * radius;
                dx, dy = fixSpeed(playerSpeed, randomPointx, randomPointy)

            else:
                test += 1
                seed += 1

            #for x in range(0, sheepNumber):
            #    if (test == (1 + x)):

#            self.dy = dx
#            self.dx = dy


            #print now, SecondPlayer



            # Stay within the game screen
            if self.rect.left < 0:
                self.rect.left = 0
                dx *= -1
                self.rect.centerx += dx

            elif self.rect.centerx > screen_width - 32:
                self.rect.centerx = screen_width - 32
                dx *= -1
                self.rect.centerx += dx

            elif self.rect.top < 0:
                self.rect.top = 0
                dy *= -1
                #self.rect.centery += dy

            elif self.rect.centery > screen_height - 16:
                self.rect.centery = screen_height - 16
                dy *= -1
                #self.rect.centery += dy
            else:
                self.rect.centerx += dx
                self.rect.centery += dy


            # Update the location of the globals
            x = self.rect.centerx
            y = self.rect.centery
            #self.rect.centerx += self.dx  # * 10
            #self.rect.centery += self.dy  # * 10 #* args[0]




# Sheep
# ===================================================================
class Sheep(Sprite):
    global screen_width
    global screen_height


    def __init__(self, x, y, dx, dy):

        global sheepNumber
        global sheepNumberTracker


        Sprite.__init__(self)
        #self.rect = Rect(0, 0, 64, 64)
        screen = pygame.display.set_mode((screen_width, screen_height))
        self.rect = pygame.draw.circle(screen, (0, 0, 255), (0, 0), 16, 1)
        self.image = players_sheet.subsurface(Rect(32, 0, 32, 32))


        #DEFINE THE START POINT FOR EACH CIRCLE
        #======================================

        self.rect.centerx = x
        self.rect.centery = y


        self.dx = dx
        self.dy = dy

        #def printit():
        #    threading.Timer(1.0, printit).start()
        #    self.dx = self.dx * -.1
        #    self.dy = self.dy * -.1
        #    print(self.dx, self.dy)
        #printit()



    def update(self, *args):
        global Second
        global turnRate
        global test
        global sheepNumber
        global screen_width
        global screen_height
        global shit
        global seed

        # in case of colision, args is -1
        if (args[0] == -1):
            self.dx *= -1
            self.dy *= -1
        else:
            now = datetime.now().second

            if (Second == None):
                Second = now

            if (now == 0):
                Second = 0

            elif ((Second + turnRate) == now):
                Second += turnRate
                test = 0
                # self.dy = random.uniform(-.1, .1)
                # self.dx = random.uniform(-.1, .1)
            else:
                test += 1
                seed += 1
                #print(test)



            """
            if (Second == None):
                Second = now
            elif ((Second + turnRate) == now):
                Second += turnRate
                #self.dy = random.uniform(-.1, .1)
                #self.dx = random.uniform(-.1, .1)
                test = 0
            else:
                test += 1
                print(test)
            """

            #print(self.dx)

            for x in range(0, sheepNumber):
                if (test == (1+x)):
                    #random.seed(seed)
                    #self.dy = random.uniform(0, 0)
                    #self.dx = random.uniform(-.1, .1)
                    randomPointx = random.gauss(0, .2)
                    randomPointy = random.gauss(0, .2)
                    dx, dy = fixSpeed(wolfSpeed, randomPointx, randomPointy)
                    self.dy = dx
                    self.dx = dy

                    #shit += dx
                    #print(shit)




            # args[0] = delta time in milliseconds

            # Using clock tick?
            #clock = pygame.time.Clock()
            #clock.tick(15)

            # WOLF Walking Algorithm
            # ======================






            #dy = random.uniform(-10, 10)

            #self.rect.centerx += self.dx * args[0]
            #self.rect.centery += self.dy * args[0]

        # Stay within the game screen
        if self.rect.left < 0:
            self.rect.left = 0
            self.dx *= -1
            # dx = random.uniform(0, 100)
            # self.rect.centerx += dx

        #if self.rect.right > screen_width - 16:
        if self.rect.centerx > screen_width - 32:
            self.rect.centerx = screen_width - 32
            #self.dx *= -1
            # dx = random.uniform(-10, 0)
            # self.rect.centerx += dx

        if self.rect.top < 0:
            self.rect.top = 0
            self.dy *= -1
            # dy = random.uniform(0, 100)
            # self.rect.centery += dy

        if self.rect.centery > screen_height - 16  :
            # dy = random.uniform(-10, 0)
            # self.rect.centery += dy
            #self.rect.bottom = screen_height - 32
            self.rect.centery = screen_height - 16
            self.dy *= -1
            # self.rect.bottom = screen_height



        self.rect.centerx += self.dx #* 10
        self.rect.centery += self.dy #* 10 #* args[0]

        """
        x = self.rect.centerx
        goX = x + dx

        print(self.rect.centerx, dx, goX)

        if (x != goX):
            if (abs(dx) <= wolfSpeed):
                self.rect.centerx = goX

            if (dx > 0):
                if (dx > wolfSpeed):
                    while self.rect.centerx < goX:
                        self.rect.centerx = self.rect.centerx + wolfSpeed
                else:
                    self.rect.centerx = goX
            elif (dx < 0):
                if (dx < wolfSpeed):
                    while self.rect.centerx > goX:
                        self.rect.centerx = self.rect.centerx - wolfSpeed
                else:
                    self.rect.centerx = goX
        """
        #self.rect.centery += self.dy * args[0]

        """
        #self.rect.centerx += dx
        #self.rect.centery += dy
        print(self.rect.centerx, dx)

        self.rect.centerx += self.dx * args[0]
        self.rect.centery += self.dy * args[0]

        #print(sheepNumberTracker, x, y)
        #print(x, dx, self.dx, args[0])
        # if Sheep goes off screen kill it and spawn a new Sheep
        #screen_w = game.screen_rect.width
        #screen_h = game.screen_rect.height
        """





        """
        is_sheep_out = False
        if (self.rect.left > screen_w):
            is_sheep_out = True
        if (self.rect.right < 0):
            is_sheep_out = True
        if (self.rect.top > screen_h):
            is_sheep_out = True
        if (self.rect.bottom < 0):
            is_sheep_out = True

        if (is_sheep_out):
            sheep_recycle_bin.append(self)
            self.kill()
        """

# Wolf
# ===================================================================
class Wolf(Sprite):
    global screen_width
    global screen_height
    global killZone

    def __init__(self, x, y, dx, dy):

        Sprite.__init__(self)
        # self.rect = Rect(0, 0, 64, 64)
        screen = pygame.display.set_mode((screen_width, screen_height))
        self.rect = pygame.draw.circle(screen, (0, 0, 255), (0, 0), killZone, 1)

        self.image = players_sheet.subsurface(Rect(32, 0, 32, 32))

        # DEFINE THE START POINT FOR EACH CIRCLE
        # ======================================

        self.rect.centerx = x
        self.rect.centery = y

        self.dx = dx
        self.dy = dy

        # def printit():
        #    threading.Timer(1.0, printit).start()
        #    self.dx = self.dx * -.1
        #    self.dy = self.dy * -.1
        #    print(self.dx, self.dy)
        # printit()

    def update(self, *args):
        global wolfSpeed
        global chaseAngle
        global chaseRate
        global trialNumber
        global Second
        global turnRate
        global test
        global sheepNumber
        global wolfNumberTracker
        global screen_width
        global screen_height
        global shit
        global seed
        global x
        global y

        now = datetime.now().second

        if (Second == None):
            Second = now

        if (now == 0):
            Second = 0

        if (Second  == now):
            Second += turnRate
            test = 0

            # get the chase rate
            probability = numpy.random.choice(100, 1)
            probability += 1

            if probability <= chaseRate[trialNumber]:
                # self.dy = random.uniform(-.1, .1)
                # self.dx = random.uniform(-.1, .1)
                # 1) get the player position (x & y global)
                # 2) get the wolf position (self.rect.centerx & self.rect.centery)
                # 3) get the ANGLE to the target and the DISTANCE (i.e. radius)
                angleTarget = numpy.rad2deg(numpy.arctan2(y - self.rect.centery, x - self.rect.centerx))

                SquerdDistance = ((y - self.rect.centery)**2) + ((x - self.rect.centerx)**2)
                radius = math.sqrt(SquerdDistance)
                print radius
                # 4) get a random noise angle
                angleNoise = chaseAngle[trialNumber]

                # 5) adjust the angle to the target by adding the random noise
                angleLow = int(angleTarget - angleNoise)
                angleUp = int(angleTarget + angleNoise)

                # 6) get an angle in the range
                angle = random.randrange(angleLow, angleUp, 1)
                # print("ANGLE", angleTarget, angleLow, angleUp)

                # 7) get a random point within the angle
                randomPointx = math.cos(math.radians(angle)) * radius;
                randomPointy = math.sin(math.radians(angle)) * radius;

                # 8) get the dx and dy and set a fix speed
                dx, dy = fixSpeed(wolfSpeed, randomPointx, randomPointy)

                self.dx = dx #* args[0]
                self.dy = dy #randomPointy / radius

                # self.rect.centerx += self.dx * args[0]
                # self.rect.centery += self.dy * args[0]
            else:
                randomPointx = random.gauss(0,.2)
                randomPointy = random.gauss(0, .2)
                dx, dy = fixSpeed(wolfSpeed, randomPointx, randomPointy)
                self.dy = dx
                self.dx = dy

        self.rect.centerx += self.dx  # * 10
        self.rect.centery += self.dy  # * 10  # * args[0]

        # Stay within the game screen
        if self.rect.left < 0:
            self.rect.left = 0
            #self.dx *= -1
            # dx = random.uniform(0, 100)
            # self.rect.centerx += dx

        #if self.rect.right > screen_width - 16:
        if self.rect.centerx > screen_width - 32:
            self.rect.centerx = screen_width - 30
            #self.dx *= -1
            #dx = random.uniform(-10, 0)
            # self.rect.centerx += dx

        if self.rect.top < 0:
            self.rect.top = 0
            #self.dy *= -1
            # dy = random.uniform(0, 100)
            # self.rect.centery += dy

        if self.rect.centery > screen_height - 16  :
            # dy = random.uniform(-10, 0)
            # self.rect.centery += dy
            #self.rect.bottom = screen_height - 32
            self.rect.centery = screen_height - 15
            #self.dy *= -1



# ====================================================================
# ====================================================================
#                           S  C  E  N  E  S
# ====================================================================
# ====================================================================

# --------------------------------------------------------------------
# Trial Scene
# ====================================================================
class trialScene(Scene):
    name = "trial"

    global sheepNumber
    global sheepNumberTracker
    global wolfNumberTracker
    wolfNumberTracker = 0 #RESET

    def on_init(self):
        global is_game_over
        global mouseCursor
        global wolfSpeed

        # initialize event system
        self.outer_event_system = code.event.TimedEventSystem()
        self.inner_event_system = code.event.TimedEventSystem()

        # game constants
        self.sheep_speed = wolfSpeed
        self.wolf_speed = wolfSpeed
        self.millis_per_sheep = 1000

        # game variables
        self.max_enemies = 0
        self.game_time = 0

        # set game over variable to false

        is_game_over = False

        self.is_paused = False

        # hide the mouse cursor
        pygame.mouse.set_visible(mouseCursor)

        # create the background image
        screen_w = self.parent.screen.get_width()
        screen_h = self.parent.screen.get_height()

        # define the initial mouse & player positions
        # -------------------------------------------
        global x
        global y
        pygame.mouse.set_pos(screen_w / 2, screen_h / 2)
        x = int(screen_w / 2)
        y = int(screen_h / 2)

        #background_tile = players_sheet.subsurface(Rect(0, 0, 32, 32))
        #self.create_background(screen_w, screen_h, background_tile)

        # initialize the player
        self.player_group = Group()
        player_sprite = Player()
        player_sprite.add(self.player_group)

        # initialize the sheep group
        self.sheep_group = Group()
        self.wolf_group = Group()

        # initialize the game clock
        self.clock = Clock()



    def on_cleanup(self):
        pass

    def on_update(self, delta, events):
        global duration
        global sheepNumberTracker
        global sheepNumber
        global wolfNumberTracker
        global Second
        global trialNumber
        global trialType

        self.outer_event_system.update(delta)

        if (not self.is_paused):
            # update the game clock
            self.clock.update(delta)

            # keep track of game duration and update sheep count
            self.game_time += delta

            #print(self.game_time)



            # = self.game_time / self.millis_per_sheep
            self.max_enemies = sheepNumber

            # update timed events
            self.inner_event_system.update(delta)

            # update player group with mouse position
            mouse_pos = pygame.mouse.get_pos()
            self.player_group.update(mouse_pos[0], mouse_pos[1])


            #def printit(dx, dy):
                #threading.Timer(1.0, printit).start()
                # self.dx = self.dx * -.1
                # self.dy = self.dy * -.1
                # print(self.dx, self.dy)
                #print("HIHI")
                #return (dx, dy)

            #dx, dy = printit(dx, dy)



            """
            now = datetime.now().second
            if (now == 0):
                Second = 0
            if (Second == 0):
                Second = now
                dy = random.uniform(-10, 10)
            elif (Second + 1 == now):
                Second += 1
                dy = random.uniform(-10, 10)
                print(int(dy), Second)
            """


            # update the sheep group
            self.sheep_group.update(delta)
            self.wolf_group.update(delta)

            # Add the requested number of wolf and sheep
            if (wolfNumberTracker == 0 and trialType[trialNumber] > 0):
                wolfNumberTracker = numpy.random.choice((sheepNumber), 1, replace=False)
                wolfNumberTracker += 1  #because the sample includes 0, so I correct the range

            if ((len(self.sheep_group)+len(self.wolf_group))  < self.max_enemies):
                sheepNumberTracker += 1
                if (sheepNumberTracker != wolfNumberTracker):
                    self.spawn_sheep()
                else:
                    self.spawn_wolf()



            # ENDING THE GAME
            # ======================================================================

            # check for collision
            for player_sprite in self.player_group:
                for sheep_sprite in self.sheep_group:
                    if (pygame.sprite.collide_circle(player_sprite, sheep_sprite)):
                        # self.game_over()
                        # dx = -1
                        self.sheep_group.update(-1)
            for player_sprite in self.player_group:
                for wolf_sprite in self.wolf_group:
                    if (pygame.sprite.collide_circle(player_sprite, wolf_sprite)):
                        self.game_over()

            # if the duration of the trial is reached, end the game
            # -----------------------------------------------------
            try:
                if (self.game_time > (duration[trialNumber] * 1000)):
                    self.game_over()
            except ValueError:
                print("")
                    # self.parent.set_next_scene("end")


    def on_render(self, screen):
        # clear the screen
        pygame.draw.rect(screen, Color("black"), self.parent.screen_rect)

        global backgroundColor

        # add background color
        # --------------------
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((backgroundColor))
        screen.blit(background, (0, 0))

        # draw background
        #screen.blit(self.background_image, Rect(0, 0, screen_width, screen_height))
        # draw the player, sheep, and wolf
        self.player_group.draw(screen)
        self.sheep_group.draw(screen)
        self.wolf_group.draw(screen)

        # draw clock counter
        self.clock.draw(screen)

    def create_background(self, width, height, image):
        """Create the background image for the game.
        Returns a new Surface object."""
        tiles_x = width / 32
        if (width % 32) > 0:
            tiles_x += 1

        tiles_y = height / 32
        if (height % 32) > 0:
            tiles_y += 1

        background = pygame.Surface((width, height))
        for x in range(0, tiles_x):
            for y in range(0, tiles_y):
                background.blit(image, Rect(x * 32, y * 32, 32, 32))

        self.background_image = background

    def spawn_sheep(self):
        global Radius
        global sheepNumberTracker
        global sheepNumber
        global screen_width

        # use existing enemies from the recycle bin if available
       # if (len(sheep_recycle_bin) > 0):
        #    sheep = sheep_recycle_bin.pop()
        #    sheep.rect.center = (spawn_x, spawn_y)
        #    sheep.dx = dx
        #    sheep.dy = dy
        #else:
        #    sheep = Sheep(spawn_x, spawn_y, dx, dy)

        dx = random.uniform(-0.1, 0.1)
        dy = random.uniform(-0.1, 0.1)


        #spawn_x = screen_width
        #spawn_y = screen_height

        # Generate uniform random radian with average of pi
        unirad = random.vonmisesvariate(math.pi, 0)
        spawn_x = (math.cos(unirad)*Radius)+(screen_width/2)
        spawn_y = (math.sin(unirad)*Radius)+(screen_height/2)

        sheep = Sheep(spawn_x, spawn_y, dx, dy)
        #self.rect = pygame.draw.circle(screen, (0, 0, 255), (0, 0), 50, 1)



        seat = (sheepNumberTracker*32)
        sheep.image = players_sheet.subsurface(Rect(seat, 0, 32, 32))
        self.sheep_group.add(sheep)




    def spawn_wolf(self):

        # RESET THE wolfNumberTracker when the game is over

        global Radius
        global sheepNumberTracker
        global wolfNumberTracker
        global screen_width

        dx = random.uniform(-0.1, 0.1)
        dy = random.uniform(-0.1, 0.1)

        # Generate uniform random radian with average of pi
        unirad = random.vonmisesvariate(math.pi, 0)
        spawn_x = (math.cos(unirad)*Radius)+(screen_width/2)
        spawn_y = (math.sin(unirad)*Radius)+(screen_height/2)

        wolf = Wolf(spawn_x, spawn_y, dx, dy)
        #self.rect = pygame.draw.circle(screen, (0, 0, 255), (0, 0), 50, 1)

        seat = (wolfNumberTracker*32)
        wolf.image = players_sheet.subsurface(Rect(seat, 0, 32, 32))
        self.wolf_group.add(wolf)
        #print("THE WOLF NUMBER IS", wolfNumberTracker)





    def game_over(self):
        global player_score
        global gameover_sound
        global wolfNumberTracker
        global sheepNumberTracker
        global Second
        global SecondPlayer

        player_score = self.game_time
        # print score to console and play buzzer sound
        print("Game Over\tScore: {}".format(player_score))

        # if gameover sound is True, play it! If the confoguration
        # is True, the value IS NOT TRUE here because I load the sound
        # with the same name. That's why I use "!= False" here
        if (gameover_sound != False):
            gameover_sound.play()

        # create a timer for 3 seconds and then go to high score scene
        def timer_func():
            #global mouseCursor
            self.parent.set_next_scene("detect")
            self.finished = True
            pygame.mouse.set_visible(True)

        self.outer_event_system.add(2000, timer_func)
        self.is_paused = True
        global is_game_over
        is_game_over = True

        # RESET VALUES
        sheepNumberTracker = 0
        Second = None
        SecondPlayer = None






# --------------------------------------------------------------------
# ID Scene
# ====================================================================
class IDScene(Scene):
    name = "ID"
    global backgroundColor
    def on_init(self):
        # logical for controling the ID that turns to False after Enter
        self.write_name = True
        self.player_name = ""

        # initialize buttons
        self.button_group = ButtonGroup()
        self.type_info()

    def on_cleanup(self):
        pass

    # Data controller
    # ===============
    def type_info(self):

        global fontColor
        
	# WHAT IS YOUR USERNAME?
        print("Save the user ID")
        # render the text to prompt the user for their name
        font = Font(pygame.font.get_default_font(), 24)
        self.player_name_prompt_group = Group()
        prompt_sprite = Sprite(self.player_name_prompt_group)
        prompt_sprite.image = font.render("Enter Your Username and press 'enter key'",
                                          True, Color(fontColor))
        #prompt_sprite.rect = Rect(0, 0, prompt_sprite.image.get_width(),
        #                                 prompt_sprite.image.get_height())
        prompt_sprite.rect = Rect(0, 0, prompt_sprite.image.get_width(),
                                         game.screen_rect.height)
        prompt_sprite.rect.center = (game.screen_rect.width / 2,
                                     (game.screen_rect.width / 2) + 64)

        # group to hold the player name image
        self.player_name_group = Group()
        # clear the player name image
        self.draw_name()


    # on update, if the "write_name" is "True" continue writing. Otherwise
    # move to the next scene!
    def on_update(self, delta, events):
        global ID
        global player_name
        global name_changed

        if (self.write_name):

            #enter only capital letters and numbers
            for event in events:
                if (event.type == KEYDOWN):
                    name_changed = False

                    results = keyboard(event, ID)

                    #Update ID
                    ID = results[0]

                    self.player_name = ID

                    name_changed = results[1]

                    print(results[0])
                    # after entering the user ID, press enter key
                    # -------------------------------------------
                    if (event.key == K_RETURN):

                        # Save the ID
                        #ID = self.player_name
                        print("\nSaving the User ID " + ID)

                        # switch off writing
                        self.write_name = False

                    if (name_changed):
                        if (len(ID) > 12):
                            ID = ID[0:len(ID) - 1]
                        self.draw_name()
        else:
            # not in high score mode, just displaying the high scores
            self.button_group.update()

    def on_render(self, screen):
        global backgroundColor
        #WHY BOTHERING WITH BACKGROUND IMAGE?
        #screen.blit(next_trial_image, self.parent.screen_rect)
        self.button_group.draw(screen)

        # add background color
        # --------------------
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((backgroundColor))
        screen.blit(background, (0, 0))

        if (self.write_name):
            # prompt player for their name
            self.player_name_prompt_group.draw(screen)

            global screen_width
            global screen_height
            # draw a box area where the player can type in their name
            pygame.draw.rect(screen, Color("orange"), Rect(screen_width/2-110, (screen_height/2)-16, 220, 32), 3)
            # draw the player's name as they type it
            self.player_name_group.draw(screen)
        else:
            game.set_next_scene("menu")
            game.current_scene.finished = True

    # Draw the subject ID
    # -------------------
    def draw_name(self):
        self.player_name_group.empty()
        font = Font(pygame.font.get_default_font(), 24)
        player_name_sprite = Sprite(self.player_name_group)
        player_name_sprite.image = font.render(self.player_name, True, Color(fontColor))
        player_name_sprite.rect = Rect(0, 0, player_name_sprite.image.get_width(),
                                       player_name_sprite.image.get_height())
        player_name_sprite.rect.center = (game.screen_rect.width / 2,
                                          game.screen_rect.height/2)




# --------------------------------------------------------------------
# MENU SCENE
# ====================================================================
class MenuScene(Scene):
    name = "menu"
    global backgroundColor
    global fontColor


    def on_init(self):
        # add buttons
        global screen_w
        global screen_h
        screen_w = game.screen.get_width()
        screen_h = game.screen.get_height()

        self.button_group = ButtonGroup()

        play_button = self.PlayButton()
        play_button.rect.centerx = screen_w / 2
        play_button.rect.centery = screen_h / 2
        self.button_group.add(play_button)

        high_score_button = self.DescriptionButton()
        high_score_button.rect.centerx = screen_w / 2
        high_score_button.rect.centery = screen_h * 0.75
        self.button_group.add(high_score_button)

        exit_button = self.ExitButton()
        exit_button.rect.bottomleft = (64, 536)
        self.button_group.add(exit_button)



    def on_cleanup(self):
        pass

    def on_update(self, delta, events):
        self.button_group.update()

    def on_render(self, screen):
        global backgroundColor

        # add background color
        # --------------------
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((backgroundColor))
        screen.blit(background, (0, 0))

        # Adding a background image on the main menu
        # ------------------------------------------

        # by activating the code below and defining "title_image"
        # you can add a background image. BUT THAT WON'T ALLOW YOU
        # to set the screen resolution without screwing the background

        #screen.blit(title_image, self.parent.screen_rect)

        credit = "Developed by HAGHISH UG,  http://haghish.com/"
        myFont = pygame.font.SysFont("monaco", 18)
        screen.blit(myFont.render(credit, True, Color(fontColor)), (screen_w/2 - 150, 20))
        self.button_group.draw(screen)

    # START button
    # ------------------------------------------
    class PlayButton(TextButton):
        def __init__(self):
            TextButton.__init__(self, "START", 76, color=Color(fontColor))

        def on_click(self):
            # go to the play scene
            game.set_next_scene("trial")
            game.current_scene.finished = True

    # Description button
    # ------------------------------------------
    class DescriptionButton(TextButton):
        def __init__(self):
            TextButton.__init__(self, "Description", 36, color=Color(fontColor))

        def on_click(self):
            # game.set_next_scene("findwolf")
            path = os.path.dirname(os.path.abspath(__file__))
            url = path + '/resources/html/description.html'
            new = 1
            webbrowser.open(url,new=new)
            game.current_scene.finished = True


    class ExitButton(TextButton):
        def __init__(self):
            TextButton.__init__(self, "EXIT", 32, color=Color(fontColor))

        def on_click(self):
            game.stop()



# --------------------------------------------------------------------
# WOLF DETECTED?
# ====================================================================
class DetectScene(Scene):
    name = "detect"
    global backgroundColor
    global fontColor

    def on_init(self):
        # add buttons
        global screen_w
        global screen_h
        screen_w = game.screen.get_width()
        screen_h = game.screen.get_height()

        self.button_group = ButtonGroup()

        play_button = self.PlayButton()
        play_button.rect.centerx = screen_w / 3
        play_button.rect.centery = screen_h / 2
        self.button_group.add(play_button)

        high_score_button = self.DescriptionButton()
        high_score_button.rect.centerx = screen_w*2 / 3
        #high_score_button.rect.centery = screen_h * 0.75
        high_score_button.rect.centery = screen_h / 2
        self.button_group.add(high_score_button)

        #exit_button = self.ExitButton()
        #exit_button.rect.bottomleft = (64, 536)
        #self.button_group.add(exit_button)

        # Write the data
        if (is_game_over):
            self.save_trial()


    def on_cleanup(self):
        pass

    def on_update(self, delta, events):
        self.button_group.update()



    def on_render(self, screen):
        global backgroundColor

        # add background color
        # --------------------
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((backgroundColor))
        screen.blit(background, (0, 0))

        # Adding a background image on the main menu
        # ------------------------------------------

        # by activating the code below and defining "title_image"
        # you can add a background image. BUT THAT WON'T ALLOW YOU
        # to set the screen resolution without screwing the background

        # screen.blit(title_image, self.parent.screen_rect)

        credit = "Did You Detect a Wolf?"
        myFont = pygame.font.SysFont("monaco", 48)
        screen.blit(myFont.render(credit, True, Color(fontColor)), (screen_w/2 - 185, 100)) #position of the text
        self.button_group.draw(screen)


    # Write THE WHOLE ROW AT ONCE
    # --------------------------
    def save_trial(self):
        global ID
        global player_score
        global trialNumber
        global trialType
        global wolf
        global wolfNumberTracker
        try:
            # If data.csv does not exist, create it and write the header.
            #   Otherwise, append the existing file
            if (os.path.isfile('data.csv')):
                data_file = open("data.csv", "a")
            else:
                data_file = open("data.csv", "w+")
                data_file.write("id, trial, trialtype, trial_time, act_olf, wolf\n")

            # Make a list and get the actual wolf name: A, C, D, E, H, K, L, M, S, T, U, Z
            #NameVector = numpy.array(["0","A","B","C","D","E","F","G","H","I","J","K","L",
            #                      "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
            NameVector = numpy.array(["0", "A", "C", "D", "E", "H", "K", "L", "M", "S", "T", "U", "Z"])
            actwolf = a = ' '.join(map(str, NameVector[wolfNumberTracker]))

            # for high_score in self.high_scores:
            #   data_file.write(high_score[0] + ", " + str(high_score[1]) + "\n")
            data_file.write(ID + "," + str(trialNumber+1)+ "," + str(trialType[trialNumber])
                            + "," + str(player_score) + "," + str(actwolf) + "," )
            print("\nWrite a Row but don't end it ")
            # print(ID + "," + str(trialNumber) + "," + str(player_score) + ",")
            data_file.close()
        except IOError:
            print("error saving high score data file")

        # RESET VALUES
        wolfNumberTracker = 0

    # Write the Username ID
    # =====================
    #def write_data(self):
    #    global ID
    #    try:
    #        data_file = open("data.csv", "w+")
    #        data_file.write(ID + ", ")
    #        data_file.close()
    #    except IOError:
    #        print("error saving user's data")

    # START button
    # ------------------------------------------
    class PlayButton(TextButton):
        def __init__(self):
            TextButton.__init__(self, "Yes", 76, color=Color(fontColor))

        def on_click(self):
            # go to the trial scene
            game.set_next_scene("findwolf")
            game.current_scene.finished = True

    # Description button
    # ------------------------------------------
    class DescriptionButton(TextButton):

        # Add Wolf Information
        # --------------------------
        def write_wolf(self):
            print("\nThe wolf is " + str(wolf))
            try:
                data_file = open("data.csv", "a")
                data_file.write(str(wolf) + "\n")
                data_file.close()
            except IOError:
                print("error saving wolf data file")

        def __init__(self):
            TextButton.__init__(self, "No", 76, color=Color(fontColor))

        def on_click(self):
            global trialNumber
            global trialsTotal
            global wolf

            # set wolf to be 0 in the data
            wolf = 0
            self.write_wolf()

            # go to the next trial
            trialNumber = trialNumber + 1
            if (trialNumber != trialsTotal):
                game.set_next_scene("trial")
            else:
                game.set_next_scene("end")
            game.current_scene.finished = True


# --------------------------------------------------------------------
# findWolf Scene
# ====================================================================
class findWolf(Scene):
    name = "findwolf"

    def on_init(self):
        # boolean to control if the player should enter their name
        self.high_score_mode = False

        self.player_name = ""

        # sprites that display the high score table
        self.score_group = Group()

        # initialize buttons
        self.button_group = ButtonGroup()

        back_button = self.BackButton()
        back_button.rect.bottomleft = (screen_width / 1.2, 536)
        self.button_group.add(back_button)

        #lunch the data controller
        self.data_controller()


    def on_cleanup(self):
        pass




    # Add Wolf Information
    # --------------------------
    def write_wolf(self):
        global wolf
        print("\nThe wolf is " + wolf)
        try:
            data_file = open("data.csv", "a")
            data_file.write(str(wolf) + "\n")
            print(str(wolf) + "")
            data_file.close()
        except IOError:
            print("error saving wolf data file")


    # Data controller
    # ===============
    def data_controller(self):
        high_score_achieved = False

        print("Specify the wolf")
        font = Font(pygame.font.get_default_font(), 24)
        self.player_name_prompt_group = Group()
        prompt_sprite = Sprite(self.player_name_prompt_group)
        prompt_sprite.image = font.render("Specify the wolf and press 'enter key'",
                                          True, Color("white"))
        # prompt_sprite.rect = Rect(0, 0, prompt_sprite.image.get_width(),
        #                                 prompt_sprite.image.get_height())
        prompt_sprite.rect = Rect(0, 0, prompt_sprite.image.get_width(),
                                  game.screen_rect.height)
        prompt_sprite.rect.center = (game.screen_rect.width / 2,
                                     (game.screen_rect.width / 2) + 64)

        # group to hold the player name image
        self.player_name_group = Group()
        # clear the player name image
        self.redraw_player_name()
        # switch into high score mode
        self.high_score_mode = True

        #if (is_game_over):
            #self.save_trial()





    def on_update(self, delta, events):
        global player_score
        global ID
        global wolf
        global player_name

        if (self.high_score_mode):

            # enter only capital letters and numbers
            for event in events:
                if (event.type == KEYDOWN):
                    name_changed = False

                    wolfname = ""

                    #use player_name to avoid updating the wolf global
                    results = keyboard(event, wolfname)

                    if (event.key != K_RETURN):
                        wolf = results[0]
                        name_changed = results[1]

                        self.player_name = wolf
                        player_name = wolf
                        print("wolf name> " + wolf)


                    # after entering the user ID, press enter key (change=FALSE)
                    # -------------------------------------------
                    if (event.key == K_RETURN):

                        #print("player name: " + wolf)

                        #wolf = self.player_name

                        # Save the wolf letter
                        #if (ID == None):
                        #    ID = self.player_name
                        #else:
                        #wolf = self.player_name

                        print("\nThe wolf is " + wolf)
                        self.write_wolf()

                        # print("High score of " + str(player_score) + " achieved by " + self.player_name)


                        # insert the player name and insert the entry into the list
                        # self.high_scores.pop()
                        # self.high_scores.insert(self.high_score_index, (self.player_name, player_score))

                        # write the scores to a file or to the server
                        # if high_score_server_enabled:
                        #    url = "http://{}/cgi-bin/chaseserver.py/?c=submit&name={}&score={}".format(
                        #             high_score_server_ip, self.player_name, player_score)
                        #     requests.get(url)
                        # else:
                        #     self.write_data()


                        # INSTEAD OF THIS, WRITE ANOTHER FUNCTION
                        # ---------------------------------------
                        # self.write_data()



                        # redraw the high score table
                        # self.redraw_score_group()

                        # switch out of high score mode and reset the player score
                        self.high_score_mode = False
                        player_score = 0

                    if (name_changed):
                        #if (len(self.player_name) > 12):
                        #    self.player_name = self.player_name[0:len(self.player_name) - 1]
                        self.redraw_player_name()

        else:
            # not in high score mode, just displaying the high scores
            self.button_group.update()

    def on_render(self, screen):
        # WHY BOTHERING WITH BACKGROUND IMAGE?
        # screen.blit(next_trial_image, self.parent.screen_rect)
        global backgroundColor

        # add background color
        # --------------------
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((backgroundColor))
        screen.blit(background, (0, 0))

        self.button_group.draw(screen)
        self.score_group.draw(screen)
        if (self.high_score_mode):
            # prompt player for their name
            self.player_name_prompt_group.draw(screen)

            global screen_width
            global screen_height
            # draw a box area where the player can type in their name
            # pygame.draw.rect(screen, Color("orange"), Rect(100, 520, 220, 32), 3)
            pygame.draw.rect(screen, Color("orange"),
                             Rect(screen_width / 2 - 110, (screen_height / 2) - 16, 220, 32), 3)
            # draw the player's name as they type it
            self.player_name_group.draw(screen)

    def redraw_player_name(self):
        self.player_name_group.empty()
        font = Font(pygame.font.get_default_font(), 24)
        player_name_sprite = Sprite(self.player_name_group)
        player_name_sprite.image = font.render(self.player_name, True, Color("white"))
        player_name_sprite.rect = Rect(0, 0, player_name_sprite.image.get_width(),
                                       player_name_sprite.image.get_height())
        player_name_sprite.rect.center = (game.screen_rect.width / 2,
                                          game.screen_rect.height / 2)

    def redraw_score_group(self):
        """Recreates all of the high score font renders. The sprite group is emptied
        and re-populated with new score sprites."""
        # empty the score sprite group
        self.score_group.empty()

        y = 64
        font = Font(pygame.font.get_default_font(), 24)
        for score in self.high_scores:
            string = score[0] + "   .   .   .   .   .   " + str(score[1])
            sprite = Sprite(self.score_group)
            sprite.image = font.render(string, True, Color("white"))
            sprite.rect = Rect(0, 0, sprite.image.get_width(), sprite.image.get_height())

            sprite.rect.midtop = (game.screen_rect.width / 2, y)
            y += 36


    # BackButton
    # ----------------------------------------------------------------
    class BackButton(TextButton):

        def __init__(self):
            TextButton.__init__(self, "Continue", 32)

        def on_click(self):
            global trialNumber
            global trialsTotal

            # go to the next trial
            trialNumber = trialNumber + 1
            if (trialNumber != trialsTotal):
                game.set_next_scene("trial")
            else:
                game.set_next_scene("end")
            game.current_scene.finished = True


# --------------------------------------------------------------------
# End Scene
# ====================================================================
class endScene(Scene):
    name = "end"

    global backgroundColor
    global fontColor

    def on_init(self):
        global screen_w
        global screen_h
        screen_w = game.screen.get_width()
        screen_h = game.screen.get_height()

        self.button_group = ButtonGroup()

        exit_button = self.ExitButton()
        exit_button.rect.bottomleft = (screen_w / 1.2, 536)
        self.button_group.add(exit_button)

    def on_cleanup(self):
        pass

    def on_update(self, delta, events):
        self.button_group.update()

    def on_render(self, screen):
        # Adding a background image on the main menu
        # ------------------------------------------

        # by activating the code below and defining "title_image"
        # you can add a background image. BUT THAT WON'T ALLOW YOU
        # to set the screen resolution without screwing the background

        # screen.blit(title_image, self.parent.screen_rect)

        # credit = "Developed by E. F. Haghish,  http://haghish.com/stat"
        # myFont = pygame.font.SysFont("monaco", 18)
        # screen.blit(myFont.render(credit, True, (200,200,200)), (0,0))

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((backgroundColor))
        screen.blit(background, (0, 0))

        credit = "Thank you for your participation"
        myFont = pygame.font.SysFont("monaco", 64)
        screen.blit(myFont.render(credit, True, Color(fontColor)), ((screen_width/2) -350 , 200))

        self.button_group.draw(screen)

    class ExitButton(TextButton):
        def __init__(self):
            TextButton.__init__(self, "EXIT", 32, color=Color(fontColor))

        def on_click(self):
            game.stop()


# Execute the game
# ===================================================================
if (__name__ == "__main__"):

    # 1. Load settings which changes some global variables
    load_settings()

    # 2. game screen
    game = Game(screen_width, screen_height, fullscreen=fullscreen)

    # 3. Load resources
    load_resources()

    # set the window icon and caption
    icon_path = os.path.join("resources/image/icon.png")
    pygame.display.set_icon(pygame.image.load(icon_path))
    pygame.display.set_caption("Chase")


    # initialize the game scenes
    menu_scene = game.add_scene(MenuScene)
    play_scene = game.add_scene(trialScene)
    end_scene = game.add_scene(endScene)
    detect_scene = game.add_scene(DetectScene)
    high_score_scene = game.add_scene(findWolf)
    ID_scene = game.add_scene(IDScene)

    random.seed() # seed the prng
    game.set_next_scene("ID")  #ID menu trial detect findwold end
    game.start() # start it up!












