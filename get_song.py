import re
import subprocess
import urllib.parse
import urllib.request
from time import sleep
from recognize import Recognize
import pafy
import os
from speak import Voice


def play_video(video_name):
    query_string = urllib.parse.urlencode({"search_query": song_name})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    url = "https://www.youtube.com/watch?v=" + search_results[0]
    video = pafy.new(url)
    best = video.getbest()
    cmd = ['mplayer','-novideo','-ao','oss', best.url]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    sleep(5)
    while True:
        command = Recognize.get_recognize_google()
        print(command)
        if command == False:
            pass
        else:
            if "pause" in command or "stop" in command or "exit" in command or "quit" in command:
                os.system("pkill mplayer")
                break
def play_song(song_name):
    song_name = song_name.replace(" ", "+")
    html_data = urllib.request.urlopen(
        urllib.request.Request("https://songspk.mobi/search?q="+ song_name,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
        "utf8")
    link = "https://songspk.mobi"+ re.findall('<a href="(.*?)"', html_data)[23]
    html_data = urllib.request.urlopen(
        urllib.request.Request(link,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
        "utf8")
    if "<h4>Your search did not yield any results.</h4>" in html_data:
        Voice.speak_flite("I am afraid, i cannot find any songs of that name")
    else:
        mp3_link = re.findall('<a href="(.*?)" download="" class="btn btn-block btn-default">', html_data)[0]

        cmd = ['mplayer','-novideo', '-ao', 'oss', mp3_link]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        sleep(5)
        while True:
            command = Recognize.get_recognize_google()
            print(command)
            if command == False:
                pass
            else:
                if "pause" in command or "stop" in command or "exit" in command or "quit" in command or "top" in command:
                    os.system("pkill mplayer")
                    break
                elif "download to server" in command or "save to server" in command or "download" in command:
                    os.system("pkill mplayer")
                    os.system("sudo mount -t cifs -o user=root,pass=dietpi //192.168.1.111/dietpi /Dietpi")
                    Voice.speak_flite("Saving The File")
                    os.system("cd /Dietpi && wget '"+ mp3_link + "'")
                    break



    
