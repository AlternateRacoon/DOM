import wikipedia
from speak import Voice
import random
def search_wikipedia(search):
    if "who is" in search or "who was" in search or "who are" in search or "what is" in search:
        Voice.speak_flite("Searching About it")
        search = search.split()[2:]
        search = " ".join(search)
        try:
            info = wikipedia.summary(search, sentences=2)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            info = wikipedia.summary(s, sentences=2)
        except wikipedia.PageError as e:
            Voic.speak_flite("Could not find any results")
        if info:
            Voice.speak_flite(info)
