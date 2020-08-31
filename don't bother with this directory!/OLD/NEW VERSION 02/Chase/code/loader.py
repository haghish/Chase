"""
The loader module contains functions for loading resource files into
the game. Resources are cached so subsequent loading is almost
instantaneous.
"""


import os
import pygame, code


#global resource cache
images = {}
sounds = {}


# Loading the resources
# ====================================================================
#
# the program loads several images and a sound from "res" subdirectory
# You can make changes to the game by altering these files! For
# description see the manual.

gameover_sound = None

def load_resources():
    from loader import load
    # Title image is used for the main manu
    # global title_image
    # title_image = code.loader.load("title.jpg")

    # global end_image
    # end_image = code.loader.load("title.jpg")


    # global next_trial_image
    # next_trial_image = code.loader.load("high-score.jpg")

    # loads the image file that has the background and players
    global players_sheet
    players_sheet = code.loader.load("background_players.png")

    # loads the sound for ending the trial (if lost)
    global gameover_sound

    if (gameover_sound == True):
        gameover_sound = code.loader.load("end.ogg")

def load(file_name):
    file_ext = file_name.split(".")[-1]
    if (file_ext == "jpg" or file_ext == "jpeg" or file_ext == "png" or file_ext == "bmp"):
        return load_image(file_name)
    elif file_ext == "ogg":
        return load_sound(file_name)


def load_image(file_name):
    """Load an image. Magenta is used as a color key."""
    cached_image = images.get(file_name, None)
    if cached_image:
        return cached_image
    
    file_path = os.path.join("resources/image/" + file_name)
    image = pygame.image.load(file_path)
    conv_image = image.convert()
    conv_image.set_colorkey(pygame.Color(255, 0, 255))
    #cache the image
    images[file_name] = conv_image
    return conv_image


def load_sound(file_name):
    cached_sound = sounds.get(file_name, None)
    if cached_sound:
        return cached_sound
    
    file_path = os.path.join("resources/sound/" + file_name)
    sound = pygame.mixer.Sound(file_path)
    #cache the sound
    sounds[file_name] = sound
    return sound
