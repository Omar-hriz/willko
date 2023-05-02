import sqlite3


def get_users():
    connection = sqlite3.connect('dataBase.db')
    cursor = connection.cursor()
    result = cursor.execute("select * from Users").fetchall()
    connection.close()
    return result


def add_event(user1, start, end, summary):
    connection = sqlite3.connect('dataBase.db')
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Events ("user","start","end","summary") VALUES ('{}', '{}', '{}', '{}');""".format(user1, start, end, summary))
    connection.commit()
    connection.close()

