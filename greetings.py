import datetime
import re
import urllib.request

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
                return "Hello I am Dom, Nice To meet You"
        for row in greetings[1]:
            if response in row:
                check = True
                return "I am Fine, How About You?"
        for row in greetings[2]:
            if response in row:
                check = True
                return "Nothing much"
        for row in greetings[3]:
            if response in row:
                check = True
                return "Everything is fine"
        for row in greetings[4]:
            if response in row:
                check = True
                return "My Day is Just Fine"
        for row in greetings[-2]:
            if response in row:
                check = True
                return "Nice to Meet you too"
        if "how have you been" in response:
            check = True
            return "I have been fine, how about you"
        if "morning" in response or "afternoon" in response or "evening" in response:
            check = True
            hour = datetime.datetime.now().hour
            greeting = "Its morning", "Good morning" if 5 <= hour < 12 else "Its Afternoon", "Good afternoon" if hour < 18 else "Its Evening", "Good evening"
            return greeting
        if "hello" in response:
            check = True
            return "Hello I am Dom, Nice To meet You"
        if "how are you" in response:
            check = True
            return "I have been fine, what about you"
        if "fine" in response:
            if "i am" in response:
                check = True
                return "Good To Know"
            if "are you" in response:
                check = True
                return "Yes I am Fine"
        if "ok" in response:
            if "i am" in response:
                check = True
                return "Good To Know"
            if "are you" in response:
                check = True
                return "Yes I am Fine"
        if "who are you" in response:
            check = True
            return "I am Dom, Dom stands for Data Operating Module"
        if "who made you" in response:
            check = True
            return "I am Just A Home Project"
        if not check:
            return False
