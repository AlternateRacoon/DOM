from recognize import Recognize
from media_center import media_center_control, call_dom, connect_media_center
from greetings import greet_user
from search import search_wikipedia, read_news_headlines, joke, search_google, get_recipe
from get_song import play_song, play_video
from speak import Voice
from weather import get_weather
from users import create_user, get_all_users


import sys
import datetime
import os
import pygame
import datetime
import requests
import subprocess
import speech_recognition as sr

pygame.font.init()

currentDT = str(datetime.datetime.now())

Name = ""
Age = 0
Birthday = ""

Voice.speak_flite("Hello", "This Is Dom")
news_number = 2


def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


screen = pygame.display.set_mode([677, 530])

pygame.display.set_caption("DOM")

clock = pygame.time.Clock()

background_position = [0, 0]

myfont = pygame.font.SysFont('Bebas Neue', 40)

fontsmall = pygame.font.SysFont('Bebas Neue', 20)

fontbig = pygame.font.SysFont('Bebas Neue', 60)
# background_image = pygame.image.load("background.jpg")


done = True
r = sr.Recognizer()
speech = sr.Microphone()

while done:
    now = datetime.datetime.now()
    if int(now.strftime("%I")) <= 9:
        currenttime = now.strftime("%I:%M %p").replace("0", "", 1)
    else:
        currenttime = now.strftime("%I:%M %p")
    currentmonth = " " + now.strftime("%B")
    currentday = now.strftime("%A") + ","
    currentdaymonth = currentday + currentmonth

    monthday = myfont.render(currentdaymonth, False, (255, 255, 255))
    time = myfont.render(currenttime, False, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(time, [0, 0])
    screen.blit(monthday, [0, 50])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.display.flip()
    pygame.display.update()
    with speech as source:
        blit_text(screen, "Listening", (0, 100), fontbig, color=pygame.Color('green'))
        print("listening")
        pygame.display.flip()
        pygame.display.update()
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    screen.fill((0, 0, 0))
    screen.blit(time, [0, 0])
    screen.blit(monthday, [0, 50])
    print("recognizing")
    blit_text(screen, "Recognizing", (0, 100), fontbig, color=pygame.Color('green'))
    pygame.display.flip()
    pygame.display.update()
    try:
        recog = r.recognize_google(audio)
    except sr.UnknownValueError:
        recog = "Unable to recognize speech"
    if "Unable to recognize speech" not in recog:
        recog = recog.replace("Don", "Dom")
        if "I am" in recog:
            recog = recog.replace("Iron", "Ayaan")
    screen.fill((0, 0, 0))
    screen.blit(time, [0, 0])
    screen.blit(monthday, [0, 50])
    print(recog)
    if "Unable to recognize speech" not in recog:
        color = 'WHITE'
    else:
        color = 'RED'
    blit_text(screen, recog, (0, 100), fontbig, color=pygame.Color(color))
    pygame.display.flip()
    pygame.display.update()
    currentDT = datetime.datetime.now()
    if "Unable to recognize speech" not in recog:
        response = recog
        if "break" in response or "sleep" in response:
            Voice.speak_flite("dom is now going to sleep, call again by saying dom")
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            pygame.display.flip()
            pygame.display.update()
            while True:
                response = Recognize.get_recognize_google()
                print(response)
                if response == False:
                    pass
                elif "dom" in response.lower() or "start" in response:
                    Voice.speak_flite("Listening...")
                    break
        elif "shutdown" in response:
            os.system("poweroff")
        elif "reboot" in response:
            os.system("reboot")
        elif "play" in response or "start" in response:
            play_video(" ".join(response.split()[1:]))
        elif "time" in response:
            Voice.speak_flite(currenttime)
        elif "day" in response:
            Voice.speak_flite(currentdaymonth)
        elif "song" in response:
            play_video(" ".join(response.split()[1:]))
        elif "play song" in response or "start song" in response:
            play_video(" ".join(response.split()[2:]))
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
                            Voice.speak_flite("Hello There " + row[0] + ", Welcome Back")
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
