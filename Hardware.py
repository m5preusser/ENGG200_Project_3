from time import sleep
import get_time
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
import tm1637

# Buttons
yes_button = Pin(0, Pin.IN, Pin.PULL_UP)
no_button = Pin(1, Pin.IN, Pin.PULL_UP)
off_button = Pin(2, Pin.IN, Pin.PULL_UP)

# Screen
spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))
broadway = XglcdFont('Broadway17x15.c', 17, 15)

# Clock
clock = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

def button_input():
    if yes_button.value() == 0:
        print('Yes Button Pressed')
        sleep(0.1)
        return 'yes'

    elif no_button.value() == 0:
        print('No Button pressed')
        sleep(0.1)
        return 'no'

    elif off_button.value() == 0:
        print('off button pressed')
        sleep(0.1)
        return 'off'

    else:
        return ''

def display_text(text: str):
    display.clear(color565(255, 255, 255))
    display.draw_text(0, 255, text, broadway, 0, background=color565(255, 255, 255), landscape=True)

def display_time():
    current_hour = get_time.hour()
    current_minute = get_time.minute()
    clock.numbers(current_hour, current_minute)
    print(f'{current_hour}:{current_minute}')
    pass

