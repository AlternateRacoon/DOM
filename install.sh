sudo apt-get install -y youtube-dl 
sudo apt-get install -y portaudio19-dev 
sudo apt-get install -y git
sudo apt-get install -y python3 python3-dev python3-pip
sudo apt-get install -y flac
wget https://files.pythonhosted.org/packages/ab/42/b4f04721c5c5bfc196ce156b3c768998ef8c0ae3654ed29ea5020c749a6b/PyAudio-0.2.11.tar.gz
tar -xzvf PyAudio-0.2.11.tar.gz
cd PyAudio-0.2.11 && python3 setup.py install
wget https://files.pythonhosted.org/packages/26/e1/7f5678cd94ec1234269d23756dbdaa4c8cfaed973412f88ae8adf7893a50/SpeechRecognition-3.8.1-py2.py3-none-any.whl
pip3 install SpeechRecognition-3.8.1-py2.py3-none-any.whl
cd / && git clone https://github.com/festvox/flite.git
cd /flite && ./configure && make && wget https://github.com/MycroftAI/mimic1/raw/development/voices/mycroft_voice_4.0.flitevox
pip3 install wikipedia
pip3 install pafy
pip3 install pygame
pip3 install gtts
pip3 install ibm_watson
pip3 install ibm_cloud_sdk_core
pip3 install youtube-dl
sudo apt-get install mpv
cd / && git clone https://github.com/AlternateRacoon/DOM.git
cd /DOM && python3 core.py
