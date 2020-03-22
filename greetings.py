import datetime
import re
import urllib.request

from speak import Voice

html_data = urllib.request.urlopen("https://www.fluentu.com/blog/english/english-greetings-expressions/").read().decode(
    "utf-8")

unfiltered_greetings = re.findall("<h3>(.*?)</h3>", html_data)

greetings = []


for row in unfiltered_greetings:
    greeting = re.findall("<b>(.*?)</b>", row)
    if greeting:
        for number in range(1, 17):
            greeting[0] = greeting[0].replace(str(number) + '.', '')
        greetings.append(greeting)

greetings = greetings[:-7]
for index in range(len(greetings)):
    for row in range(len(greetings[index])):
        greetings[index][row] = greetings[index][row].lower()
        greetings[index][row] = greetings[index][row].replace("what’s", "whats")
        greetings[index][row] = greetings[index][row].replace("how’s", "how is")
        greetings[index][row] = greetings[index][row].replace("it’s", "it is")
        greetings[index][row] = greetings[index][row].replace("?", "")

def greet_user(response):
    response = response.lower()
    check = False
    if response:
        for row in greetings[0]:
            if response in row:
                check = True
                Voice.speak_flite("Hello I am Dom", "Nice To meet You")
                return check
        for row in greetings[1]:
            if response in row:
                check = True
                Voice.speak_flite("I am Fine", "How About You?")
                return check
        for row in greetings[2]:
            if response in row:
                check = True
                Voice.speak_flite("Nothing much")
                return check
        for row in greetings[3]:
            if response in row:
                check = True
                Voice.speak_flite("Everything is fine")
                return check
        for row in greetings[4]:
            if response in row:
                check = True
                Voice.speak_flite("My Day is Just Fine")
                return check
                    
        for row in greetings[-2]:
            if response in row:
                check = True
                Voice.speak_flite("Nice to Meet you too")
                return check
        if "how have you been" in response:
            check = True
            Voice.speak_flite("I have been fine", "how about you")
            return check
        if "morning" in response or "afternoon" in response or "evening" in response:
            check = True
            hour = datetime.datetime.now().hour
            greeting = "Its morning", "Good morning" if 5 <= hour < 12 else "Its Afternoon", "Good afternoon" if hour < 18 else "Its Evening", "Good evening"
            Voice.speak_flite(greeting)
            return check
        if "hello" in response:
            check = True
            Voice.speak_flite("Hello I am Dom", "Nice To meet You")
            return check
        if "how are you" in response:
            check = True
            Voice.speak_flite("I have been fine", "what about you")
            return check
        if "fine" in response:
            check = True
            if "i am" in response:
                Voice.speak_flite("Good To Know")
                return check
            if "are you" in response:
                Voice.speak_flite("Yes I am Fine")
                return check
        if "ok" in response:
            check = True
            if "i am" in response:
                Voice.speak_flite("Good To Know")
                return check
            if "are you" in response:
                Voice.speak_flite("Yes I am Fine")
                return check
        if "who are you" in response:
            check = True
            Voice.speak_flite("I am Dom", "Dom stands for Data Operating Module")
            return check
        if "who made you" in response:
            Voice.speak_flite("I am Just A Home Project")
            return check
        if not check:
            return False
