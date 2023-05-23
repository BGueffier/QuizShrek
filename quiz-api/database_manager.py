import sqlite3

def rebuild_database():
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()

        c.execute('''DROP TABLE IF EXISTS answer''')
        c.execute('''DROP TABLE IF EXISTS question''')
        c.execute('''DROP TABLE IF EXISTS participation''')


        c.execute('''CREATE TABLE "question" (
                    "id"	INTEGER NOT NULL,
                    "position"	INTEGER NOT NULL,
                    "title"	TEXT NOT NULL,
                    "text"	TEXT NOT NULL,
                    "image"	TEXT NOT NULL,
                    PRIMARY KEY("id" AUTOINCREMENT))''')

        c.execute('''CREATE TABLE "answer" (
                    "id"	INTEGER NOT NULL,
                    "text"	TEXT NOT NULL,
                    "isCorrect"	INTEGER NOT NULL,
                    "question_id"	INTEGER NOT NULL,
                    FOREIGN KEY("question_id") REFERENCES "question"("id"),
                    PRIMARY KEY("id" AUTOINCREMENT))''')
            
        c.execute('''CREATE TABLE "participation" (
                    "id"	INTEGER NOT NULL,
                    "playerName"	TEXT NOT NULL,
                    "score"	INTEGER NOT NULL,
                    "date"	TEXT NOT NULL,
                    PRIMARY KEY("id" AUTOINCREMENT))''')

        db_connection.commit()
        