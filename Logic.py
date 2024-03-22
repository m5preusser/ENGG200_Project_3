#Logic.py
from machine import Pin
 
button_yes = None
button_no = None
button_off = None
path = None

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
    pass

def question_1():

    question = ""
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
        question = ""
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
        question = ""
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
