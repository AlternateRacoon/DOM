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


