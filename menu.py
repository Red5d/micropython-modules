# Example usage:
#
# # Create a function to receive selected values from the menu
# def doSelection(value):
#     print(value)
#
# # Setup and display the menu
# m = menu.Menu(tft, tft.FONT_DejaVu18, doSelection)
# m.title = "Testing"
# m.items = ["One", "Two", "Three", "Four", "Five"]
# m.render()
#
# # Use the m5stack module Button functions to navigate the menu
# up = m5stack.ButtonA(callback=m.up)
# select = m5stack.ButtonB(callback=m.select)
# down = m5stack.ButtonC(callback=m.down)

class Menu(object):
    def __init__(self, tft, font, handler):
        self.title = ""
        self.items = []
        self.tft = tft
        self.font = font
        self.handler = handler
        self.max_x = 320
        self.max_y = 240
        self.box_y = 40
        self.selection = None
        self.item_bg = tft.LIGHTGREY
        self.item_border = tft.BLACK
        self.item_color = tft.BLACK
        self.title_bg = tft.BLACK
        self.title_border = tft.BLACK
        self.title_color = tft.WHITE
        self.sel_bg = tft.BLUE
        self.sel_border = tft.BLUE
        self.sel_color = tft.WHITE

    def draw_box(self, slot, text, background, border, text_color):
        self.tft.rect(0, self.box_y*slot, self.max_x, self.box_y, border, background)
        # Print the text in center (h/v) of box
        self.tft.text(self.tft.CENTER, int((self.box_y - self.tft.fontSize()[1]) / 2)+(slot*self.box_y), text, text_color)

    def render(self):
        # Set font and clear screen
        self.tft.font(self.font, transparent=True)
        self.tft.clear(self.item_bg)

        # Draw title bar
        self.draw_box(0, self.title, self.title_bg, self.title_border, self.title_color)

        # Draw menu items
        current_slot = 1
        for item in self.items:
            if current_slot <= (self.max_y / self.box_y):
                self.draw_box(current_slot, item, self.item_bg, self.item_border, self.item_color)

            current_slot += 1

    def up(self, pin, pressed):
        if pressed and (self.selection == None):
            # Select the first box
            self.selection = 0
            self.draw_box(self.selection+1, self.items[self.selection], self.sel_bg, self.sel_border, self.sel_color)
        elif pressed and (self.selection > 0):
            # Reset the currently selected box
            self.draw_box(self.selection+1, self.items[self.selection], self.item_bg, self.item_border, self.item_color)
            # Decrement selection and draw newly-selected box
            self.selection -= 1
            self.draw_box(self.selection+1, self.items[self.selection], self.sel_bg, self.sel_border, self.sel_color)
            
    def down(self, pin, pressed):
        if pressed and (self.selection == None):
            # Select the first box
            self.selection = 0
            self.draw_box(self.selection+1, self.items[self.selection], self.sel_bg, self.sel_border, self.sel_color)
        elif pressed and (self.selection+1) < (int(self.max_y / self.box_y)-1):
            # Reset the currently selected box
            self.draw_box(self.selection+1, self.items[self.selection], self.item_bg, self.item_border, self.item_color)
            # Increment selection and draw newly-selected box
            self.selection += 1
            self.draw_box(self.selection+1, self.items[self.selection], self.sel_bg, self.sel_border, self.sel_color)

    def select(self, pin, pressed):
        if pressed and (self.selection != None):
            # Run the handler function and pass the selected value to it
            self.handler(self.items[self.selection])
