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
    

    while True:
        Hardware.display_text(Hardware.button_input())
        Hardware.display_time()
        time.sleep(0.1)


if __name__ == '__main__':
    main()
