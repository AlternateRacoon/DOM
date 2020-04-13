sudo rm -rf /DOM
cd / &&  git clone https://github.com/AlternateRacoon/DOM.git
cd / && rm users.db
cd / && wget https://github.com/AlternateRacoon/DOM/raw/master/users.db
cd /DOM && python3 core.py
