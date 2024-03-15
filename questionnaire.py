# Question Tree File

button_yes = None
button_no = None
button_off = None 

def __init__(self, button_1, button_2, button_3):
    button_yes = button_1
    button_no = button_2
    button_off = button_3

def questionnaire():
    pass
    #Goes through the questionnaire tree

def button_input(button_yes, button_no):
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
    
