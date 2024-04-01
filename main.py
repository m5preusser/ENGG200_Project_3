from machine import Pin, Timer
import time
import Setup
import get_time
import machine
import Logic


def boot():
    print('Main started')

    Setup.setup()
    Setup.connect()
    get_time.set_time()
    Hardware.display_text(f'{Hardware.get_temp()}C', 'top right')
    Logic.question_1()


    


def loop():
    Hardware.display_time()

    if Hardware.get_darkness():
        Hardware.light_state(Hardware.get_motion())
        Hardware.clock.brightness(1)
        Hardware.display.display_off()

    else:
        Hardware.light.clear()
        Hardware.light.show()
        Hardware.clock.brightness(7)
        Hardware.display.display_on()

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