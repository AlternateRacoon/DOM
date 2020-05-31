import os
import re
import urllib.request

from recognize import Recognize
from speak import Voice


def call_dom():
    Voice.speak_flite("dom is now going to sleep", "call again by saying dom")
    while True:
        response = Recognize.get_recognize_google()
        print(response)
        if response == False:
            pass
        elif "dom" in response.lower() or "start" in response.lower():
            Voice.speak_flite("Listening...")
            break


def connect_media_center():
    Voice.speak_flite("Connected to media center", "please speak your commands")
    while True:
        response = Recognize.get_recognize_google()
        print(response)
        if response == False:
            pass
        elif "break" in response or "back" in response or "continue" in response:
            break
        else:
            media_center_control("media center " + response)


def SearchMovie(movie_name):
    html_page = "http://www.emasti.pk/search?keyword=" + movie_name
    html_page = html_page.replace(" ", "+")

    html_data = urllib.request.urlopen(html_page).read().decode("utf-8")
    if '<h1>Error 404</h1>' in html_data:
        google_link = "https://www.google.com/search?q=" + movie_name
        google_link = google_link.replace(" ", "+")
        html_data = urllib.request.urlopen(
            urllib.request.Request(google_link,
                                   headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
            "utf8")
        movie_name = re.findall('<span>(.*?)</span>', html_data)
        movie_name = re.findall('AP7Wnd">(.*?)</div>', movie_name[0])
        if movie_name:
            movie_name = movie_name[0]
        else:
            movie_name = re.findall('<span>(.*?)</span>', html_data)
        html_page = "http://www.emasti.pk/search?keyword=" + movie_name
        html_page = html_page.replace(" ", "+")
        html_data = urllib.request.urlopen(html_page).read().decode("utf-8")
        movie_names = re.findall('" >(.*?)</a> </div>', html_data)
        movie_links = re.findall('<a class="name" href="(.*?)" >', html_data)
        mp4_links = []
        movie_posters = re.findall('<img src="(.*?)"', html_data)

        if "3d" in movie_names[0].lower():
            movie_list_number = 1
            if "3d" in movie_names[1].lower():
                movie_list_number = 2
        else:
            movie_list_number = 0
        movie_html = urllib.request.urlopen(movie_links[movie_list_number]).read().decode("utf-8")
        mp4_link = re.findall('<a href="(.*?)" class="vh_button red icon-down hover_right">Download</button></a></div>',
                              movie_html)
        if '3d' in mp4_link[0].lower():
            movie_list_number += 1
        movie_html = urllib.request.urlopen(movie_links[movie_list_number]).read().decode("utf-8")
        mp4_link = re.findall('<a href="(.*?)" class="vh_button red icon-down hover_right">Download</button></a></div>',
                              movie_html)
        if '3d' in mp4_link[0].lower():
            movie_list_number += 1
        movie_html = urllib.request.urlopen(movie_links[movie_list_number]).read().decode("utf-8")
        mp4_link = re.findall('<a href="(.*?)" class="vh_button red icon-down hover_right">Download</button></a></div>',
                              movie_html)
    else:

        movie_names = re.findall('" >(.*?)</a> </div>', html_data)
        movie_links = re.findall('<a class="name" href="(.*?)" >', html_data)
        mp4_links = []
        movie_posters = re.findall('<img src="(.*?)"', html_data)

        if "3d" in movie_names[0].lower():
            movie_list_number = 1
            if "3d" in movie_names[1].lower():
                movie_list_number = 2
        else:
            movie_list_number = 0
        movie_html = urllib.request.urlopen(movie_links[movie_list_number]).read().decode("utf-8")
        mp4_link = re.findall('<a href="(.*?)" class="vh_button red icon-down hover_right">Download</button></a></div>',
                              movie_html)
        if '3d' in mp4_link[0].lower():
            movie_list_number += 1
        movie_html = urllib.request.urlopen(movie_links[movie_list_number]).read().decode("utf-8")
        mp4_link = re.findall('<a href="(.*?)" class="vh_button red icon-down hover_right">Download</button></a></div>',
                              movie_html)
        if '3d' in mp4_link[0].lower():
            movie_list_number += 1
        movie_html = urllib.request.urlopen(movie_links[movie_list_number]).read().decode("utf-8")
        mp4_link = re.findall('<a href="(.*?)" class="vh_button red icon-down hover_right">Download</button></a></div>',
                              movie_html)

    return mp4_link[0]


def text2int(textnum, numwords={}):
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


def media_center_control(response):
    if "play" in response or "movie" in response:
        response = response.split()[3:]
        os.system("xbmc-client --url=" + SearchMovie("".join(response)))
    elif "play movie" in response or "open movie" in response or "start movie" in response:
        response = response.split()[4:]
        os.system("xbmc-client --url=" + SearchMovie("".join(response)))
    elif "up" in response:
        os.system("xbmc-client --up")
    elif "down" in response:
        os.system("xbmc-client --down")
    elif "right" in response:
        os.system("xbmc-client --right")
    elif "left" in response:
        os.system("xbmc-client --left")
    elif "play" in response:
        os.system("xbmc-client -p")
    elif "stop" in response:
        os.system("xbmc-client -p")
    elif "start" in response:
        os.system("xbmc-client -p")
    elif "exit" in response:
        os.system("xbmc-client --stop")
    elif "select" in response or "ok" in response:
        os.system("xbmc-client --select")
    elif "home" in response:
        os.system("xbmc-client --home")
    elif "videos" in response:
        os.system("xbmc-client --videos")
    elif "volume" in response:
        if len(response.split()) == 5:
            volume = text2int(response.split()[3] + " " + response.split()[4])
        if len(response.split()) == 4:
            volume = text2int(response.split()[3])
        os.system("xbmc-client --volume=" + str(volume))
    elif "mute" in response:
        os.system("xbmc-client --mute")
    elif "unmute" in response:
        os.system("xbmc-client --unmute")
