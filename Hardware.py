from time import sleep
import get_time
from ili9341 import Display, color565
from machine import Pin, SPI, ADC
from xglcd_font import XglcdFont
import tm1637
from dht import DHT11, InvalidChecksum
from neopixel import Neopixel

# Buttons
yes_button = Pin(12, Pin.IN, Pin.PULL_UP)
no_button = Pin(1, Pin.IN, Pin.PULL_UP)
off_button = Pin(2, Pin.IN, Pin.PULL_UP)

# Screen
spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))
broadway = XglcdFont('Broadway17x15.c', 17, 15)

# Clock
clock = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

# thermometer
thermometer = DHT11(Pin(22))

# Motion Sensor
motion_sensor = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Photoresistor
photoresitor = ADC(27)

# LED ring
light = Neopixel(8, 0, 0, 'GRB')
white = (233, 224, 201)


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
    pass

def get_temp():
    thermometer.measure()
    return thermometer.temperature

def get_humidity():
    thermometer.measure()
    return thermometer.humidity

def get_motion():
    if motion_sensor.value() == 1:
        return True
    
    else:
        return False
    
def light_state(state: bool):
    if state:
        light.fill(white)
        light.show()
    
    else:
        light.clear()
        light.show()

def get_darkness():
    if photoresitor.read_u16() > 750:
        return True
    else:
        return False