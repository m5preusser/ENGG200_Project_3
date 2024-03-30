from machine import Pin, Timer
import time
import Hardware
import Setup
import get_time



def main():
    print('Main started')

    Setup.setup()
    Setup.connect()
    get_time.set_time()

    while True:
        loop()
        time.sleep(0.2)

    

def loop():
    print('looping')
    Hardware.log('looping')
    Hardware.display_text(Hardware.button_input(), 'top left')
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

    if (get_time.minute() % 60) == 0:
        pass

if __name__ == '__main__':
    try:
        main()
    except:
        Hardware.light.clear()
        Hardware.light.show()