from machine import Pin, Timer
import time
import Setup
import get_time
import machine
import Logic
from ili9341 import color565


# runs on start up
def boot():
    print('Main started')
    Hardware.display.clear(color565(255, 255, 255))                 # Clear display to white
    Setup.setup()                                                   # Connect to internet
    Setup.connect()                                                 # Connect to internet
    get_time.set_time()                                             # Get current time
    Hardware.display_text(f'{Hardware.get_temp()}C', 'top right')   # Get temperature and display in top right of the screen


# runs every 0.2 seconds
def loop():
    Hardware.display_time()

    # checks to see if it is dark
    if Hardware.get_darkness():
        Hardware.light_state(Hardware.get_motion())
        Hardware.clock.brightness(1)
        Hardware.display.display_off()
    else:
        Hardware.light.clear()
        Hardware.light.show()
        Hardware.clock.brightness(7)
        Hardware.display.display_on()

    if Hardware.button_no() == 1:
        Logic.question_1()
    
    # Displays temperature every ten minutes
    if (get_time.minute() % 10) == 0 and get_time.second() == 0:
        Hardware.display_text(Hardware.get_temp(), 'top right')
    

import Hardware

if __name__ == '__main__':
    try:
        boot()
        while True:
            loop()
            time.sleep(0.2)

    except:
        print('program end')
        Hardware.light.clear()
        Hardware.light.show()
        Hardware.player.stop()
        # machine.reset()
