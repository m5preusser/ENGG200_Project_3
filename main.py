from machine import Pin
import time
import Hardware



def main():
    print('Main started')
    
    Hardware.display_text('hello world')

    while True:
        Hardware.display_text(Hardware.button_input())
        time.sleep(0.1)


if __name__ == '__main__':
    main()
