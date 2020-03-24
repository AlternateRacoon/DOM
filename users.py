from speak import Voice
from recognize import Recognize

import sqlite3

conn = sqlite3.connect('users.db')


def create_user(name, age, birthday):
    conn.execute("INSERT INTO users (NAME,AGE,BIRTHDAY) \
          VALUES ('"+ name +"',"+ age +", '"+ birthday +"')");
    conn.commit()
    conn.close()
def delete_user(name):
    conn.execute("DELETE from users where NAME = '"+ name +"';")
    conn.commit()
    conn.close()
def get_all_users():
    cursor = conn.execute("SELECT * from users")
    return cursor.fetchall()
    conn.commit()
    conn.close()


Name = ""
Age = 0
Birthday = ""

def user_stuff(response):
    if "create user" in response:
        Voice.speak_mimic("Say The Users Name You Want to Create")
        name = Recognize.get_recognize_google()
        Voice.speak_mimic("Say The Users Age")
        age = Recognize.get_recognize_google()
        Voice.speak_mimic("Say The Users Birthday")
        birthday = Recognize.get_recognize_google()
        Voice.speak_mimic("Name, " + name + " Age, " + age + " Birthday, " + birthday)
        Voice.speak_mimic("Are you sure you want to create this user")
        response = Recognize.get_recognize_google()
        print(response)
        if "yes" in response:
            Voice.speak_mimic("Creating User")
            create_user(name, age, birthday)
    elif "I am" in response:
        for row in get_all_users():
            response_split = response.split()
            for index in response_split:
                if row[0] == index:
                    Name = row[0]
                    Age = row[1]
                    Birthday = row[2]
                    if row[0] == "Zara":
                        Voice.speak_mimic("Hello There Zarah, Welcome Back")
                    elif row[0] == "Ayaan":
                        Voice.speak_mimic("Hello There Aion, Welcome Back")
    elif "what is my birthday" in response or "when is my birthday" in response:
        if Birthday:
            Voice.speak_mimic("Your Birthday comes on " + Birthday)
        else:
            Voice.speak_mimic("Please say who you are")
    elif "what is my age" in response:
        if Age:
            Voice.speak_mimic("Your Age is " + str(Age))
        else:
            Voice.speak_mimic("Please say who you are")
    elif "what is my name" in response:
        if Name:
            if Name == "Ayaan":
                Voice.speak_mimic("Your Name is Aion")
            elif Name == "Zara":
                Voice.speak_mimic("You Name is Zarah")
            else:
                Voice.speak_mimic("Your Name is " + Name)
        else:
            Voice.speak_mimic("Please say who you are")

