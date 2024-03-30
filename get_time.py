import urequests
import time
import machine



def set_time():
    try:
        data = urequests.get('https://timeapi.io/api/Time/current/zone?timeZone=America/Edmonton')
        global hour_offset
        hour_offset = time.localtime()[3]
        global minute_offset
        minute_offset = time.localtime()[4]

        items = data.json().items()

        for key, value in items:
            if key == "hour":
                global set_hour
                set_hour = value
            if key == "minute":
                global set_minute
                set_minute = value
            

    except:
        print('issue getting current time')
        machine.soft_reset()
    finally:
        data.close()

def hour():
    return (time.localtime()[3] + set_hour - hour_offset + (time.localtime()[4] + set_minute - minute_offset) // 60) % 24
    
def minute():
    return (time.localtime()[4] + set_minute - minute_offset)%60   