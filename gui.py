import datetime
import os
import sys

import pygame
import speech_recognition as sr
from get_song import play_video
from greetings import greet_user
from recognize import Recognize
from search import search_wikipedia, read_news_headlines, joke, get_recipe, translate_urdu_to_english, translate_english_to_urdu
from speak import Voice
from users import create_user, get_all_users
from weather import get_weather
from time import sleep

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
    position1 = (245, 200)
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
        blit_text(screen, "Listening", position1, fontbig, color=pygame.Color('green'))
        print("listening")
        pygame.display.flip()
        pygame.display.update()
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    screen.fill((0, 0, 0))
    screen.blit(time, [0, 0])
    screen.blit(monthday, [0, 50])
    print("recognizing")
    blit_text(screen, "Recognizing", position1, fontbig, color=pygame.Color('green'))
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
    if int(len(recog.split())) < 5:
        blit_text(screen, recog, position1, fontbig, color=pygame.Color(color))
    else:
        blit_text(screen, recog, (0, 200), fontbig, color=pygame.Color(color))
    pygame.display.flip()
    pygame.display.update()
    sleep(5)
    currentDT = datetime.datetime.now()
    if "Unable to recognize speech" not in recog:
        response = recog
        if "break" in response or "sleep" in response:
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen, "dom is now going to sleep, call again by saying dom", (0,200), fontbig,color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite("dom is now going to sleep, call again by saying dom")
            while True:
                response = Recognize.get_recognize_google()
                print(response)
                if response == False:
                    pass
                elif "dom" in response.lower() or "start" in response:
                    screen.fill((0, 0, 0))
                    screen.blit(time, [0, 0])
                    screen.blit(monthday, [0, 50])
                    blit_text(screen, "Listening...", (0, 200), fontbig,
                              color=pygame.Color("white"))
                    pygame.display.flip()
                    pygame.display.update()
                    Voice.speak_flite("Listening...")
                    break
        elif " + " in response or " - " in response or " x " in response or " / " in response:
            first = int(response.split()[0])
            second = int(response.split()[2])
            if " + " in response:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, str(first + second), (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(str(first + second))
            if " - " in response:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, str(first - second), (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(str(first - second))
            if " x " in response:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, str(first * second), (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(str(first * second))
            if " / " in response:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, str(first / second), (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(str(first / second))
        elif "what does" in response and "mean in English" in response:
            word = response.split()[2]
            english_word = translate_urdu_to_english(word)
            if "no word found" in english_word:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, "No Word Found", (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite("no word found")
            else:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, word + ' means "'+ english_word + '" in english', (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(word + " means "+ english_word + " in english")
        elif "what does" in response and "mean in Urdu" in response:
            word = response.split()[2]
            urdu_word = translate_english_to_urdu(word)
            if "no word found" in urdu_word:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, "No Word Found", (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite("no word found")
            else:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, word + ' means "'+ urdu_word + '" in urdu', (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(word + " means "+ urdu_word + " in urdu")
        elif "shutdown" in response:
            os.system("poweroff")
        elif "reboot" in response:
            os.system("reboot")
        elif "play" in response or "start" in response:
            vid_play = play_video(" ".join(response.split()[1:]))
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen,"Stopping Audio", (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite("Stopping Audio")
        elif "time" in response:
            if int(currentDT.strftime("%I")) <= 9:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(currentDT.strftime("%I:%M %p").replace('0', '', 1), "", (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(currentDT.strftime("%I:%M %p").replace('0', '', 1))
            else:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(currentDT.strftime("%I:%M %p"), "", (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(currentDT.strftime("%I:%M %p").replace('0', '', 1))
        elif "day today" in response:
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(currentDT.strftime("%A, %B %Y").replace('0', '', 1), "", (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite(currentDT.strftime("%Y, %B %Y").replace('0', '', 1))
        elif "song" in response:
            vid_play = play_video(" ".join(response.split()[1:]))
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen,"Stopping Audio", (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite("Stopping Audio")
        elif "play song" in response or "start song" in response:
            vid_play = play_video(" ".join(response.split()[2:]))
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen,vid_play, (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite(vid_play)
        elif "stop" in response or "quit" in response or "exit" in response:
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen,"Dom Is Now Exiting", (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite("Dom Is Now Exiting")
            sys.exit()
        elif "recipe for" in response or "recipe of" in response:
            info = get_recipe(" ".join(response.split()[2:]))
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen, info[0], (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite(info[0])
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen, "You will need the following ingredients", (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite("You will need the following ingredients")
            for row in info[1]:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, row, (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(row)   
            for row in info[2]:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, row, (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(row)
        elif "weather" in response:
            text = get_weather()
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen, text, (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite(text)
        elif "news" in response:
            if "next" in response:
                news_number += 1
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen,read_news_headlines(news_number), (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(read_news_headlines(news_number))
            else:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen,read_news_headlines(news_number), (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(read_news_headlines(news_number))
        elif "joke" in response:
            random_joke = joke()
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen, random_joke[0], (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite(random_joke[0])
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen, random_joke[1], (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite(random_joke[1])
        elif "update yourself" in response:
            os.system("cd / && ./update.sh")
            sys.exit()
        elif "create user" in response:
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen,"Say The Users Name You Want to Create", (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite("Say The Users Name You Want to Create")
            name = Recognize.get_recognize_google()
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen, "Say The Users Age", (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite("Say The Users Age")
            age = Recognize.get_recognize_google()
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen, "Say The Users Birthday", (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite("Say The Users Birthday")
            birthday = Recognize.get_recognize_google()
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen,"Name, " + name + " Age, " + age + " Birthday, " + birthday, (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite("Name, " + name + " Age, " + age + " Birthday, " + birthday)
            screen.fill((0, 0, 0))
            screen.blit(time, [0, 0])
            screen.blit(monthday, [0, 50])
            blit_text(screen, "Are you sure you want to create this user", (0, 200), fontbig,
                      color=pygame.Color("white"))
            pygame.display.flip()
            pygame.display.update()
            Voice.speak_flite("Are you sure you want to create this user")
            response = Recognize.get_recognize_google()
            print(response)
            if "yes" in response:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, "Creating User", (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
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
                            screen.fill((0, 0, 0))
                            screen.blit(time, [0, 0])
                            screen.blit(monthday, [0, 50])
                            blit_text(screen, "Hello There Zara, Welcome Back", (0, 200), fontbig,
                                      color=pygame.Color("white"))
                            pygame.display.flip()
                            pygame.display.update()
                            Voice.speak_flite("Hello There Zarah, Welcome Back")
                        elif row[0] == "Ayaan":
                            screen.fill((0, 0, 0))
                            screen.blit(time, [0, 0])
                            screen.blit(monthday, [0, 50])
                            blit_text(screen, "Hello There Ayaan, Welcome Back", (0, 200), fontbig,
                                      color=pygame.Color("white"))
                            pygame.display.flip()
                            pygame.display.update()
                            Voice.speak_flite("Hello There Aion, Welcome Back")
                        else:
                            screen.fill((0, 0, 0))
                            screen.blit(time, [0, 0])
                            screen.blit(monthday, [0, 50])
                            blit_text(screen, "Hello There " + row[0] + ", Welcome Back", (0, 200), fontbig,
                                      color=pygame.Color("white"))
                            pygame.display.flip()
                            pygame.display.update()
                            Voice.speak_flite("Hello There " + row[0] + ", Welcome Back")
        elif "what is my birthday" in response or "when is my birthday" in response:
            if Birthday:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, "Your Birthday Comes On" + Birthday, (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite("Your Birthday comes on " + Birthday)
            else:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, "Please Say Who You Are", (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite("Please say who you are")
        elif "what is my age" in response:
            if Age:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, "Your Age is" + str(Age), (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite("Your Age is" + str(Age))
            else:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, "Please Say Who You Are", (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite("Please say who you are")
        elif "what is my name" in response:
            if Name:
                if Name == "Ayaan":
                    screen.fill((0, 0, 0))
                    screen.blit(time, [0, 0])
                    screen.blit(monthday, [0, 50])
                    blit_text(screen, "Your Name is Ayaan", (0, 200), fontbig,
                              color=pygame.Color("white"))
                    pygame.display.flip()
                    pygame.display.update()
                    Voice.speak_flite("Your Name is Aion")
                elif Name == "Zara":
                    screen.fill((0, 0, 0))
                    screen.blit(time, [0, 0])
                    screen.blit(monthday, [0, 50])
                    blit_text(screen, "Your Name is Zara", (0, 200), fontbig,
                              color=pygame.Color("white"))
                    pygame.display.flip()
                    pygame.display.update()
                    Voice.speak_flite("Your Name is Zarah")
                else:
                    screen.fill((0, 0, 0))
                    screen.blit(time, [0, 0])
                    screen.blit(monthday, [0, 50])
                    blit_text(screen, "Your Name is "+ Name , (0, 200), fontbig,
                              color=pygame.Color("white"))
                    pygame.display.flip()
                    pygame.display.update()
                    Voice.speak_flite("Your Name is "+ Name)
            else:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, "Please Say Who You Are", (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite("Please Say Who You Are")
        else:

            check = greet_user(response)
            if check == False:
                search = response
                if "who is" in search or "who was" in search or "who are" in search or "what is" in search or "what was" in search or "history of" in search or "tell me about" in search or "how" in search or "why" in search or "when" in search:
                    screen.fill((0, 0, 0))
                    screen.blit(time, [0, 0])
                    screen.blit(monthday, [0, 50])
                    blit_text(screen, "Searching about " + " ".join(search.split()[2:]), (0, 200), fontbig,
                              color=pygame.Color("white"))
                    pygame.display.flip()
                    pygame.display.update()
                    Voice.speak_flite("Searching about " + " ".join(search.split()[2:]))
                    search = search_wikipedia(response)
                    screen.fill((0, 0, 0))
                    screen.blit(time, [0, 0])
                    screen.blit(monthday, [0, 50])
                    blit_text(screen, search, (100,0), pygame.font.SysFont('Bebas Neue', 30),
                              color=pygame.Color("white"))
                    pygame.display.flip()
                    pygame.display.update()
                    Voice.speak_flite(search)
            else:
                screen.fill((0, 0, 0))
                screen.blit(time, [0, 0])
                screen.blit(monthday, [0, 50])
                blit_text(screen, check, (0, 200), fontbig,
                          color=pygame.Color("white"))
                pygame.display.flip()
                pygame.display.update()
                Voice.speak_flite(check)

