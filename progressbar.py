# Example Usage:
#
# from progressbar import ProgressBar
# p = ProgressBar(30, 30, 150, 20)
# p.add(20)
# p.set(60)
# p.subtract(10)

class ProgressBar(object):
    def __init__(self, tft, x, y, width, height, border_width=2):
        self.tft = tft
        self.border_color = tft.BLACK
        self.bar_color = tft.GREEN
        self.bar_background = tft.WHITE
        self.progress = 0
        self.border_width = border_width
        self.x = x
        self.y = y
        self.bar_x = x+border_width
        self.bar_y = y+border_width
        self.bar_width = (width - (border_width * 3))
        self.bar_height = (height - (border_width * 3))

        # Draw bar outline
        borders = 0
        current_width = width - 2
        current_height = height - 2
        while borders < self.border_width:
            tft.rect(x+borders, y+borders, current_width, current_height, self.border_color)
            borders += 1
            current_width -= 2
            current_height -= 2

        # Draw bar background
        tft.rect(self.bar_x, self.bar_y, self.bar_width, self.bar_height, self.bar_background, self.bar_background)

    def set(self, percent):
        if percent <= 100:
            if percent < self.progress:
                # If bar is moving backward, redraw the background before updating the bar
                self.tft.rect(self.bar_x, self.bar_y, self.bar_width, self.bar_height, self.bar_background, self.bar_background)

            self.progress = percent
            self.tft.rect(self.bar_x, self.bar_y, int(self.bar_width*(percent/100)), self.bar_height, self.bar_color, self.bar_color)

    def add(self, percent):
        if (self.progress+percent) <= 100:
            self.set(self.progress+percent)
        else:
            self.set(100)

    def subtract(self, percent):
        if (self.progress-percent) >= 0:
            self.set(self.progress-percent)
        else:
            self.set(0)
