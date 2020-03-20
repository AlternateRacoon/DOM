import wikipedia
from speak import Voice
def search_wikipedia(search):
    if "who is" in search or "who was" in search or "who are" in search or "what is" in search:
        search = search.split()[2:]
        search = " ".join(search)
        try:
            info = wikipedia.summary(search, sentences=2)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            info = wikipedia.page(s)
        Voice.speak_flite(info)
