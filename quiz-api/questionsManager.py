import question
import sqlite3
import answer

def create_question(payload):
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()

        query = "INSERT INTO question (position, title, text, image) VALUES (?, ?, ?, ?)"
        values = (payload['position'], payload['title'], payload['text'], payload['image'])

        c.execute(query, values)

        question_id = c.lastrowid

        for answerInQuestion in payload['possibleAnswers']:
            query = "INSERT INTO answer (question_id, text, isCorrect) VALUES (?, ?, ?)"
            values = (question_id, answerInQuestion['text'], answerInQuestion['isCorrect'])
            c.execute(query, values)

        db_connection.commit()

    return question_id







