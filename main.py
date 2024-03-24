from machine import Pin
import time

yes_button = Pin(0, Pin.IN, Pin.PULL_UP)
no_button = Pin(1, Pin.IN, Pin.PULL_UP)
off_button = Pin(2, Pin.IN, Pin.PULL_UP)
led1 = Pin("LED", Pin.OUT)


def main():
    print('Main started')

    while True:
        if yes_button.value() == 0:
            print('Yes Button Pressed')
        if no_button.value() == 0:
            print('No Button pressed')
        if off_button.value() == 0:
            print('off button pressed')

        led1.value(True)
        time.sleep(1)
        led1.value(False)


if __name__ == '__main__':
    main()
