import random
import re
import urllib.request

import wikipedia
from speak import Voice


def read_news_headlines(news_number):
    html_data = urllib.request.urlopen(
        urllib.request.Request("https://www.geo.tv/category/pakistan",
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
        "utf8")
    news_link = re.findall('<a data-vr-contentbox="Category Pakistan ' + str(
        news_number) + '" data-vr-contentbox-url="(.*?)" class="open-section" href="', html_data)[0]
    html_data = urllib.request.urlopen(
        urllib.request.Request(news_link,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
        "utf8")
    lines = re.findall("<p>(.*?)</p>", html_data)
    if lines[0]:
        lines = lines[0].replace("<i>", "").replace("</i>", "")
    elif lines[1]:
        lines = lines[1].replace("<i>", "").replace("</i>", "")
    elif lines[2]:
        lines = lines[2].replace("<i>", "").replace("</i>", "")
    elif lines[3]:
        lines = lines[3].replace("<i>", "").replace("</i>", "")
    return lines.replace('"', '').replace("<br>", "").replace("</br>", "")


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
    search = search.replace(" ", "+")
    if "how" in search:
        if " to " in search:
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
                ans = ans.replace(
                    '</div></div><div class="Ap5OSd"><ol class="mSx1Ee v7pIac"><li class="v9i61e"><div class="BNeawe s3v9rd AP7Wnd">',
                    '')
                ans = ans.replace('</div></li><li class="v9i61e"><div class="BNeawe s3v9rd AP7Wnd">', '')
                ans = ans.replace('</div></li><li><div class="BNeawe s3v9rd AP7Wnd">', '')
                ans = ans.replace('</div>', '')
                ans = ans.replace(
                    '<div><ol class="mSx1Ee v7pIac"><li class="v9i61e"><div class="BNeawe s3v9rd AP7Wnd">', '')
                return ans
            else:
                return
        else:
            link = "https://www.google.com/search?q=" + search
            html_data = urllib.request.urlopen(
                urllib.request.Request(link,
                                       headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
                "utf8")
            ans = re.findall(
                '<div class="BNeawe s3v9rd AP7Wnd"><div><div class="BNeawe s3v9rd AP7Wnd">(.*?)</div></div></div></div></div><div',
                html_data)
            if ans:
                ans = ans[0]
                ans = ans.replace('<span class="FCUp0c rQMQod">', '')
                ans = ans.replace('<span>', '')
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
        ans = re.findall('AP7Wnd">(.*?)</div>', html_data)
        if ans:
            if '</span><span class="BNeawe s3v9rd AP7Wnd">' in ans[0]:
                ans = ans[1]
            else:
                ans = ans[0]
            ans = ans.replace('<div><div class="BNeawe iBp4i AP7Wnd">', '')
            ans = ans.replace('<div class="Ap5OSd"><div class="BNeawe s3v9rd AP7Wnd">', '')
            ans = ans.replace('<span class="FCUp0c rQMQod">', '')
            ans = ans.replace('<span>', '')
            ans = ans.replace('</span>', '')
            ans = ans.replace('<div class="Ap5OSd">', '')
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
            ans = ans.replace('<span>', '')
            ans = ans.replace('</span>', '')
            ans = ans.replace('<div class="BNeawe s3v9rd AP7Wnd">', '')
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
            ans = ans.replace('<span>', '')
            ans = ans.replace('</span>', '')
            ans = ans.replace('<div class="BNeawe s3v9rd AP7Wnd">', '')
            ans = ans.replace('<div>', '')
            ans = ans.replace('</div>', '')
            ans = ans.replace('<span class="r0bn4c rQMQod">', '')
            return ans
        else:
            return


def search_wikipedia(search):
    search1 = search
    search = search
    info = False
    try:
        info = wikipedia.summary(search, sentences=2)
    except wikipedia.DisambiguationError as e:
        s = random.choice(e.options)
        info = wikipedia.summary(s, sentences=2)
    except wikipedia.PageError as e:
        google_search = search_google(search1)
        if google_search:
            return google_search
        else:
            return "Could not find any results about it"
    if info:
        return info.replace('"', '')



def get_recipe(recipe_name):
    recipe_name = recipe_name.replace(" ", "%20")
    html_data = urllib.request.urlopen(
        urllib.request.Request("https://www.allrecipes.com/search/results/?wt=" + recipe_name,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
    link = re.findall(
        '<a href="(.*?)" data-content-provider-id="" data-internal-referrer-link="hub recipe" data-internal-',
        html_data)

    html_data = urllib.request.urlopen(
        urllib.request.Request(link[0],
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
    description = html_data.splitlines()[129].replace("description", "").replace('"', '').replace(':', '')
    number = 144
    steps = []
    while number < len(html_data.splitlines()[148:]):
        number += 1
        if '"text": "' in html_data.splitlines()[number]:
            steps.append(html_data.splitlines()[number].replace('"', '').replace('text', '').replace(':', ''))
        if number > 300:
            break
    ingredients = []
    for row in html_data.splitlines()[134:]:
        if '        ],' in row:
            break
        elif "recipeIngredient:" in row:
            pass
        else:
            ingredients.append(
                row.replace("½", "half").replace("¼", "one fourth").replace("1 ½", "one and a half").replace("2 ½",
                                                                                                             "two and a half").replace(
                    "3 ½", "three and a half").replace("4 ½", "4 and a half").replace("¾", "three fourth").replace('"',
                                                                                                                   '').replace(
                    ',', '').replace('recipeIngredient: [', ''))
    return description, ingredients, steps


def translate_urdu_to_english(word):
    url = "https://www.urdupoint.com/dictionary/roman-urdu-word-" + word + ".html"
    html_data = urllib.request.urlopen(
        urllib.request.Request(url,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf8')
    link = re.findall('<a class="m_words" href="(.*?)">', html_data)
    if len(link) == 0:
        return "no word found"
    else:
        html_data = urllib.request.urlopen(
            urllib.request.Request(link[0],
                                   headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf8')
        word = re.findall('<p class="fwb fs30 lh38 mean ac">(.*?)</p>', html_data)
        return word[0]


def translate_english_to_urdu(word):
    url = "https://www.urdupoint.com/dictionary/english-word-" + word + ".html"
    html_data = urllib.request.urlopen(
        urllib.request.Request(url,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf8')
    link = re.findall('<a class="m_words" href="(.*?)">', html_data)
    if len(link) == 0:
        return "no word found"
    else:
        link = link[0]
    html_data = urllib.request.urlopen(
        urllib.request.Request(link,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf8')
    urdu_word = re.findall('<p class="fs13 txt_gray mt5 ac">(.*?)</p>', html_data)
    return urdu_word[0]


def usd_to_pkr(usd):
    usd = int(usd)
    url = "http://free.currconv.com/api/v7/convert?q=USD_PKR&compact=ultra&apiKey=0f8c9f694a57c5574bff"
    html_data = urllib.request.urlopen(
        urllib.request.Request(url,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf8').replace('{"USD_PKR":',
                                                                                                     '').replace("}",
                                                                                                                 "")
    currency = float(html_data)
    price = round(currency * usd)
    return price


def pkr_to_usd(pkr):
    pkr = int(pkr)
    url = "http://free.currconv.com/api/v7/convert?q=PKR_USD&compact=ultra&apiKey=0f8c9f694a57c5574bff"
    html_data = urllib.request.urlopen(
        urllib.request.Request(url,
                               headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf8').replace('{"PKR_USD":',
                                                                                                     '').replace("}",
                                                                                                                 "")
    currency = float(html_data)
    price = currency * pkr
    return price

