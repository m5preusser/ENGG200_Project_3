import urequests
import time

def set_time():
    data = urequests.get('https://timeapi.io/api/Time/current/zone?timeZone=America/Edmonton')
    global hour_offset
    hour_offset = time.localtime()[3]
    global minute_offset
    minute_offset = time.localtime()[4]
    for key, value in data.json().items():
        if key == "hour":
            global set_hour
            set_hour = value
    for key, value in data.json().items():
        if key == "minute":
            global set_minute
            set_minute = value


def hour():
    return (time.localtime()[3] + set_hour - hour_offset + (time.localtime()[4] + set_minute - minute_offset) // 60) % 24
    
def minute():
    return (time.localtime()[4] + set_minute - minute_offset)%60   