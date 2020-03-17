from recognize import Recognize
from media_center import media_center_control,call_dom, connect_media_center
from greetings import greet_user
from search import search_wikipedia
from get_song import play_song


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
        greet_user(response)
        search_wikipedia(response)
