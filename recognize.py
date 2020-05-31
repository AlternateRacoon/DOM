import speech_recognition as sr


class Recognize():
    @staticmethod
    def get_recognize_ibm():
        r = sr.Recognizer()
        speech = sr.Microphone()
        authenticator = IAMAuthenticator('api_key')
        speech_to_text = SpeechToTextV1(
            authenticator=authenticator
        )
        with speech as source:
            print("Listening....")
            audio_file = r.listen(source)
        print("recognizing")
        speech_recognition_results = speech_to_text.recognize(audio=audio_file.get_wav_data(),
                                                              content_type='audio/wav').get_result()
        if speech_recognition_results["results"]:
            recog = speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
            recog = recog.replace("don't", "dom")
            recog = recog.replace("dome", "dom")
            recog = recog.replace("your view", "YouTube")
            recog = recog.replace("please", "play")
        else:
            recog = False
        return recog

    @staticmethod
    def get_recognize_google():
        r = sr.Recognizer()
        speech = sr.Microphone(device_index=0)
        # for recognizing speech
        with speech as source:
            print("Listening…")
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        print("recognizing")
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }
        try:
            response["transcription"] = r.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"
        recog = response["transcription"]
        if recog:
            recog = recog.replace("Don", "Dom")
            if "I am" in recog:
                recog = recog.replace("Iron", "Ayaan")
            print(recog)
            return recog
        else:
            return False

    @staticmethod
    def get_recognize_sphinx():
        r = sr.Recognizer()
        speech = sr.Microphone(device_index=0)
        # for speech recognition
        with speech as source:
            print("Listening…")
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        print("recognizing")
        recog = r.recognize_sphinx(audio)
        recog = recog.replace("don't", "dom")
        recog = recog.replace("dome", "dom")
        recog = recog.replace("your view", "YouTube")
        return recog

    @staticmethod
    def get_recognize_all():
        r = sr.Recognizer()
        speech = sr.Microphone()
        with speech as source:
            print("Listening…")
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        authenticator = IAMAuthenticator('api_key')
        speech_to_text = SpeechToTextV1(
            authenticator=authenticator
        )
        print("recognizing")
        recog_sphinx = r.recognize_sphinx(audio)
        recog_google = r.recognize_google(audio)
        recog_ibm = \
        speech_to_text.recognize(audio=audio.get_wav_data(), content_type='audio/wav').get_result()["results"][0][
            "alternatives"][0]["transcript"]
        return recog_google, recog_ibm, recog_sphinx
