from recognize import Recognize
from media_center import media_center_control,call_dom, connect_media_center
from greetings import greet_user
from search import search_wikipedia,read_news_headlines, joke
from get_song import play_song
from speak import Voice
from weather import get_weather


import sys

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
        elif "play" in response or "start" in response:
            play_song(" ".join(response.split()[1:]))
        elif "stop" in response or "quit" in response or "exit" in response:
            Voice.speak_flite("Dom Is Now Exiting")
            sys.exit()
        elif "weather" in response:
            get_weather()
        elif "news" in response:
            Voice.speak_flite(read_news_headlines(news_number))
            if "next" in response:
                news_number += 1
                Voice.speak_flite(read_news_headlines(news_number))
        elif "joke" in response:
            random_joke = joke()
            Voice.speak_flite(random_joke[0])
            Voice.speak_flite(random_joke[1])
        else:
            check = greet_user(response)
            if not check:
                search_wikipedia(response)
