import sqlite3
from flask import jsonify

def create_question(payload):
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()

        c.execute("SELECT COUNT(*) FROM question")
        number_of_questions = c.fetchone()[0]
        new_position = payload['position']

        if new_position < 1 or new_position > number_of_questions + 1: #On prend en compte la question que l'on va ajouter juste après d'ou le +1
            raise ValueError("Invalid position (musn't be less than 1 or greater than questions length + 1)")
        
        c.execute("UPDATE question SET position=position+1 WHERE position >= ?", (new_position,))

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
        current_position = c.fetchone()[0]
        if current_position == None:
            raise ValueError("Question not found")

        c.execute("SELECT COUNT(*) FROM question")
        number_of_questions = c.fetchone()[0]
        new_position = payload['position']

        if new_position < 1 or new_position > number_of_questions:
            raise ValueError("Invalid position (musn't be less than 1 or greater than questions length)")

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

        for answer in payload['possibleAnswers']:
            query = "INSERT INTO answer (text, isCorrect, question_id) VALUES (?, ?, ?)"
            values = (answer['text'], answer['isCorrect'], question_id_request)
            c.execute(query, values)

        db_connection.commit()

def get_question_by_id(question_id_request):
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()

        c.execute("SELECT * FROM question WHERE id=?", (question_id_request,))
        question_content = c.fetchone()

        if question_content is None:
            return jsonify({'message': 'Question not found'}), 404

        c.execute("SELECT * FROM answer WHERE question_id=?", (question_id_request,))
        answers_content = c.fetchall()
        question_answers = []

        for answer in answers_content:
            question_answers.append({
                'id': answer[0],
                'text': answer[1],
                'isCorrect': answer[2],
                'question_id': question_id_request 
            })
        
        question = {
            'id': question_id_request,
            'position': question_content[1],
            'title': question_content[2],
            'text': question_content[3],
            'image': question_content[4],
            'possibleAnswers': question_answers            
        }

        return jsonify({'question': question}), 200
    
def get_question_by_position(position):
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()

        c.execute("SELECT * FROM question WHERE position=?", (position,))
        question_content = c.fetchone()

        if question_content is None:
            return jsonify({'message': 'Question not found'}), 404

        c.execute("SELECT * FROM answer WHERE question_id=?", (question_content[0],))
        answers_content = c.fetchall()
        question_answers = []

        for answer in answers_content:
            question_answers.append({
                'id': answer[0],
                'text': answer[1],
                'isCorrect': answer[2],
                'question_id': question_content[0] 
            })
        
        question = {
            'id': question_content[0],
            'position': question_content[1],
            'title': question_content[2],
            'text': question_content[3],
            'image': question_content[4],
            'possibleAnswers': question_answers            
        }

        return jsonify({'question': question}), 200







