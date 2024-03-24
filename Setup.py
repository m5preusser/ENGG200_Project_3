import ubinascii
import time
import machine
import network

ssid = 'airuc-guest' # This should be ‘airuc-guest’ on campus Wi-Fi

def setup():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    print(mac)

def connect():
    print('connecting to internet')
    try:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid) # Remove password if using airuc-guest

        while wlan.isconnected() == False:
            print('Waiting for connection...')
            time.sleep(1)
    except KeyboardInterrupt:
        machine.reset()
    
    if wlan.isconnected():
        print('connected')
        global ip
        ip = wlan.ifconfig()[0]
    else:
        print('not connected')
