import time, _thread

# Example Usage:
#
# from spinner import Spinner
# s = Spinner(tft)      # tft = display control object
# s.start()
# s.stop()

class Spinner(object):
    def __init__(self, tft):
        self.tft = tft
        self.green_arc = [0, 120] # Starting green arc angle
        self.grey_arc = [315, 0]  # Starting grey arc angle
        self.th = None            # Variable for thread id

    def _spin(self):
        while True:
            # Check for notification signals
            ntf =  _thread.getnotification()
            if ntf:
                if ntf == _thread.EXIT:
                    # ...if received EXIT signal, clear screen to black and exit thread
                    self.tft.clear(self.tft.BLACK)
                    return

            # Draw green and grey (following) arc
            self.tft.arc(160, 120, 20, 5, self.green_arc[0], self.green_arc[1], self.tft.GREEN, self.tft.GREEN)
            self.tft.arc(160, 120, 20, 5, self.grey_arc[0], self.grey_arc[1], self.tft.LIGHTGREY, self.tft.LIGHTGREY)
            # Tiny delay before continuing to keep the animation at a reasonable speed.
            time.sleep_ms(50)

            # Step arc angles forward (accounting for going from 360 back to 0 degrees)
            if (self.green_arc[0] + 45) <= 360:
                self.green_arc[0] += 45
            else:
                self.green_arc[0] = 45-(360-self.green_arc[0])
    
            if (self.green_arc[1] + 45) <= 360:
                self.green_arc[1] += 45
            else:
                self.green_arc[1] = 45-(360-self.green_arc[1])
    
            if (self.grey_arc[0] + 45) <= 360:
                self.grey_arc[0] += 45
            else:
                self.grey_arc[0] = 45-(360-self.grey_arc[0])
    
            if (self.grey_arc[1] + 45) <= 360:
                self.grey_arc[1] += 45
            else:
                self.grey_arc[1] = 45-(360-self.grey_arc[1])


    def stop(self):
        # Notify thread to EXIT
        _thread.notify(self.th, _thread.EXIT)

    def start(self):
        # Clear screen to black and start the spinner thread
        self.tft.clear(self.tft.BLACK)
        self.th = _thread.start_new_thread("SPINNER", self._spin, ())
