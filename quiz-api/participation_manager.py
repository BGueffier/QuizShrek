import sqlite3
from flask import jsonify

def get_quiz_infos():
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()

        c.execute("SELECT COUNT(*) FROM question")
        number_of_questions = c.fetchone()[0]

        c.execute("SELECT * FROM participation ORDER BY score DESC")
        participation_content = c.fetchall()
        participations = []

        for participation in participation_content:
            participations.append({
                'playerName': participation[1],
                'score': participation[2],
                'date': participation[3]
            })

        result = {
            'size': number_of_questions,
            'scores': participations
        }
        
        return jsonify(result), 200
    
def add_participation(player_name, answers):
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()

        c.execute("SELECT COUNT(*) FROM question")
        number_of_questions = c.fetchone()[0]

        if len(answers) != number_of_questions:
             return jsonify({'message': 'Bad Request: answers length must be equal to the number of questions in the quiz.'}), 400

        return jsonify(''), 200