import wikipedia
from speak import Voice
import random
import urllib.request
import re
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

    if "how" in search:
        if "to" in search:
            html_data = urllib.request.urlopen(
                urllib.request.Request("https://www.google.com/search?q=" + search,
                                       headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
                "utf8")
            ans = re.findall(
                '<div class="BNeawe s3v9rd AP7Wnd"><span class="FCUp0c rQMQod">(.*?)</div></li></ol>',
                html_data)
            if ans:
                ans = ans[0]
                ans = ans.replace('<span class="FCUp0c rQMQod">', '')
                ans = ans.replace('<span>', '')
                ans = ans.replace('</span>', '')
                ans = ans.replace('</div></div><div class="Ap5OSd"><ol class="mSx1Ee v7pIac"><li class="v9i61e"><div class="BNeawe s3v9rd AP7Wnd">', '')
                ans = ans.replace('</div></li><li class="v9i61e"><div class="BNeawe s3v9rd AP7Wnd">', '')
                ans = ans.replace('</div></li><li><div class="BNeawe s3v9rd AP7Wnd">', '')
                ans = ans.replace('</div>','')
                ans = ans.replace('<div><ol class="mSx1Ee v7pIac"><li class="v9i61e"><div class="BNeawe s3v9rd AP7Wnd">','')
                return ans
            else:
                return
        else:
            html_data = urllib.request.urlopen(
                urllib.request.Request("https://www.google.com/search?q=" + search,
                                       headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
                "utf8")
            ans = re.findall('<div class="BNeawe s3v9rd AP7Wnd"><div><div class="BNeawe s3v9rd AP7Wnd">(.*?)</div></div></div></div></div><div', html_data)
            if ans:
                ans = ans[0]
                ans = ans.replace('<span class="FCUp0c rQMQod">', '')
                ans = ans.replace('<span>','')
                ans = ans.replace('</span>', '')
                return ans
            else:
                ans = re.findall(
                    '</span>(.*?)</div></div></div></div></div></div></div></div><div><div class="',
                    html_data)
                if ans:
                    ans = ans[-3]
                    ans = ans.replace('<span class="FCUp0c rQMQod">', '')
                    ans = ans.replace('<span>', '')
                    ans = ans.replace('</span>', '')
                    ans = ans.replace('<span class="r0bn4c rQMQod"> ', '')
                    return ans
                else:
                    return
    if "when" in search:
        html_data = urllib.request.urlopen(
            urllib.request.Request("https://www.google.com/search?q=" + search,
                                   headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
            "utf8")

        ans = re.findall('<div><div class="BNeawe iBp4i AP7Wnd"><div><div class="BNeawe iBp4i AP7Wnd">(.*?)</div></div></div></div></div></div><div class="kvKEAb iafz5e">', html_data)
        if ans:
            ans = ans[0]
            ans = ans.replace('<span class="FCUp0c rQMQod">', '')
            ans = ans.replace('<span>','')
            ans = ans.replace('</span>', '')
            return ans
        else:
            return
    elif "is" in search:
        html_data = urllib.request.urlopen(
            urllib.request.Request("https://www.google.com/search?q=" + search,
                                   headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
            "utf8")

        ans = re.findall('<div class="BNeawe s3v9rd AP7Wnd">(.*?)</div></div></div></div></div>', html_data)
        if ans:
            ans = ans[0]
            ans = ans.replace('<span class="FCUp0c rQMQod">', '')
            ans = ans.replace('<span>','')
            ans = ans.replace('</span>', '')
            ans = ans.replace('<div class="BNeawe s3v9rd AP7Wnd">','')
            ans = ans.replace('<div>', '')
            ans = ans.replace('</div>', '')
            return ans
        else:
            return
    elif "why" in search:
        html_data = urllib.request.urlopen(
            urllib.request.Request("https://www.google.com/search?q=" + search,
                                   headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
            "utf8")

        ans = re.findall('<div class="BNeawe s3v9rd AP7Wnd">(.*?)</div></div></div></div></div>', html_data)
        if ans:
            ans = ans[0]
            ans = ans.replace('<span class="FCUp0c rQMQod">', '')
            ans = ans.replace('<span>','')
            ans = ans.replace('</span>', '')
            ans = ans.replace('<div class="BNeawe s3v9rd AP7Wnd">','')
            ans = ans.replace('<div>', '')
            ans = ans.replace('</div>', '')
            ans = ans.replace('<span class="r0bn4c rQMQod">','')
            return ans
        else:
            return
def search_wikipedia(search):
    if "who is" in search or "who was" in search or "who are" in search or "what is" in search or "what was" in search or "history of" in search:
        search1 = search
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
            google_search = search_google(search1)
            if google_search:
                Voice.speak_flite(google_search)
            else:
                Voice.speak_flite("Could not find any results")
        if info:
            Voice.speak_flite(info)
    elif "tell me about" in search:
        search1 = search
        search = " ".join(search.split()[2:])
        Voice.speak_flite("Searching about "+ search)
        info = ""
        try:
            info = wikipedia.summary(search, sentences=2)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            info = wikipedia.summary(s, sentences=2)
        except wikipedia.PageError as e:
            google_search = search_google(search1)
            if google_search:
                Voice.speak_flite(google_search)
            else:
                Voice.speak_flite("Could not find any results")
        if info:
            Voice.speak_flite(info)
    return "who is" in search or "who was" in search or "who are" in search or "what is" in search or "what was" in search or "history of" in search or "tell me about" in search
