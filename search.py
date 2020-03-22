import wikipedia
from speak import Voice
import random
def search_wikipedia(search):
    if "who is" in search or "who was" in search or "who are" in search or "what is" in search or "what was" in search or "history of" in search:
        search = search.split()[2:]
        search = " ".join(search)
        Voice.speak_flite("Searching about "+ search)
        info = ""
        try:
            info = wikipedia.summary(search, sentences=2)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            info = wikipedia.summary(s, sentences=2)
        except wikipedia.PageError as e:
            Voice.speak_flite("Could not find any results")
        if info:
            Voice.speak_flite(info)
    elif "tell me about" in search:
        search = " ".join(search.split()[2:])
        Voice.speak_flite("Searching about "+ search)
        info = ""
        try:
            info = wikipedia.summary(search, sentences=2)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            info = wikipedia.summary(s, sentences=2)
        except wikipedia.PageError as e:
            Voice.speak_flite("Could not find any results")
        if info:
            Voice.speak_flite(info)   
def read_news_headlines(news_number):
    html_data = urllib.request.urlopen(
        urllib.request.Request("https://www.geo.tv/category/pakistan",
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
        "utf8")
    news_link = re.findall('<a data-vr-contentbox="Category Pakistan '+ str(news_number) +'" data-vr-contentbox-url="(.*?)" class="open-section" href="', html_data)[0]
    html_data = urllib.request.urlopen(
        urllib.request.Request(news_link,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
        "utf8")
    lines = re.findall("<p>(.*?)</p>", html_data)
    if lines[0]:
        lines = lines[0].replace("<i>","").replace("</i>","")
    elif lines[1]:
        lines = lines[1].replace("<i>", "").replace("</i>", "")
    elif lines[2]:
        lines = lines[2].replace("<i>", "").replace("</i>", "")
    elif lines[3]:
        lines = lines[3].replace("<i>", "").replace("</i>", "")
    return lines
