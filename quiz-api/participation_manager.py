import sqlite3
from flask import jsonify
import datetime

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
        
        query_correct_answers_position = """
        SELECT 
            (SELECT COUNT(*) + 1 FROM Answer ans WHERE ans.question_id = q.id AND ans.id < a.id) AS answer_index 
        FROM Question q 
        JOIN Answer a 
        ON q.id = a.question_id 
        AND a.isCorrect = 1
        """
        c.execute(query_correct_answers_position)
        correct_answers_position = []
        answers_position = c.fetchall()
        for position in answers_position:
            correct_answers_position.append(int(position[0]))

        answers_summaries = []
        player_score = 0
        
        for i, answer in enumerate(answers):
            wasCorrect = bool(answer == correct_answers_position[i])
            if wasCorrect == True:
                player_score += 1
            answers_summaries.append({
                'correctAnswerPosition': correct_answers_position[i],
                'wasCorrect': wasCorrect
            })
        
        date = datetime.datetime.now()
        formattedDate = date.strftime("%d/%m/%Y %H:%M:%S")

        c.execute("INSERT INTO participation (playerName, score, date) VALUES (?, ?, ?)", (player_name, player_score, formattedDate,))

        result = {
            'answersSummaries': answers_summaries,
            'playerName': player_name,
            'score': player_score
        }

        return jsonify(result), 200
    
def delete_all_participation():
    with sqlite3.connect("database.db") as db_connection:
        c = db_connection.cursor()
        c.execute("DELETE FROM participation")
        db_connection.commit()
        return jsonify({'message': 'No Content'}), 204