from recognize import Recognize
from media_center import media_center_control,call_dom, connect_media_center
from greetings import greet_user
from search import search_wikipedia,read_news_headlines, joke, search_google
from get_song import play_song, play_video
from speak import Voice
from weather import get_weather
from users import create_user, get_all_users

import sys
import logging
import datetime

currentDT = str(datetime.datetime.now())

logging.basicConfig(filename="dom_log.log", level=logging.INFO)

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
        if Name:
            logging.info('[INFO] '+ Name +' said '+ response +'at '+ currentDT)
        else:
            logging.info('[INFO] (unidentified user) said ' + response + 'at ' + currentDT)
        if "break" in response or "sleep" in response:
            call_dom()
        elif "play" in response or "start" in response:
            play_video(" ".join(response.split()[1:]))
        elif "song" in response:
            play_song(" ".join(response.split()[1:]))
        elif "play song" in response or "start song" in response:
            play_song(" ".join(response.split()[2:]))
        elif "stop" in response or "quit" in response or "exit" in response:
            Voice.speak_flite("Dom Is Now Exiting")
            sys.exit()
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
                if not search: 
                    if "how" in response or "when" in response or "why" in response or "is" in response:
                        Voice.speak_flite(search_google(response))

                
