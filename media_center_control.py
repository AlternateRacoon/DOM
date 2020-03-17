import os
from threading import Thread

import pyaudio
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from media_center import media_center_control
from speak import Voice

try:
    from Queue import Queue, Full
except ImportError:
    from queue import Queue, Full

###############################################
#### Initalize queue to store the recordings ##
###############################################
CHUNK = 1024
# Note: It will discard if the websocket client can't consumme fast enough
# So, increase the max size as per your choice
BUF_MAX_SIZE = CHUNK * 10
# Buffer to store audio
q = Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK)))

# Create an instance of AudioSource
audio_source = AudioSource(q, True, True)

###############################################
#### Prepare Speech to Text Service ########
###############################################
Voice.speak_flite("Connected to media center", "please speak your commands")
# initialize speech to text service
authenticator = IAMAuthenticator('6w6sJ_t12M9VfKaXsCRWkpQlILb70e8mDVAciW6b_LQ8')
speech_to_text = SpeechToTextV1(authenticator=authenticator)


# define callback for the speech to text service
class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_transcription(self, transcript):

        response = transcript[0]["transcript"]
        print(response)
        if response == False:
            pass
        elif "break" in response or "back" in response or "continue" in response:
            Voice.speak_flite("going back to normal mode")
            os.system("python3 core_ibm.py")
        else:
            media_center_control("media center " + response)

    def on_connected(self):
        print('Connection was successful')

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

    def on_listening(self):
        print('Service is listening')

    def on_hypothesis(self, hypothesis):
        pass

    def on_data(self, data):
        pass

    def on_close(self):
        print("Connection closed")


# this function will initiate the recognize service and pass in the AudioSource
def recognize_using_weboscket(*args):
    mycallback = MyRecognizeCallback()
    speech_to_text.recognize_using_websocket(audio=audio_source,
                                             content_type='audio/l16; rate=44100',
                                             recognize_callback=mycallback,
                                             interim_results=True)


###############################################
#### Prepare the for recording using Pyaudio ##
###############################################

# Variables for recording the speech
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


# define callback for pyaudio to store the recording in queue
def pyaudio_callback(in_data, frame_count, time_info, status):
    try:
        q.put(in_data)
    except Full:
        pass  # discard
    return (None, pyaudio.paContinue)


# instantiate pyaudio
audio = pyaudio.PyAudio()

# open stream using callback
stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
    stream_callback=pyaudio_callback,
    start=False
)

#########################################################################
#### Start the recording and start service to recognize the stream ######
#########################################################################

print("Enter CTRL+C to end recording...")
stream.start_stream()

try:
    recognize_thread = Thread(target=recognize_using_weboscket, args=())
    recognize_thread.start()

    while True:
        pass
except KeyboardInterrupt:
    # stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    audio_source.completed_recording()
