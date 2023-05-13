import sqlite3

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

def delete_question(question_id_request):
    with sqlite3.connect('database.db') as db_connection:
        c = db_connection.cursor()

        c.execute("SELECT * FROM question WHERE id=?", (question_id_request,))
        if c.fetchone() == None:
            raise ValueError("Question not found")

        c.execute('DELETE FROM answer WHERE question_id = ?', (question_id_request,))
        c.execute('DELETE FROM question WHERE id = ?', (question_id_request,))

        db_connection.commit()

def delete_all_question():
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()

        c.execute("DELETE FROM answer")
        c.execute("DELETE FROM question")
        db_connection.commit()

def update_question(payload, question_id_request):
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()

        c.execute("SELECT position FROM question WHERE id=?", (question_id_request,))
        if c.fetchone() == None:
            raise ValueError("Question not found")
        current_position = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM question")
        num_questions = c.fetchone()[0]
        new_position = payload['position']

        if new_position < 1 or new_position > num_questions:
            raise ValueError("Invalid position")

        if new_position != current_position:
            if new_position < current_position:
                shift_range = (new_position, current_position - 1)
                shift_offset = 1
            else:
                shift_range = (current_position + 1, new_position)
                shift_offset = -1

            c.execute("UPDATE question SET position=position+? WHERE position BETWEEN ? AND ?", (shift_offset, shift_range[0], shift_range[1]))

        query = "UPDATE question SET position=?, title=?, text=?, image=? WHERE id=?"
        values = (payload['position'], payload['title'], payload['text'], payload['image'], question_id_request)
        c.execute(query, values)

        c.execute("DELETE FROM answer WHERE question_id=?", (question_id_request,))

        # Insert new answers
        for answer in payload['possibleAnswers']:
            query = "INSERT INTO answer (text, isCorrect, question_id) VALUES (?, ?, ?)"
            values = (answer['text'], answer['isCorrect'], question_id_request)
            c.execute(query, values)

        db_connection.commit()







