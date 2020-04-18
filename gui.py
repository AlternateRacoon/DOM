import pygame
import datetime
import requests
from search import read_news_headlines
import subprocess
import speech_recognition as sr

pygame.init()

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

screen = pygame.display.set_mode([677,530])

pygame.display.set_caption("DOM")

clock = pygame.time.Clock()

background_position = [0,0]

myfont = pygame.font.SysFont('Bebas Neue', 40)

fontsmall = pygame.font.SysFont('Bebas Neue', 20)

fontbig = pygame.font.SysFont('Bebas Neue', 60)
#background_image = pygame.image.load("background.jpg")

news = "-" + read_news_headlines(2)
news1 = "-" + read_news_headlines(3)
news2 = "-" + read_news_headlines(4)

done = True
r = sr.Recognizer()
speech = sr.Microphone()


while done:
    temp = "C.P.U Temprature: "+ subprocess.check_output("cputemp -f n", shell=True).decode("utf8").replace("\n","")
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Karachi&APPID=07bbb96304be02263bcfa5534021d1c6")
    x = response.json()
    y = x["main"]
    current_temperature = y["temp"]
    current_humidity = y["humidity"]
    z = x["weather"]
    temprature = str(int(current_temperature - 273.15)) + "°C"
    now = datetime.datetime.now()
    if int(now.strftime("%I")) <= 9:
        currenttime = now.strftime("%I:%M %p").replace("0","",1)
    else:
        currenttime = now.strftime("%I:%M %p")
    currentmonth = " "+ now.strftime("%B")
    currentday = now.strftime("%A") + ","
    currentdaymonth = currentday + currentmonth

    monthday = myfont.render(currentdaymonth, False, (255,255,255))
    time = myfont.render(currenttime, False, (255, 255, 255))
    weather = myfont.render("Temprature Outside: "+ temprature, False, (255, 255, 255))
    cpu_temp = myfont.render(temp, False, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(time, [0, 0])
    screen.blit(monthday, [0,50])
    screen.blit(weather, [300,0])
    screen.blit(cpu_temp, [270, 50])
    blit_text(screen, "Latest News Headlines:", (0,250),myfont)
    blit_text(screen, news, (10, 300), fontsmall)
    blit_text(screen, news1, (10, 375), fontsmall)
    blit_text(screen, news2, (10, 450), fontsmall)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.display.flip()
    pygame.display.update()
    with speech as source:
        blit_text(screen, "Listening", (0,100), fontbig, color=pygame.Color('green'))
        print("listening")
        pygame.display.flip()
        pygame.display.update()
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    screen.fill((0, 0, 0))
    screen.blit(time, [0, 0])
    screen.blit(monthday, [0,50])
    screen.blit(weather, [300,0])
    screen.blit(cpu_temp, [270, 50])
    blit_text(screen, "Latest News Headlines:", (0, 250), myfont)
    blit_text(screen, news, (10, 300), fontsmall)
    blit_text(screen, news1, (10, 375), fontsmall)
    blit_text(screen, news2, (10, 450), fontsmall)
    print("recognizing")
    blit_text(screen, "Recognizing", (0,100), fontbig, color=pygame.Color('green'))
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
    screen.blit(monthday, [0,50])
    screen.blit(weather, [300,0])
    screen.blit(cpu_temp, [270, 50])
    blit_text(screen, "Latest News Headlines:", (0, 250), myfont)
    blit_text(screen, news, (10, 300), fontsmall)
    blit_text(screen, news1, (10, 375), fontsmall)
    blit_text(screen, news2, (10, 450), fontsmall)
    print(recog)
    if "Unable to recognize speech" not in recog:
        color = 'WHITE'
    else:
        color = 'RED'
    blit_text(screen, recog, (0, 100), fontbig, color=pygame.Color(color))
    pygame.display.flip()
    pygame.display.update()