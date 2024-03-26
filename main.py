from machine import Pin
import time
import Hardware
import Setup
import get_time


def main():
    print('Main started')
    
    Setup.setup()
    Setup.connect()
    get_time.set_time()
    Hardware.light.clear()
    Hardware.light.show()

    while True:
        Hardware.display_text(Hardware.button_input())
        Hardware.display_time()
        if Hardware.get_darkness():
            Hardware.light_state(Hardware.get_motion())
        else:
            Hardware.light.clear()
            Hardware.light.show()
        time.sleep(0.1)



if __name__ == '__main__':
    try:
        main()
    except:
        Hardware.light.clear()
        Hardware.light.show()