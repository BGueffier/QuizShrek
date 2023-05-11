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

def update_question(payload, question_id_request):
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()

        query = "UPDATE question SET position = ?, title = ?, text = ?, image = ? WHERE id = ?"
        values = (payload['position'], payload['title'], payload['text'], payload['image'], question_id_request)

        c.execute(query, values)

        for answerInQuestion in payload['possibleAnswers']:
            print(answerInQuestion['text'])
            print(answerInQuestion['isCorrect'])
            print(question_id_request)
            queryAnswers = "UPDATE answer SET text = ?, isCorrect = ? WHERE question_id = ?"
            valuesAnswers = (answerInQuestion['text'], answerInQuestion['isCorrect'], question_id_request)
            c.execute(queryAnswers, valuesAnswers)

        db_connection.commit()






