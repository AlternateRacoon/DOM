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
def joke():
    html_data = urllib.request.urlopen(
        urllib.request.Request("https://www.beano.com/categories/jokes",
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
        "utf8")
    questions = re.findall('"question":"(.*?)"', html_data)
    answers = re.findall('"answer":"(.*?)"', html_data)
    jokes = []
    for row in range(len(questions)):
        joke = []
        joke.append(questions[row])
        joke.append(answers[row])
        jokes.append(joke)
    return random.choice(jokes)
def search_google(search):
    search = search.replace(" ","+")
    html_data = urllib.request.urlopen(
        urllib.request.Request("https://www.google.com/search?q=" + search,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
        "utf8")

    ans = re.findall('<div class="BNeawe s3v9rd AP7Wnd"><div><div class="BNeawe s3v9rd AP7Wnd">(.*?)</div></div></div></div></div><div', html_data)[0]
    ans = ans.replace('<span class="FCUp0c rQMQod">', '')
    ans = ans.replace('<span>','')
    ans = ans.replace('</span>', '')
    return ans

