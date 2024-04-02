#Logic.py
from time import sleep
import Hardware

path = None
temperature = ""
time = ""

def question_1():

    question = "Nice to talk to you again! Are you feeling well today?"
    Hardware.display_text(question)
    Hardware.play_file()
    response = Hardware.button_input()

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
        Hardware.display_text(question)
        Hardware.play_file()
        response = Hardware.button_input()

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
        Hardware.display_text(question)
        Hardware.play_file()
        response = Hardware.button_input()

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
        question = "I always like telling jokes, here's one. Why don't skeletons fight each other? Becuase they don't have the guts! Would you like to hear another?"
        Hardware.display_text(question)
        Hardware.play_file()
        response = Hardware.button_input()

        if response == "yes":
            terminating_statement = "What's the last thing to go through a flies head before it hits the fly swatter? Its bum. Thanks for speaking with me today!"
            Hardware.display_text(terminating_statement)
            Hardware.play_file()
        elif response == "no":
            terminating_statement = "That's alright, one joke is enough for today. Thanks for the chat!"
            Hardware.display_text(terminating_statement)
            Hardware.play_file()
        else:
            pass
    
    elif path == "01":
        question = "That's alright, sometimes you're not in the mood for jokes. Would you like some current information?"
        Hardware.display_text(question)
        Hardware.play_file()
        response = Hardware.button_input()

        if response == "yes":
            terminating_statement = "It is currently " + time + " and the ambient temperature is " + temperature + "."
            Hardware.display_text(terminating_statement)
            Hardware.play_file()
        elif response == "no":
            terminating_statement = "I hope I provided some emotional support today. It's always good to talk to someone."
            Hardware.display_text(terminating_statement)
            Hardware.play_file()
        else:
            pass

    elif path == "10":
        question = "Would you describe your pain as a headache?"
        Hardware.display_text(question)
        Hardware.play_file()
        response = Hardware.button_input()

        if response == "yes":
            question = "The current ambient temperature is " + temperature + " °C. Would you like to cool off?"
            Hardware.display_text(question)
            Hardware.play_file()
            response = Hardware.button_input()

            if response == "yes":
                #turn on fan
                pass
            else:
                terminating_statement = "I would recommend having something to eat and drinking some water. Carbohydrates such as toast or bananas are best for digestion. If your headache persists, I would suggest you call a nurse for help"

        elif response == "no":
            terminating_statement = "If you're in any kind of significant anguish, I would highly reccomend calling a nurse. I am unfortunately limited in my ability to help physically."
            Hardware.display_text(terminating_statement)
            Hardware.play_file()
        else:
            pass

    elif path == "11":
        question = "That's good to hear at least. Are you in any emotional anguish?"
        Hardware.display_text(question)
        Hardware.play_file()
        response = Hardware.button_input()

        if response == "yes":
            terminating_statement = "Remember to drink and eat enough food and water throughout your day. That will help you keep your energy up!"
            Hardware.display_text(terminating_statement)
            Hardware.play_file()
        elif response == "no":
            terminating_statement = "I won't be able to help you with much else. If you need something, I would reccomend calling a nurse. If not, try calling some family, social interaction can help your mental health."
            Hardware.display_text(terminating_statement)
            Hardware.play_file()
        else:
            pass
