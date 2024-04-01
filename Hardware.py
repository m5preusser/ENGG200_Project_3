from time import sleep
import get_time
from ili9341 import Display, color565
from machine import Pin, SPI, ADC
import machine
from xglcd_font import XglcdFont
import tm1637
from dht import DHT11, InvalidChecksum
from neopixel import Neopixel
import sdcard
import os
from wavePlayer import wavePlayer

# Buttons
yes_button = Pin(11, Pin.IN, Pin.PULL_UP)
no_button = Pin(12, Pin.IN, Pin.PULL_UP)
off_button = Pin(13, Pin.IN, Pin.PULL_UP)

# Screen
spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(6), cs=Pin(2), rst=Pin(7))
times_new_roman = XglcdFont('Times_New_Roman60x62.c', 34, 36)


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

# SD Card reader
sd = sdcard.SDCard((SPI(0, baudrate=60000000, sck=Pin(2), mosi=Pin(19), miso=Pin(16))), Pin(17))
vfs = os.VfsFat(sd)
os.mount(sd, '/sd')
print(os.listdir('/sd'))

# Speaker
player = wavePlayer()

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

def display_text(_text, _position: str):
    try:
        text = str(_text)
        position = {'top left': (0, 320), 'top right': (0, times_new_roman.measure_text(text))}
        display.clear(color565(255, 255, 255))
        display.draw_text(position[_position][0], position[_position][1], text, times_new_roman, 0, background=color565(255, 255, 255), landscape=True)
    except:
        print('issue at screen')
        machine.soft_reset()


def display_time():
    try:
        current_hour = get_time.hour()
        current_minute = get_time.minute()
        clock.numbers(current_hour, current_minute)
    except:
        print('issue at clock')
        machine.soft_reset()
        

def get_temp():
    try:
        thermometer.measure()
        return thermometer.temperature
    except:
        print('issue with temp sensor')
        return 22.1

def get_humidity():
    try:
        thermometer.measure()
        return thermometer.humidity
    except:
        print('issue with temp sensor')
        return 52

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
    

def play_file(track):
    try:
        print(f'/sd/{track}')
        player.play(f'/sd/{track}')
    except:
        print('issue playing sound')
        player.close()

    