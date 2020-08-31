"""
Copyright (C) 2014  Jason Gosen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import pygame
from pygame.sprite import Group, Sprite
from pygame.font import Font
from pygame.locals import *


class ButtonGroup(Group):
    def update(self, *args):
        mouse_event = pygame.event.get(MOUSEBUTTONDOWN)
        if mouse_event:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            Group.update(self, mouse_x, mouse_y)


class Button(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.rect = Rect(0, 0, 0, 0)
    
    def update(self, mouse_x, mouse_y):
        if self.is_clicked(mouse_x, mouse_y):
            self.on_click()
    
    def is_clicked(self, mouse_x, mouse_y):
        """Returns True/False if the button had been clicked"""
        if (mouse_x >= self.rect.left
                and mouse_x <= self.rect.right
                and mouse_y >= self.rect.top
                and mouse_y <= self.rect.bottom):
            return True
        return False
    
    def on_click(self):
        """Called when the button had been clicked on."""
        pass


class TextButton(Button):
    def __init__(self, text, font_size, color=Color("white")):
        Button.__init__(self)
        #render text with default font
        self.font = Font(None, font_size)
        self.font_color = color
        self.image = self.font.render(text, True, self.font_color)
        self.rect = Rect(0, 0, self.image.get_width(), self.image.get_height())


class ImageButton(Button):
    def __init__(self, image):
        Button.__init__(self)
        self.image = image
        self.rect = Rect(0, 0, image.get_width(), image.get_height())
