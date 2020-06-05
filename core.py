import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import json
import pickle
import random
import os
import datetime
import sys
from get_song import play_video
from media_center import call_dom
from recognize import Recognize
from search import search_wikipedia, read_news_headlines, joke, get_recipe, translate_urdu_to_english, \
    translate_english_to_urdu, usd_to_pkr, pkr_to_usd
from speak import Voice
from users import create_user, get_all_users
from weather import get_weather
with open("intents.json") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)


model.load("model.tflearn")


#model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
#model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)



def chat():
    news_number = 1
    Name = ""
    Age = 0
    Birthday = ""
    while True:
        inp = Recognize.get_recognize_google()
        #inp = input("Input: ")
        if not inp:
            pass
        else:
            results = model.predict([bag_of_words(inp, words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[results_index]
            if results[results_index] > 0.7:
                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg['responses']
                if "song" == responses[0] and "songs" not in responses[0]:
                    if "song" in inp.lower():
                        inp = inp.replace("song", "", 1)
                    if " the " in inp.lower():
                        inp = inp.replace("the", "", 1)
                    if "play" in inp.lower():
                        inp = inp.replace("play", "", 1)
                    if "start" in inp.lower():
                        inp = inp.replace("start", "", 1)
                    if "video" in inp.lower():
                        inp = inp.replace("video", "", 1)
                    if "audio" in inp.lower():
                        inp = inp.replace("audio", "", 1)
                    inp = inp.replace(" ","")
                    Voice.speak_flite("Playing Audio - "+ inp)
                    play_video(inp.lower())
                elif "sleep" == responses[0]:
                    call_dom()
                elif "convert" == responses[0]:
                    us_string_place = 0
                    pkr_string_place = 0
                    for row in range(len(inp.split())):
                        inp = inp.lower()
                        if inp.split()[row] == "us":
                            us_string_place += row
                        elif inp.split()[row] == "rupees":
                            pkr_string_place += row
                    res = [int(i) for i in inp.split() if i.isdigit()][0]
                    if us_string_place > pkr_string_place:
                        number = pkr_to_usd(res)
                        Voice.speak_flite(str(number))
                    else:
                        number = usd_to_pkr(res)
                        Voice.speak_flite(str(number))
                elif "spelling" == responses[0]:
                    if "what" in inp:
                        inp = inp.replace("what","")
                    if "is" in inp:
                        inp = inp.replace("is","")
                    if "does" in inp:
                        inp = inp.replace("does","")
                    if "of" in inp:
                        inp = inp.replace("of","")
                    if "spelling" in inp:
                        inp = inp.replace("spelling","")
                    if "spell" in inp:
                        inp = inp.replace("spell","")
                    inp = inp.replace(" ","")
                    word = " ".join(inp)
                    for row in range(len(word)):
                        Voice.speak_flite(word[row])
                elif "maths" == responses[0]:
                    if 'square root' in inp:
                        num = [int(i) for i in inp.split() if i.isdigit()][0]
                        square_root = num ** 0.5
                        Voice.speak_flite(str(square_root))
                    else:
                        first = [int(i) for i in inp.split() if i.isdigit()][0]
                        second = [int(i) for i in inp.split() if i.isdigit()][1]
                        if '+' in inp:
                            Voice.speak_flite(str(first + second))
                        if '-' in inp:
                            Voice.speak_flite(str(first - second))
                        if '/' in inp:
                            Voice.speak_flite(str(first / second))
                        if '*' in inp:
                            Voice.speak_flite(str(first * second))
                elif "translate" == responses[0]:
                    if "translate" in inp:
                        inp = inp.replace("translate","")
                    if "to" in inp:
                        inp = inp.replace("to","")
                    if "what" in inp:
                        inp = inp.replace("what","")
                    if "does" in inp:
                        inp = inp.replace("does","")
                    if "english" in inp.lower():
                        inp = inp.replace("english","")
                        inp = inp.replace(" ","")
                        Voice.speak_flite(translate_urdu_to_english(inp))
                    elif "urdu" in inp.lower():
                        inp = inp.replace("urdu","")
                        inp = inp.replace(" ","")
                        Voice.speak_flite(translate_english_to_urdu(inp))
                elif "system" == responses[0]:
                    if "shutdown" in inp or "poweroff" in inp:
                        os.system("shutdown")
                    elif "reboot" in inp:
                        os.system("reboot")
                elif "time" == responses[0]:
                    currentDT = datetime.datetime.now()
                    if int(currentDT.strftime("%I")) <= 9:
                        Voice.speak_flite(currentDT.strftime("%I:%M %p").replace('0', '', 1))
                    else:
                        Voice.speak_flite(currentDT.strftime("%I:%M %p"))
                elif "day" == responses[0]:
                    currentDT = datetime.datetime.now()
                    Voice.speak_flite(currentDT.strftime("%A, %B, %Y"))
                elif "exit" == responses[0]:
                    break
                elif "recipe" == responses[0]:
                    if "recipe" in inp:
                        inp = inp.replace("recipe","")
                    elif "for" in inp:
                        inp = inp.replace("for","")
                    elif "of" in inp:
                        inp = inp.replace("of","")
                    inp = inp.replace("give","").replace("me","").replace(" a ","").replace("tell", "").replace("me","").replace("about","")
                    info = get_recipe(inp)
                    Voice.speak_flite(info[0])
                    Voice.speak_flite("You will need the following ingredients")
                    for row in info[1]:
                        Voice.speak_flite(row)
                    for row in info[2]:
                        Voice.speak_flite(row)
                elif "weather" == responses[0] and "i can play songs, tell the weather, tell a joke" not in responses[0]:
                    text = get_weather()
                    Voice.speak_flite(text)
                elif "news" == responses[0]:
                    if "next" in inp:
                        news_number += 1
                        Voice.speak_flite(read_news_headlines(news_number))
                    else:
                        Voice.speak_flite(read_news_headlines(news_number))
                elif "joke" == responses[0] and not "i can play songs, tell the weather, tell a joke" == responses[0]:
                    random_joke = joke()
                    Voice.speak_flite(random_joke[0])
                    Voice.speak_flite(random_joke[1])
                elif "update" == responses[0]:
                    os.system("cd / && ./update.sh")
                    sys.exit()
                elif "create" == responses[0]:
                    Voice.speak_flite("Say The Users Name You Want to Create")
                    name = Recognize.get_recognize_google()
                    Voice.speak_flite("Say The Users Age")
                    age = Recognize.get_recognize_google()
                    Voice.speak_flite("Say The Users Birthday")
                    birthday = Recognize.get_recognize_google()
                    Voice.speak_flite("Name, " + name + " Age, " + age + " Birthday, " + birthday)
                    Voice.speak_flite("Are you sure you want to create this user")
                    response = Recognize.get_recognize_google()
                    print(response)
                    if "yes" in response:
                        Voice.speak_flite("Creating User")
                        create_user(name, age, birthday)
                elif "user" == responses[0]:
                    for row in get_all_users():
                        response_split = inp.split()
                        for index in response_split:
                            if row[0] == index:
                                Name = row[0]
                                Age = row[1]
                                Birthday = row[2]
                                if row[0] == "Zara":
                                    Voice.speak_flite("Hello There Zarah, Welcome Back")
                                elif row[0] == "Ayaan":
                                    Voice.speak_flite("Hello There Aion, Welcome Back")
                                else:
                                    Voice.speak_flite("Hello There " + row[0] + ", Welcome Back")
                elif "info" == responses[0]:
                    if "birthday" in inp:
                        if Birthday:
                            Voice.speak_flite("Your Birthday comes on " + Birthday)
                        else:
                            Voice.speak_flite("Please say who you are")
                    elif "age" in inp:
                        if Age:
                            Voice.speak_flite("Your Age is " + str(Age))
                        else:
                            Voice.speak_flite("Please say who you are")
                    elif "name" in inp:
                        if Name:
                            if Name == "Ayaan":
                                Voice.speak_flite("Your Name is Aion")
                            elif Name == "Zara":
                                Voice.speak_flite("You Name is Zarah")
                            else:
                                Voice.speak_flite("Your Name is " + Name)
                        else:
                            Voice.speak_flite("Please say who you are")
                elif "search" == responses[0]:
                    inp = inp.split()
                    srch = []
                    for inp1 in inp:
                        inp = inp1
                        if "is" in inp and "histroy" not in inp:
                            pass
                        elif "was" in inp:
                            pass
                        elif "are" in inp:
                            pass
                        elif "of" in inp:
                            pass
                        elif "who" in inp:
                            pass
                        elif "what" in inp:
                            pass
                        elif "how" in inp:
                            pass
                        elif "why" in inp:
                            pass
                        elif "does" in inp:
                            pass
                        elif "tell" in inp:
                            pass
                        elif "me" in inp:
                            pass
                        elif "about" in inp:
                            pass
                        elif "to" in inp and "histroy" not in inp:
                            pass
                        else:
                            srch.append(inp)
                    inp = srch
                    Voice.speak_flite("Searching about " + " ".join(inp))
                    search = search_wikipedia(inp)
                    Voice.speak_flite(search)
                else:
                    Voice.speak_flite(random.choice(responses))
            else:
                Voice.speak_flite("I do not Understand Please Retry")
chat()
