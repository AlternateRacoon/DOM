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
     
