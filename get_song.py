import re
import subprocess
import urllib.parse
import urllib.request
from time import sleep
from recognize import Recognize
import pafy


def play_song(song_name):
    query_string = urllib.parse.urlencode({"search_query": song_name})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    url = "https://www.youtube.com/watch?v=" + search_results[0]
    video = pafy.new(url)
    best = video.getbest()
    cmd = ['mplayer','-novideo','-ao','oss','-slave', '-quiet', best.url]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    sleep(5)
    while True:
        command = Recognize.get_recognize_google()
        print(command)
        if "pause" in command or "stop" in command or "exit" in command or "quit" in command:
            p.stdin.write(b'\nquit\n')
            os.system("pkill mplayer")
            break
    if "pause" in command or "stop" in command or "exit" in command or "quit" in command:
        p.stdin.write(b'\nquit\n')
        os.system("pkill mplayer")

    
