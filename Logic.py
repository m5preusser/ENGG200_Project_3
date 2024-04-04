#Logic.py
import time
import get_time
import Hardware

def question_1():
    print("question 1")
    Hardware.display_time()
    paath = None
    question = "Nice to talk to you again! Are you feeling well today?"
    # Name this recording "recording_1"
    Hardware.display_text(question, "middle")
    Hardware.play_file("recording_1.wav")

    print("getting button input")
    waiting = True
    response = ""
    while waiting == True:
        response = Hardware.button_input()
        if response == "":
            waiting = True
            time.sleep(0.1)
        else:
            waiting = False

    if response == "yes":
        paath = "0"
        question_2(paath)
    elif response == "no":
        paath = "1"
        question_2(paath)
    else:
        pass

def question_2(paath):
    print("question 2")
    Hardware.display_time()
    paath = paath
    if paath == "0":
        question = "Glad you're feeling alright! I've been working on some jokes, would you be interested in hearing one?"
        # Name this recording "recording_2"
        Hardware.display_text(question, "middle")
        Hardware.play_file("recording_2.wav")

        print("getting button input")
        waiting = True
        while waiting == True:
            response = Hardware.button_input()
            if response == "":
                waiting = True
                time.sleep(0.1)
            else:
                waiting = False

        if response == "yes":
            paath = "00"
            question_3(paath)
        elif response == "no":
            paath = "01"
            question_3(paath)
        else:
            pass
    
    else:
        question = "I'm sorry to hear that today's not going great. I'd like to help, are you in any physical pain?"
        # Name this recording "recording_3"
        Hardware.display_text(question, "middle")
        Hardware.play_file("recording_3.wav")
        print("getting button input")
        waiting = True
        response = ""
        while waiting == True:
            response = Hardware.button_input()
            if response == "":
                waiting = True
                time.sleep(0.1)
            else:
                waiting = False

        if response == "yes":
            paath = "10"
            question_3(paath)
        elif response == "no":
            paath_level_1 = "11"
            question_3(paath)
        else:
            pass


def question_3(paath):
    print("question 3")
    Hardware.display_time()
    paath = paath
    if paath == "00":
        question = "I always like telling jokes, here's one. Why don't skeletons fight each other? Because they don't have the guts! Would you like to hear another?"
        # Name this recording "recording_4"
        Hardware.display_text(question, "middle")
        Hardware.play_file("recording_4.wav")

        waiting = True
        response = ""
        while waiting == True:
            response = Hardware.button_input()
            if response == "":
                waiting = True
                time.sleep(0.1)
            else:
                waiting = False

        if response == "yes":
            terminating_statement = "What's the last thing to go through a flies head before it hits the fly swatter? Its bum. Thanks for speaking with me today!"
            # Name this recording "recording_5"
            Hardware.display_text(terminating_statement, "middle")
            Hardware.play_file("recording_5.wav")
        elif response == "no":
            terminating_statement = "That's alright, one joke is enough for today.Thanks for the chat!"
            # Name this recording "recording_6"
            Hardware.display_text(terminating_statement, "middle")
            Hardware.play_file("recording_6.wav")
        else:
            pass
    
    elif paath == "01":
        question = "That's alright, sometimes you're not in the mood for jokes. Would you like some current information?"
        # Name this recording "recording_7"
        Hardware.display_text(question, "middle")
        Hardware.play_file("recording_7.wav")

        waiting = True
        response = ""
        while waiting == True:
            response = Hardware.button_input()
            if response == "":
                waiting = True
                time.sleep(0.1)
            else:
                waiting = False

        if response == "yes":
            temperature = Hardware.get_temp()
            Hardware.display_time()
            current_time = get_time()
            terminating_statement = "It is currently " + str(current_time) + " and the temperature is " + str(temperature) + "."
            # For this one, say "this is the current time and ambient temperature"
            # Name this recording "recording_8"
            Hardware.display_text(terminating_statement, "middle")
            Hardware.play_file("recording_8.wav")
        elif response == "no":
            terminating_statement = "I hope I provided some emotional support today. It's always good to talk to someone."
            # Name this recording "recording_9"
            Hardware.display_text(terminating_statement, "middle")
            Hardware.play_file("recording_9.wav")
        else:
            pass

    elif paath == "10":
        question = "Would you describe your pain as a headache?"
        # Name this recording "recording_10"
        Hardware.display_text(question, "middle")
        Hardware.play_file("recording_10.wav")

        waiting = True
        response = ""
        while waiting == True:
            response = Hardware.button_input()
            if response == "":
                waiting = True
                time.sleep(0.1)
            else:
                waiting = False

        if response == "yes":
            temperature = Hardware.get_temp()
            terminating_statement = "The current temperature is " + temperature + " °C. High temperatures can contribute to headahches, I reccomend you call a nurse to lower the temp in the room."
            # Name this recording "recording_11"
            Hardware.display_text(terminating_statement, "middle")
            Hardware.play_file("recording_11.wav")

        elif response == "no":
            terminating_statement = "If you're in any kind of significant anguish, I would highly reccomend calling a nurse. I am unfortunately limited in my ability to help physically."
            # Name this recording "recording_12"
            Hardware.display_text(terminating_statement, "middle")
            Hardware.play_file("recording_12.wav")
        else:
            pass

    elif paath == "11":
        question = "That's good to hear at least. Are you in any emotional anguish?"
        # Name this recording "recording_13"
        Hardware.display_text(question, "middle")
        Hardware.play_file("recording_13.wav")

        waiting = True
        response = ""
        while waiting == True:
            response = Hardware.button_input()
            if response == "":
                waiting = True
                time.sleep(0.1)
            else:
                waiting = False

        if response == "yes":
            terminating_statement = "Remember to drink and eat enough food and water throughout your day. That will help you keep your energy up!"
            # Name this recording "recording_14"
            Hardware.display_text(terminating_statement, "middle")
            Hardware.play_file("recording_14.wav")
        elif response == "no":
            terminating_statement = "I won't be able to help you with much else. If you need something, you should call a nurse. If not, try calling some family, social interaction can help your mental health."
            # Name this recording "recording_15"
            Hardware.display_text(terminating_statement, "middle")
            Hardware.play_file("recording_15.wav")
        else:
            pass
