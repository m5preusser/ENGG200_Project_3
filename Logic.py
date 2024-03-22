#Logic.py
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
 
button_yes = None
button_no = None
button_off = None
path = None
spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))
temperature = ""

def main(self):
    
    button_yes = machine.Pin()
    button_no = machine.Pin()
    button_off = machine.Pin()

    question_1()
    
def button_input():
    wait = True
    response = ""
    
    while wait == True:

        if button_yes.value() != 1:
            wait = False
            response = "yes"
        if button_no.value() != 1:
            wait = False
            response = "no"
        if button_off.value() != 1:
            wait = False
            response = "off"

    return response

def display_text(text):
    display.clear()
    display.draw_text(0,0,text)


def question_1():

    question = "Nice to talk to you again! Are you feeling well today?"
    display_text(question)
    response = button_input()

    if response == "yes":
        path = "0"
        question_2()
    elif response == "no":
        path = "1"
        question_2()
    else:
        pass

def question_2():

    if path == "0":
        question = "Glad you're feeling alright! I've been working on some jokes, would you be interested in hearing one?"
        display_text(question)
        response = button_input()

        if response == "yes":
            path = "00"
            question_3()
        elif response == "no":
            path = "01"
            question_3()
        else:
            pass
    
    else:
        question = "I'm sorry to hear that today's not going great. I'd like to help, are you in any physical pain?"
        display_text(question)
        response = button_input()

        if response == "yes":
            path = "10"
            question_3()
        elif response == "no":
            path_level_1 = "11"
            question_3()
        else:
            pass


def question_3():
    
    if path == "00":
        question = ""
        display_text(question)
        response = button_input()

        if response == "yes":
            terminating_statement = ""
            display_text(terminating_statement)
        elif response == "no":
            terminating_statement = ""
            display_text(terminating_statement)
        else:
            pass
    
    elif path == "01":
        question = ""
        display_text(question)
        response = button_input()

        if response == "yes":
            terminating_statement = ""
            display_text(terminating_statement)
        elif response == "no":
            terminating_statement = ""
            display_text(terminating_statement)
        else:
            pass

    elif path == "10":
        question = "Would you describe your pain as a headache?"
        display_text(question)
        response = button_input()

        if response == "yes":
            question = "The current ambient temperature is " + temperature + " °C. Would you like to cool off?"
            display_text(question)
            response = button_input()

            if response == "yes":
                #turn on fan
                pass
            else:
                terminating_statement = "I would recommend having something to eat and drinking some water. Carbohydrates such as toast or bananas are best for digestion. If your headache persists, I would suggest you call a nurse for help"

        elif response == "no":
            question = ""
            display_text(terminating_statement)
        else:
            pass

    elif path == "11":
        question = ""
        display_text(question)
        response = button_input()

        if response == "yes":
            terminating_statement = ""
            display_text(terminating_statement)
        elif response == "no":
            terminating_statement = ""
            display_text(terminating_statement)
        else:
            pass

if __name__ == "__main__":
    main()
