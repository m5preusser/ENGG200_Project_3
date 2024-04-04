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
times_new_roman = XglcdFont('Times_New_Roman19x20.c', 34, 36)


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

    '''
    takes no argument
    returns which button is being pressed as a string:
    'yes' for the yes button
    'no' for the no button
    'off' for the off button
    '' for no button pressed
    '''

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

    '''
    Arguments
        _text: the text to be display. Does not need to be a string as it gets converted, but needs to able to be converted to a string
        _position: str. 'top right' 'top left' 'middle'
        prints 'issue at screen' on error
    '''

    try:
        text = str(_text)
        lines = split_text(text)
        position = {'top left': (0, 320), 
                    'top right': (0, times_new_roman.measure_text(text)),
                    'middle': (45, 320)}
        for line in lines:
            display.draw_text(position[_position][0], position[_position][1], line, times_new_roman, 0, background=color565(255, 255, 255), landscape=True)
            # display.draw_text8x8(position[_position][0], position[_position][1], text, background=color565(255,255,255), rotate=90)
    except:
        print('issue at screen')

def split_text(text: str):
    sentence = text.split(' ')
    new_text = ['']

    i = 0
    for word in sentence:
        if times_new_roman.measure_text(f'{new_text[i]} {word}') < 320:
            if new_text[i] == '':
                new_text[i] = word
            else:
                new_text[i] = f'{new_text[i]} {word}'
        else:
            i = i + 1
            new_text.append(word)

    return new_text


def display_time():
    try:
        current_hour = get_time.hour()
        current_minute = get_time.minute()
        clock.numbers(current_hour, current_minute)
    except:
        print('issue at clock')
        # machine.soft_reset()
        

def get_temp():
    try:
        thermometer.measure()
        return thermometer.temperature
    except:
        print('issue with temp sensor')
        return 20.5

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
    

def play_file(track: str):

    '''
    Argument: the name of the file without the file extension. 
    File must be saved to the SD card and be a 16 bit, 8000 Sample Rate, mono wav file.
    To play 'Sample.wav', call 'play_file(Sample)'
    '''

    try:
        print(f'/sd/{track}')
        player.play(f'/sd/{track}')
    except:
        print('issue playing sound')
        player.close()

    
