from recognize import Recognize
from media_center import media_center_control,call_dom, connect_media_center
from greetings import greet_user
from search import search_wikipedia,read_news_headlines, joke, search_google, get_recipe
from get_song import play_song, play_video
from speak import Voice
from weather import get_weather
from users import create_user, get_all_users

import sys
import datetime
import os

currentDT = datetime.datetime.now()


Name = ""
Age = 0
Birthday = ""

Voice.speak_flite("Hello", "This Is Dom")
news_number = 1
while True:
    response = Recognize.get_recognize_google()
    print(response)
    if response == False:
        pass
    else:
        if "break" in response or "sleep" in response:
            call_dom()
        elif "shutdown" in response:
            os.system("poweroff")
        elif "reboot" in response:
            os.system("reboot")
        elif "play" in response or "start" in response:
            play_video(" ".join(response.split()[1:]))
        elif "time" in response:
            Voice.speak_flite(currentDT.strftime("%I:%M:%S %p"))
        elif "day today" in response:
            Voice.speak_flite(currentDT.strftime("%a, %b %d, %Y"))
        elif "song" in response:
            play_song(" ".join(response.split()[1:]))
        elif "play song" in response or "start song" in response:
            play_song(" ".join(response.split()[2:]))
        elif "stop" in response or "quit" in response or "exit" in response:
            Voice.speak_flite("Dom Is Now Exiting")
            sys.exit()
        elif "recipe for" in response or "recipe of" in response:
            info = get_recipe(" ".join(response.split()[2:]))
            Voice.speak_flite(info[0])
            Voice.speak_flite("You will need the following ingredients")
            for row in info[1]:
                Voice.speak_flite(row)
            for row in info[2]:
                Voice.speak_flite(row)
        elif "weather" in response:
            get_weather()
        elif "news" in response:
            if "next" in response:
                news_number += 1
                Voice.speak_flite(read_news_headlines(news_number))
            else:
                Voice.speak_flite(read_news_headlines(news_number))
        elif "joke" in response:
            random_joke = joke()
            Voice.speak_flite(random_joke[0])
            Voice.speak_flite(random_joke[1])
        elif "update yourself" in response:
            os.system("cd / && ./update.sh")
            sys.exit()
        elif "create user" in response:
            Voice.speak_flite("Say The Users Name You Want to Create")
            name = Recognize.get_recognize_google()
            Voice.speak_flite("Say The Users Age")
            age = Recognize.get_recognize_google()
            Voice.speak_flite("Say The Users Birthday")
            birthday = Recognize.get_recognize_google()
            Voice.speak_flite("Name, " + name + " Age, " + age + " Birthday, " + birthday)
            Voice.speak_flite("Are you sure you want to create this user")
            response = Recognize.get_recognize_google()
            print(response)
            if "yes" in response:
                Voice.speak_flite("Creating User")
                create_user(name, age, birthday)
        elif "I am" in response:
            for row in get_all_users():
                response_split = response.split()
                for index in response_split:
                    if row[0] == index:
                        Name = row[0]
                        Age = row[1]
                        Birthday = row[2]
                        if row[0] == "Zara":
                            Voice.speak_flite("Hello There Zarah, Welcome Back")
                        elif row[0] == "Ayaan":
                            Voice.speak_flite("Hello There Aion, Welcome Back")
                        else:
                            Voice.speak_flite("Hello There "+ row[0] +", Welcome Back")
        elif "what is my birthday" in response or "when is my birthday" in response:
            if Birthday:
                Voice.speak_flite("Your Birthday comes on " + Birthday)
            else:
                Voice.speak_flite("Please say who you are")
        elif "what is my age" in response:
            if Age:
                Voice.speak_flite("Your Age is " + str(Age))
            else:
                Voice.speak_flite("Please say who you are")
        elif "what is my name" in response:
            if Name:
                if Name == "Ayaan":
                    Voice.speak_flite("Your Name is Aion")
                elif Name == "Zara":
                    Voice.speak_flite("You Name is Zarah")
                else:
                    Voice.speak_flite("Your Name is " + Name)
            else:
                Voice.speak_flite("Please say who you are")
        else:
            check = greet_user(response)
            if not check:
                search = search_wikipedia(response)


                
