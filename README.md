# micropython-modules

The GUI modules menu.py, spinner.py, and progressbar.py require the "display" module in this MicroPython variant that has specific support for the M5Stack and its display.
https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo

#### See the top of each file for example usage.

### bestwifi.py
Use this to have your device connect to the wifi network with the best signal strength from a list of networks and associated passwords. 

### menu.py
Displays an interactive menu interface on the screen with the specified title and (currently) up to 5 selectable options.

### spinner.py
Displays a (currently fullscreen) loading spinner animation that runs in a background thread so you can have it spinning while your code is loading or running other operations that require waiting.

### progressbar.py
Displays a progressbar on the screen at the specified coordinates and dimensions. Once it's created/displayed, you can adjust the progress percentage display in either absolute or relative values.
