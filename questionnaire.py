# Question Tree File

class Questionnaire:

    def questionnaire(button_yes, button_no):
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
