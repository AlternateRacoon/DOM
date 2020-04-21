from recognize import Recognize
from media_center import media_center_control,call_dom, connect_media_center
from greetings import greet_user
from search import search_wikipedia,read_news_headlines, joke, search_google, get_recipe, translate_urdu_to_english, translate_english_to_urdu
from get_song import play_song, play_video
from speak import Voice
from weather import get_weather
from users import create_user, get_all_users
from time import sleep

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
        elif "what does" in response and "mean in English" in response:
            word = response.split()[2]
            english_word = translate_urdu_to_english(word)
            if "no word found" in english_word:
                Voice.speak_flite("no word found")
            else:
                Voice.speak_flite(word + " means "+ english_word + " in english")
        elif " + " in response or " - " in response or " x " in response or " / " in response:
            first = int(response.split()[0])
            second = int(response.split()[2])
            if " + " in response:
                Voice.speak_flite(str(first + second))
            if " - " in response:
                Voice.speak_flite(str(first - second))
            if " x " in response:
                Voice.speak_flite(str(first * second))
            if " / " in response:
                Voice.speak_flite(str(first / second))
        elif "what does" in response and "mean in Urdu" in response:
            word = response.split()[2]
            urdu_word = translate_english_to_urdu(word)
            if "no word found" in urdu_word:
                Voice.speak_flite("no word found")
            else:
                Voice.speak_flite(word + " means "+ urdu_word + " in urdu")
        elif "shutdown" in response:
            os.system("poweroff")
        elif "reboot" in response:
            os.system("reboot")
        elif "g u i" in response:
            os.system("dom")
            sys.exit()
        elif "play" in response or "start" in response:
            vid_play = play_video(" ".join(response.split()[1:]))
            speak = Voice.speak_flite(vid_play)
        elif "time" in response:
            if int(currentDT.strftime("%I")) <= 9:                
                Voice.speak_flite(currentDT.strftime("%I:%M %p").replace('0','',1))
            else:
                Voice.speak_flite(currentDT.strftime("%I:%M %p"))
        elif "day today" in response:
            Voice.speak_flite(currentDT.strftime("%A, %B, %Y"))
        elif "song" in response:
            vid_play = play_video(" ".join(response.split()[1:]))
            speak = Voice.speak_flite(vid_play)
        elif "play song" in response or "start song" in response:
            vid_play = play_video(" ".join(response.split()[2:]))
            speak = Voice.speak_flite(vid_play)
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
            text = get_weather()
            Voice.speak_flite(text)
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
            if check == False:
                search = response
                if "who is" in search or "who was" in search or "who are" in search or "what is" in search or "what was" in search or "history of" in search or "tell me about" in search or "how" in search or "why" in search or "when" in search:
                    Voice.speak_flite("Searching about "+ " ".join(search.split()[2:]))
                    search = search_wikipedia(response)
                    Voice.speak_flite(search)
            else:
                Voice.speak_flite(check)

                
