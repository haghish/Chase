# Clock
# ===================================================================
#
# a clock too appear in the top-left of the screen counting number of 
# seconds since the beginning of the trial



from pygame.locals import *
from pygame.font import Font


class Clock(object):
    def __init__(self):
        self.time = 0
        self.last_time = "00:00"
        self.font = Font(None, 24)
        self.font_color = Color("blue")
        self.draw_clock_font(self.last_time)
        self.clock_image = None

    def update(self, delta):
        self.time += delta

    def draw(self, screen):
        minutes = "%02d" % int(self.time / 1000 / 60)
        seconds = "%02d" % int(self.time / 1000 % 60)
        time_string = minutes + ":" + seconds
        if not self.last_time == time_string:
            self.draw_clock_font(time_string)
        img_w = self.clock_img.get_width()
        img_h = self.clock_img.get_height()
        dest = Rect(32, 32, img_w, img_h)
        screen.blit(self.clock_img, dest)

    def draw_clock_font(self, time_string):
        self.clock_img = self.font.render(time_string, True, self.font_color)


