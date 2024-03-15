# questionnaire.py file

class Questionnaire:

    def questionnaire(self):

        button_yes = machine.Pin(1,machine.Pin.IN, machine.Pin.PULL_UP)
        button_no = machine.Pin(1,machine.Pin.IN, machine.Pin.PULL_UP)

    def question_1(button_yes, button_no):
        # Prints question to screen
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
                # Print to screen "off"

        return response
    
