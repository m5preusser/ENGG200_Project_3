import urequests
import time
import machine
import Setup


def set_time():
    global got_time 
    try:
        print('getting time')
        data = urequests.get('https://timeapi.io/api/Time/current/zone?timeZone=America/Edmonton')
        global hour_offset
        hour_offset = time.localtime()[3]
        global minute_offset
        minute_offset = time.localtime()[4]
        global second_offset
        second_offset = time.localtime()[5]

        items = data.json().items()

        for key, value in items:
            if key == "hour":
                global set_hour
                set_hour = value
            if key == "minute":
                global set_minute
                set_minute = value
            if key == "seconds":
                global set_second
                set_second = value
        
        print(f'{hour()}:{minute()}:{second()}')
        got_time = True

    except:
        print('issue getting current time')
        set_hour = 0
        set_minute = 0
        set_second = 0
        hour_offset = 0
        minute_offset = 0
        second_offset = 0
        got_time = False

    finally:
        try:
            data.close()
        except:
            print('cant close api')

def hour():
    return (time.localtime()[3] + set_hour - hour_offset + (time.localtime()[4] + set_minute - minute_offset + (time.localtime()[5] + set_second - second_offset) // 60) // 60) % 24
    
def minute():
    return (time.localtime()[4] + set_minute - minute_offset + (time.localtime()[5] + set_second - second_offset) // 60) % 60

def second():
    return (time.localtime()[5] + set_second - second_offset) % 60  