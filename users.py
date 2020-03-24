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
    elif "I am" in response:
        for row in get_all_users():
            response_split = response.split()
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
                        Voice.speak_flite("Hello There "+ row[0] +", Welcome Back")
    elif "what is my birthday" in response or "when is my birthday" in response:
        if Birthday:
            Voice.speak_flite("Your Birthday comes on " + Birthday)
        else:
            Voice.speak_flite("Please say who you are")
    elif "what is my age" in response:
        if Age:
            Voice.speak_flite("Your Age is " + str(Age))
        else:
            Voice.speak_flite("Please say who you are")
    elif "what is my name" in response:
        if Name:
            if Name == "Ayaan":
                Voice.speak_flite("Your Name is Aion")
            elif Name == "Zara":
                Voice.speak_flite("You Name is Zarah")
            else:
                Voice.speak_flite("Your Name is " + Name)
        else:
            Voice.speak_flite("Please say who you are")

